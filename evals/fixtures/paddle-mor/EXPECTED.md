# Expected — paddle-mor

- Provider détecté : Paddle → `commercial_model=merchant_of_record`,
  `recovery_owner=provider/hybrid`.
- Aucun moteur de retry custom n'est présent dans ce fixture, et **ce
  n'est pas un manque** : `status=NOT_APPLICABLE` pour ce point (Paddle
  gère nativement les retries jusqu'à 7 sur 30 jours).
- `subscription.past_due` : audité, handler présent.
- Restauration des droits après `transaction.completed` (paiement
  récupéré) : présente et auditée (`accounts.restore_entitlements`).
- Ne pas signaler l'absence de moteur de retry comme un finding P0/P1 —
  voir règle D de `references/audit-patterns.md`.
