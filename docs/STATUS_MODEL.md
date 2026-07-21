# Status Model

## Statuts (`status`)

| Statut | Signification |
|---|---|
| `VERIFIED` | Mécanisme confirmé fonctionnellement relié (normalement preuve L3/L4). |
| `PARTIAL` | Mécanisme présent mais incomplet ou preuve insuffisante (L1/L2). |
| `ABSENT` | Recherché activement, non trouvé dans le repo. |
| `EXTERNAL_UNKNOWN` | Dépend d'un réglage dashboard non versionné — ne jamais confondre avec `ABSENT`. |
| `NOT_APPLICABLE` | Le point ne s'applique pas à ce contexte produit/provider. |
| `DATA_REQUIRED` | Le mécanisme dépend de données de production absentes du repo statique. |
| `CONTEXT_REQUIRED` | Le contexte produit (usage type, core action...) manque pour conclure. |
| `STRATEGY_REQUIRED` | Décision humaine/stratégique nécessaire (T1, T5, T6, T9, T12). |
| `BLOCKED` | L'audit ne peut pas progresser sur ce point (dépendance manquante, accès refusé). |

## Niveaux de confiance (`confidence`)

- `HIGH` — preuve directe et non ambiguë (L3/L4, ou documentation officielle).
- `MEDIUM` — preuve indirecte ou partielle (L1/L2, ou étude sérieuse mais contexte limité).
- `LOW` — signal faible, extrapolation, ou source marketing/secondaire.

## Sévérité (`severity`)

- `P0` — impact revenu direct probable, à traiter avant tout le reste.
- `P1` — impact significatif mais non bloquant immédiatement.
- `P2` — amélioration, ROI incertain ou différé.
- `INFO` — observation sans action requise.

## Catégories d'automatisation (`automation`)

| Catégorie | Exemples |
|---|---|
| `AUTO_SAFE` | Génération de rapport, doc, tests non destructifs, instrumentation sans PII validée, validation JSON, checklist. |
| `AUTO_WITH_APPROVAL` | Modification de code, migration, webhook, email, cron/job, droits, cancel flow — nécessite confirmation explicite avant mutation. |
| `MANUAL_EXTERNAL` | Dashboards providers, DNS, email provider, App Store, Google Play. |
| `MANUAL_CODE` | Modification de code jugée trop risquée pour AUTO_WITH_APPROVAL sans supervision humaine continue. |
| `DATA_DEPENDENT` | Nécessite des données de production absentes du repo. |
| `STRATEGY_HUMAN` | Discount, rétention d'un segment, définition de l'aha moment/outcome, qualification bad-fit, choix pricing. |
| `NOT_APPLICABLE` | Sans objet dans ce contexte. |

## Niveaux de preuve (`evidence_level`)

Voir `docs/EXECUTION_FLOW.md#phase-4-evidence-tracing` pour la définition
complète (L0 à L4). Règle clé : un terme trouvé dans un commentaire, un
log, ou une chaîne de caractères ne dépasse jamais L0, et ne peut donc
jamais justifier un statut `VERIFIED`.

## Combinaisons interdites

- `status=ABSENT` + preuve `EXTERNAL_UNKNOWN` par nature (réglage dashboard)
  → utiliser `EXTERNAL_UNKNOWN`, jamais `ABSENT`.
- `status=VERIFIED` + `evidence_level` ∈ {L0, L1} → interdit, rétrograder en
  `PARTIAL` au mieux.
- `automation=AUTO_WITH_APPROVAL` sans `requires_explicit_approval: true`
  dans le manifeste → interdit (voir schema).
- Findings sur T1/T5/T6/T9/T12 avec conclusion stratégique définitive →
  toujours forcer `STRATEGY_REQUIRED` sur la conclusion, même si
  l'instrumentation est `VERIFIED`.
