# Data Contract

Modèle cible documenté à titre de référence — ne pas imposer une base de
données spécifique. Utile pour évaluer `data_readiness` (Phase 5) et pour
un futur pipeline analytics.

## accounts

`account_id`, `signup_at`, `plan_id`, `contract_type`, `currency`,
`mrr_minor`, `seats_licensed`, `seats_active`, `renewal_at`,
`product_usage_type`.

## billing_accounts

`account_id`, `provider`, `provider_customer_id`, `provider_subscription_id`,
`subscription_status`, `cancel_at_period_end`, `canceled_at`.

## usage_daily

`account_id`, `date`, `active_users`, `sessions`, `core_actions`,
`distinct_core_features`, `outcome_events`.

## support_daily

`account_id`, `date`, `tickets_opened`, `tickets_resolved`, `csat`,
`sentiment`, `last_customer_reply_at`.

## payment_events

`provider_event_id`, `account_id`, `provider`, `invoice_id`, `occurred_at`,
`status`, `decline_code`, `attempt_count`, `next_attempt_at`,
`amount_due_minor`, `currency`.

## interventions

`intervention_id`, `account_id`, `signal`, `action`, `started_at`,
`outcome`, `outcome_at`.

## Règles

- `account_id` interne stable, distinct de tout identifiant provider.
- `user_id` séparé de `account_id` (un compte peut avoir plusieurs
  utilisateurs).
- `provider_customer_id` séparé, mappé explicitement vers `account_id`.
- Montants toujours en unités mineures (centimes), jamais en flottant
  décimal direct.
- Devise obligatoire sur tout montant.
- Dates en ISO-8601, avec fuseau horaire explicite.
- `provider_event_id` unique — sert de clé d'idempotence pour les
  webhooks (voir `docs/PROVIDER_MATRIX.md`).
- Pas de PII au-delà du nécessaire (éviter de stocker des champs libres
  non requis par le scoring ou la remédiation).
