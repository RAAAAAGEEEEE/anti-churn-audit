// Fixture synthétique — code original écrit pour cet eval, aucune source tierce.
const express = require("express");
const Stripe = require("stripe");
const stripe = Stripe(process.env.STRIPE_SECRET_KEY);
const db = require("./db");

const router = express.Router();

router.post("/api/webhooks/stripe", express.raw({ type: "application/json" }), async (req, res) => {
  let event;
  try {
    event = stripe.webhooks.constructEvent(
      req.body,
      req.headers["stripe-signature"],
      process.env.STRIPE_WEBHOOK_SECRET
    );
  } catch (err) {
    return res.status(400).send(`Webhook signature verification failed: ${err.message}`);
  }

  const alreadyProcessed = await db.webhookEvents.exists(event.id);
  if (alreadyProcessed) {
    return res.status(200).json({ received: true, deduped: true });
  }
  await db.webhookEvents.markProcessed(event.id);

  switch (event.type) {
    case "invoice.payment_failed": {
      const invoice = event.data.object;
      await db.accounts.markPastDue(invoice.customer, invoice.id);
      break;
    }
    case "invoice.paid": {
      const invoice = event.data.object;
      await db.accounts.restoreEntitlements(invoice.customer);
      await db.accounts.clearPastDue(invoice.customer);
      break;
    }
    case "customer.subscription.deleted": {
      const sub = event.data.object;
      await db.accounts.revokeEntitlements(sub.customer);
      break;
    }
    default:
      break;
  }

  res.status(200).json({ received: true });
});

module.exports = router;
