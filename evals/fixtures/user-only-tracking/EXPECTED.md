# Expected — user-only-tracking

- Modèle de compte détecté : B2B organisation (`organizationId` utilisé en
  facturation, sièges multiples) — voir `billing.js`.
- Analytics détecté : événements produit trackés uniquement avec
  `userId`, aucun `organizationId`/`account_id` dans le payload
  (`analytics.js`).
- Conséquence : impossible de calculer un score d'adoption ou d'usage
  fiable **au niveau compte** (S1, S4, S7) tant que ce mapping user →
  account n'existe pas côté analytics.
- Le score account-level doit être bloqué ou affiché avec
  `data_coverage` réduite ; ne jamais présenter un `risk_score`
  account-level comme fiable ici.
- Un plan de remédiation account-level (ajouter `organizationId` aux
  événements trackés) doit être proposé — voir règle B.
