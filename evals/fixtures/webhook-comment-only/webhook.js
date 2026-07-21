// Fixture synthétique — code original écrit pour cet eval, aucune source tierce.
const express = require("express");
const router = express.Router();

// TODO: vérifier la signature du webhook Stripe et gérer l'idempotence
// via event_id avant de traiter l'event. Pas encore implémenté.
router.post("/api/webhooks/stripe", express.json(), async (req, res) => {
  const event = req.body;
  console.log("received stripe event (unverified)", event.type);
  res.status(200).json({ received: true });
});

module.exports = router;
