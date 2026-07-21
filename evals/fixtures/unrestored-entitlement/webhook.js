// Fixture synthétique — code original écrit pour cet eval, aucune source tierce.
const Stripe = require("stripe");
const stripe = Stripe(process.env.STRIPE_SECRET_KEY);
const db = require("./db");

async function handleStripeEvent(rawBody, signature) {
  const event = stripe.webhooks.constructEvent(rawBody, signature, process.env.STRIPE_WEBHOOK_SECRET);

  if (event.type === "invoice.payment_failed") {
    await db.accounts.markPastDue(event.data.object.customer);
    await db.accounts.restrictAccess(event.data.object.customer);
  }

  if (event.type === "invoice.paid") {
    // NOTE fixture : on efface le flag past_due mais on ne restaure
    // jamais l'accès complet (restrictAccess n'est jamais annulé ici).
    await db.accounts.clearPastDue(event.data.object.customer);
  }

  return { received: true };
}

module.exports = { handleStripeEvent };
