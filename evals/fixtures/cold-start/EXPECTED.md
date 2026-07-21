# Expected — cold-start

- `signup_at` du compte fixture est récent (< 14 jours au moment de
  l'audit) → `product_context.cold_start = true`.
- Aucune alerte "silent churn" ne doit être présentée comme définitive
  pour ce compte (S1/S2 non fiables si disponibles, ou marqués
  `available: false`).
- Le rapport doit router vers un plan d'onboarding/activation (point T2),
  pas vers un plan de rétention silent-churn — voir règle G.
