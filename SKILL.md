---
name: anti-churn-audit
description: >
  Audite statiquement un repo SaaS pour détecter les mécanismes anti-churn
  visibles dans le code (onboarding, paiements échoués, silent churn,
  cancellation flow, win-back...), distingue ce qui est vérifiable dans le
  code de ce qui dépend de données, de réglages externes (dashboard
  provider) ou de décisions stratégiques humaines, calcule un risk_score
  heuristique déterministe (risk-engine) avec couverture de données
  explicite, et produit un rapport Markdown + JSON + manifeste de
  remédiation actionnable. Lecture seule par défaut. À utiliser quand
  l'utilisateur veut auditer la rétention/churn d'un SaaS, vérifier
  l'intégration Stripe/Paddle/Lemon Squeezy/Chargebee/RevenueCat côté
  paiements échoués et webhooks, ou générer un plan de remédiation
  anti-churn priorisé (P0/P1/P2).
---

# anti-churn-audit

Audit statique anti-churn pour SaaS, en quatre modes : `audit` (défaut),
`plan`, `fix`, `verify`. Lecture seule sauf en mode `fix` avec confirmation
explicite.

Ce document est le point d'entrée. Le détail de chaque phase est dans
`docs/EXECUTION_FLOW.md` ; les statuts et catégories dans
`docs/STATUS_MODEL.md` ; le scoring dans `docs/SCORING_MODEL.md` ; la
matrice provider dans `docs/PROVIDER_MATRIX.md` ; les règles de
déclenchement conditionnel dans `references/audit-patterns.md`.

## Principe directeur

Ne jamais confondre quatre niveaux de certitude :

1. **Visible dans le code**, avec preuve tracée (L0-L4).
2. **Efficacité nécessitant des données** de production (ex : le
   `risk_score` sans historique suffisant).
3. **Réglage externe** nécessitant un dashboard (Smart Retries, DNS...).
4. **Décision stratégique** nécessitant interviews ou jugement humain
   (discount, bad-fit, pricing).

Chaque finding porte un `status` qui reflète ce niveau (voir
`docs/STATUS_MODEL.md`) — jamais une affirmation plus forte que la preuve
disponible.

## Modes d'exécution

### MODE 1 — AUDIT (défaut)

`/anti-churn-audit audit`

- Lecture seule, aucune modification du repo audité.
- Exécute les phases 0 à 12 de `docs/EXECUTION_FLOW.md`.
- Produit les 6 artefacts de sortie (voir `docs/REPORT_FORMAT.md`).
- Peut écrire uniquement dans le dossier de sortie explicitement validé
  par l'utilisateur.

Si l'utilisateur ne précise pas de mode, choisir AUDIT.

### MODE 2 — PLAN

`/anti-churn-audit plan <finding-id>`

