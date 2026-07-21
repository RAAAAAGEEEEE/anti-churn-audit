# Scoring — détails d'implémentation

Complète `docs/SCORING_MODEL.md`. Voir ce document pour la formule et les
poids. Ce fichier détaille comment renseigner `risk_i` par signal.

## Définition de `risk_i` par signal (valeurs par défaut, à calibrer)

| Signal | `risk_i = 1.0` (risque maximal) quand… | `risk_i = 0.0` quand… |
|---|---|---|
| S1 usage trend | baisse d'activité soutenue vs baseline du compte | activité stable ou en hausse |
| S2 days inactive | inactivité > seuil configuré pour le `product_usage_type` | dernière activité récente |
| S3 payment failures | échec de paiement en cours, tentatives épuisées | aucun échec récent |
| S4 feature adoption breadth | usage d'une seule fonctionnalité cœur, rien d'autre | adoption large du produit |
| S5 contract type | mensuel, sans engagement | annuel ou pluriannuel engagé |
| S6 support | tickets répétés, sentiment négatif, pas de réponse client | support calme, sentiment neutre/positif |
| S7 seat utilization | sièges achetés très supérieurs aux sièges actifs | utilisation proche de 100% des sièges |
| S8 MRR decline | downgrade récent ou baisse de MRR mesurée | MRR stable ou en hausse |

`risk_i` peut être une valeur continue entre 0 et 1 (ex : ratio normalisé),
pas uniquement 0 ou 1. Documenter la formule exacte utilisée par produit
dans le champ `scoring.weights_profile` du rapport.

## Cold-start

Si `product_context.cold_start = true` (produit < 14 jours ou compte en
onboarding), S1 et S2 doivent être marqués `available: false` par défaut,
et le rapport doit rediriger vers le plan d'onboarding plutôt que produire
un `risk_score` définitif (voir règle G,
`references/audit-patterns.md`).

## Usage périodique/saisonnier

Ne pas appliquer un seuil `+14 jours sans connexion` pour S2 si
`product_context.usage_type` ∈ {`periodic`, `seasonal`}. Utiliser la
cadence attendue (`expected_value_window_days`), le renouvellement, et le
paiement comme signaux prioritaires à la place (voir règle H).

## P1 — calibration et account-level (préparé, pas requis en P0)

- Calibrer les poids par cohorte à partir de `interventions.outcome`
  (voir `references/data-contract.md`) une fois suffisamment de données
  historiques disponibles.
- Distinguer GRR (Gross Revenue Retention) et NRR (Net Revenue Retention)
  au niveau compte, pas seulement au niveau utilisateur.
- Ne calculer un score account-level fiable que si `account_id` est stable
  et mappé (voir `data_readiness.account_id_stable` dans le schema).

## P2 — ML (préparé, jamais actif par défaut)

- Un modèle ML ne remplace le scoring déterministe qu'après validation
  temporelle (split chronologique, pas aléatoire) et calibration
  (Brier score ou reliability diagram documentés).
- Les explications par signal (type SHAP) viennent en complément des
  preuves L0-L4, jamais en remplacement.
- Voir `docs/SCORING_MODEL.md#interface-dextension`.
