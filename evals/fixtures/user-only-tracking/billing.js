// Fixture synthétique — code original écrit pour cet eval, aucune source tierce.
// Modèle de facturation : un compte "organization" paie pour N sièges
// (plusieurs users). Voir schema organizations / organization_members.
const Stripe = require("stripe");
const stripe = Stripe(process.env.STRIPE_SECRET_KEY);

async function createOrgSubscription(organizationId, seatCount) {
  return stripe.subscriptions.create({
    customer: organizationId, // mappé côté Stripe vers un organization_id
    items: [{ price: process.env.STRIPE_SEAT_PRICE_ID, quantity: seatCount }],
  });
}

module.exports = { createOrgSubscription };
