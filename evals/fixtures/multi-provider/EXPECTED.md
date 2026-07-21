# Expected — multi-provider

- Deux providers détectés : Stripe (`merchant_direct`) et Paddle
  (`merchant_of_record`) — coexistence réelle (migration partielle selon
  le commentaire du fixture).
- Le rapport doit produire **une sous-section par provider** dans
  `ANTI_CHURN_AUDIT.md`, jamais un statut global fusionné.
- Aucun `risk_score` combiné ne doit être calculé sans documenter la
  normalisation entre les deux providers (statuts `past_due` équivalents
  mais noms d'événements différents).
- Un mapping account ↔ provider doit être demandé/vérifié (quel compte
  utilise quel provider) avant tout score account-level fiable — sinon
  marquer `CONTEXT_REQUIRED` ou `DATA_REQUIRED` sur cette partie.
