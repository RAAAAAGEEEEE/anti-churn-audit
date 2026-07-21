// Fixture synthétique — code original écrit pour cet eval, aucune source tierce.
const express = require("express");
const Stripe = require("stripe");
const stripe = Stripe(process.env.STRIPE_SECRET_KEY);

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

  // NOTE fixture : seul customer.subscription.deleted est géré.
  // invoice.payment_failed n'a aucun handler — les paiements échoués
  // n'entraînent aucune action côté application.
  if (event.type === "customer.subscription.deleted") {
    console.log("subscription deleted", event.data.object.id);
  }

  res.status(200).json({ received: true });
});

module.exports = router;
