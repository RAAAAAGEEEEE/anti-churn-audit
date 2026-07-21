// Fixture synthétique — code original écrit pour cet eval, aucune source tierce.
// Legacy : ce provider a été ajouté après une migration partielle depuis
// Stripe pour certains plans annuels ; les deux coexistent encore.
async function handlePaddleWebhook(event) {
  if (event.event_type === "subscription.past_due") {
    return { provider: "paddle", action: "mark_past_due", customer: event.data.customer_id };
  }
  return { provider: "paddle", action: "noop" };
}

module.exports = { handlePaddleWebhook };
