# Expected — stripe-incomplete

- `invoice.payment_failed` : absent du `switch`/`if` — aucune action côté
  application quand un paiement échoue (pas de marquage past_due, pas de
  notification).
- Finding correspondant : `status=ABSENT` (ou `PARTIAL` si un handler vide
  existe), `severity=P0` (impact revenu direct : les comptes en échec de
  paiement ne sont jamais signalés côté app).
- `automation=AUTO_WITH_APPROVAL` — nécessite d'ajouter un handler,
  modification de code.
- `EXTERNAL_CHECKLIST.md` doit quand même rappeler de vérifier Smart
  Retries côté dashboard Stripe, indépendamment de ce manque côté code.
- Ne pas marquer `VERIFIED` sur la base de la seule présence du webhook
  route — la chaîne s'arrête avant toute action pour ce type d'event.
