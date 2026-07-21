// Fixture synthétique — code original écrit pour cet eval, aucune source tierce.
const Stripe = require("stripe");
const stripe = Stripe(process.env.STRIPE_SECRET_KEY);

async function handleStripeWebhook(rawBody, signature) {
  const event = stripe.webhooks.constructEvent(rawBody, signature, process.env.STRIPE_WEBHOOK_SECRET);
  if (event.type === "invoice.payment_failed") {
    return { provider: "stripe", action: "mark_past_due", customer: event.data.object.customer };
  }
  return { provider: "stripe", action: "noop" };
}

module.exports = { handleStripeWebhook };
