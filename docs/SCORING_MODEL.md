# Scoring Model — risk-engine

## Nom et échelle

Le score s'appelle exclusivement **`risk_score`** (0 = risque faible,
100 = risque maximal). Ne jamais le présenter comme une probabilité
calibrée, un « churn probability », ou une « precision prédictive » sans
modèle entraîné, validé temporellement et calibré (voir P2 dans
`references/scoring.md`).

## Tiers initiaux (configurables)

| Plage | Tier |
|---|---|
| 0-29 | LOW |
| 30-49 | MEDIUM |
| 50-69 | HIGH |
| 70-100 | CRITICAL |

Ces bornes sont des valeurs par défaut, pas des seuils universels — à
recalibrer par produit/cohorte (voir `references/scoring.md`).

## Poids heuristiques initiaux (normalisés sur 100)

| Signal | Description | Poids |
|---|---|---|
| S1 | Usage trend | 28 |
| S2 | Days inactive | 20 |
| S3 | Payment failures | 16 |
| S4 | Feature adoption breadth | 12 |
| S5 | Contract type | 8 |
| S6 | Support | 8 |
| S7 | Seat utilization | 4 |
| S8 | MRR decline | 4 |
| **Total** | | **100** |

Ces poids sont configurables, pas une sortie de modèle ML. Aucun seuil
universel ne doit être présenté comme une certitude — voir `SOURCES.md`
pour le niveau de confiance des benchmarks sous-jacents.

## Formule avec signaux manquants

```
risk_score = 100 × Σ(weight_i × risk_i × available_i)
                  ÷ Σ(weight_i × available_i)
```

- `risk_i` ∈ [0, 1] : intensité du risque pour le signal i.
- `available_i` ∈ {0, 1} : disponibilité du signal i pour ce compte/produit.

## Data coverage

```
data_coverage = Σ(weight_i × available_i) ÷ 100
```

**Règle bloquante :** si `data_coverage < 0.50`, ne pas afficher un score
définitif. Afficher `INSUFFICIENT_DATA`, fournir le score exploratoire
uniquement dans les détails, et expliquer précisément quels signaux
manquent (voir `scoring.insufficient_data` dans le schema).

## Segmentation obligatoire

- Seuils différents par `product_usage_type` (daily/weekly/periodic/
  transactional/seasonal/custom).
- Configuration par produit (pas un seul jeu de poids global si plusieurs
  produits sont audités).
- Cold-start : voir règle G de `references/audit-patterns.md` — pas
  d'alerte silent churn fiable avant 14 jours ou compte non renseigné.
- Scoring au niveau `account` par défaut pour B2B ; au niveau `user` si
  B2C ou si aucun account_id stable n'existe (voir règle B).
- Score déterministe **avant** toute option ML (le déterministe reste la
  référence P0 ; le ML est une extension P2, jamais un prérequis).

## Interface d'extension (préparée, non activée en P0)

Le format `scoring` du schema JSON réserve les champs suivants pour de
futures extensions, sans les rendre obligatoires :

- `engine_version` — pour distinguer les révisions de pondération ;
- `weights_profile` — nom du profil de poids utilisé (permet une
  calibration par produit/cohorte sans changer le schema) ;
- point d'extension documentaire (pas encore un champ schema) pour :
  - calibration statistique des poids à partir d'historique de résultats ;
  - modèle ML entraîné, avec validation temporelle (train/test splits
    respectant la chronologie) et calibration (Brier score, reliability
    diagram) avant tout affichage en production ;
  - explications par signal de type SHAP ou équivalent, en complément
    (jamais en remplacement) des preuves L0-L4 déjà produites ;
  - apprentissage à partir des `interventions.outcome` du data contract
    (voir `references/data-contract.md`), pour ajuster les poids ou le
    scoring au fil du temps.

Tant qu'aucun de ces éléments n'est implémenté et validé, le rapport ne doit
jamais suggérer qu'un tel système est actif.
