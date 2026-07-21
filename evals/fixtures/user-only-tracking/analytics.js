// Fixture synthétique — code original écrit pour cet eval, aucune source tierce.
const analytics = require("./analytics-client");

function trackCoreAction(userId, actionName, properties) {
  // Tous les événements sont envoyés avec un user_id uniquement.
  // Il n'existe aucun account_id ou organization_id dans ce payload,
  // alors que le produit est vendu par abonnement à des organisations
  // (plusieurs utilisateurs par compte payant).
  analytics.track({
    userId,
    event: actionName,
    properties,
  });
}

module.exports = { trackCoreAction };