- Reprend un finding existant (dans `remediation-manifest.json` ou
  `REMEDIATION_PLAN.md` d'un audit précédent).
- Inspecte les fichiers concernés.
- Produit un plan précis (fichiers à modifier, tests requis, rollback).
- Ne modifie jamais le code.

### MODE 3 — FIX

`/anti-churn-audit fix <finding-id>`

- Exige un finding existant et son statut/`automation`.
- Si `automation` = `MANUAL_EXTERNAL` ou `STRATEGY_HUMAN` : refuser, et
  rappeler qu'aucune automatisation n'est possible pour ce type d'action.
- Si `automation` = `AUTO_WITH_APPROVAL` : afficher les fichiers ciblés,
  expliquer l'impact, demander confirmation explicite avant toute
  mutation.
- Propose les fichiers à modifier, crée/modifie les tests, exécute les
  validations locales disponibles (lint/typecheck/tests ciblés), produit
  un diff final (`git diff --stat`) et un plan de rollback.
- Ne jamais `reset`, `push`, déployer, ou modifier un dashboard externe.

### MODE 4 — VERIFY

`/anti-churn-audit verify <finding-id|all>`

- Vérifie que les corrections appliquées tiennent (fichiers générés,
  schémas JSON, preuves, statuts, tests).
- N'ajoute aucune nouvelle fonctionnalité.
- Met à jour le statut et les preuves dans le rapport existant.

## Pipeline (résumé — détail complet dans docs/EXECUTION_FLOW.md)

```
Phase 0  Preflight (SHA, git status, dossier de sortie)
Phase 1  Discovery (stack, providers séparés, comptes, analytics...)
Phase 2  Product context (usage type, account model, core action)
Phase 3  Static mechanism audit (T2/T3/T4/T7/T8/T10/T11 + S1-S8)
Phase 4  Evidence tracing (niveaux L0-L4)
Phase 5  Data readiness
Phase 6  External settings (checklist manuelle, EXTERNAL_UNKNOWN)
Phase 7  Strategy boundaries (T1/T5/T6/T9/T12 → STRATEGY_REQUIRED)
Phase 8  Classification (status/severity/confidence/automation)
Phase 9  Conditional triggers (règles A-K, references/audit-patterns.md)
Phase 10 Scoring (risk-engine, risk_score + data_coverage)
Phase 11 Remediation decision (manifeste actionnable)
Phase 12 Output (6 artefacts, validation JSON)
Phase 13 Optional apply (mode FIX uniquement, avec confirmation)
Phase 14 Verify (mode VERIFY uniquement)
```

**Ordre strict** — ne jamais sauter une phase, ne jamais scorer avant
d'avoir classifié, ne jamais classifier avant d'avoir tracé les preuves.

## risk-engine

Le moteur de scoring interne de ce skill s'appelle **`risk-engine`**. Il
est déterministe en P0 : pondérations fixes mais configurables par produit,
aucun modèle entraîné. Voir `docs/SCORING_MODEL.md` pour la formule
complète, les poids par défaut (S1=28, S2=20, S3=16, S4=12, S5=8, S6=8,
S7=4, S8=4), et la règle de `data_coverage < 0.50` → `INSUFFICIENT_DATA`.

Une interface d'extension est préparée (calibration statistique, modèle ML
avec validation temporelle, explications type SHAP, apprentissage depuis
`interventions.outcome`) mais **aucun de ces éléments n'est actif en P0**
— ne jamais laisser un rapport suggérer le contraire.

## Provider matrix

Voir `docs/PROVIDER_MATRIX.md`. Règle clé : chaque provider est audité
séparément (`commercial_model` × `recovery_owner`), jamais fusionné en un
statut global si plusieurs providers coexistent (règle F).

## Statuts et automatisation

Voir `docs/STATUS_MODEL.md` pour la liste complète. Résumé des statuts
autorisés : `VERIFIED`, `PARTIAL`, `ABSENT`, `EXTERNAL_UNKNOWN`,
`NOT_APPLICABLE`, `DATA_REQUIRED`, `CONTEXT_REQUIRED`, `STRATEGY_REQUIRED`,
`BLOCKED`. Catégories d'automatisation : `AUTO_SAFE`,
`AUTO_WITH_APPROVAL`, `MANUAL_EXTERNAL`, `MANUAL_CODE`, `DATA_DEPENDENT`,
`STRATEGY_HUMAN`, `NOT_APPLICABLE`.

## Sortie

6 artefacts obligatoires dans `<output-dir>/` — voir
`docs/REPORT_FORMAT.md` pour le détail complet et les gabarits dans
`templates/`. Valider systématiquement avec :

```
python3 scripts/validate_report.py <output-dir>/anti-churn-audit.json
python3 scripts/validate_manifest.py <output-dir>/remediation-manifest.json
```

## Limites honnêtes

- Aucune précision prédictive garantie — `risk_score` est heuristique,
  pas un modèle calibré (voir `docs/SCORING_MODEL.md`).
- Aucune récupération de revenu garantie.
- Compatibilité provider non exhaustive — voir `docs/PROVIDER_MATRIX.md`.
- Aucun appel réseau, aucune donnée envoyée par défaut — voir
  `docs/SECURITY.md`.

## Attribution

Ce skill est une réimplémentation originale inspirée par l'exploration
publique du problème de churn scoring, notamment ChurnGuard AI. Aucun
code, prompt ou contenu de notebook tiers n'a été repris — voir
`docs/LEGAL_AND_ATTRIBUTION.md` pour le détail complet et la justification
clean-room.
