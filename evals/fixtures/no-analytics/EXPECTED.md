# Expected — no-analytics

- `package.json` ne contient aucune dépendance analytics connue (pas de
  Segment, Amplitude, PostHog, Mixpanel, RudderStack...).
- Aucun événement produit (`core_action`, `outcome_event`) n'est
  détectable côté code.
- Le rapport ne doit **pas** générer de health score comportemental basé
  sur des signaux d'usage (S1, S4 notamment) — ces signaux doivent être
  marqués `available: false`.
- `scoring.insufficient_data` probable si la couverture descend sous 50%.
- Un plan d'instrumentation doit être proposé, avec une sévérité P0 ou P1
  selon si le produit a déjà des clients payants (contexte à demander).
- Le scoring comportemental global est marqué `DATA_REQUIRED`.
