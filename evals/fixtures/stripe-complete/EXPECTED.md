# Expected — stripe-complete

- Webhook Stripe : signature vérifiée via `stripe.webhooks.constructEvent`
  sur le corps brut (`express.raw`) → chaîne complète jusqu'à L3/L4
  (test présent dans `webhook.test.js`).
- Idempotence : `db.webhookEvents.exists(event.id)` avant traitement →
  contrôle event_id présent, `status=VERIFIED` possible.
- `invoice.payment_failed` → `markPastDue` : présent.
- `invoice.paid` → `restoreEntitlements` + `clearPastDue` : présent
  (restauration des droits après récupération).
- Smart Retries (dashboard Stripe) : ne peut pas être confirmé depuis ce
  code → `EXTERNAL_UNKNOWN`, jamais `ABSENT`.
- Aucun moteur de retry custom ne doit être recommandé en P0/P1 pour ce
  fixture — Stripe gère nativement les retries.
