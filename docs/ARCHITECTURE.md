# Architecture

## Vue d'ensemble

`anti-churn-audit` est un skill Claude, pas un service réseau. Il n'y a pas
de serveur, pas de base de données, pas d'appel API externe requis pour le
mode AUDIT. Tout tourne dans le contexte d'exécution de Claude Code contre
le repo local de l'utilisateur.

```
repo utilisateur (lecture seule en mode audit)
        │
        ▼
 SKILL.md (pipeline phases 0-14)
        │
        ├─ Discovery (stack, providers, analytics, comptes)
        ├─ Product context (usage type, account model)
        ├─ Static mechanism audit (points Tibo T2/T3/T4/T7/T8/T10/T11)
        ├─ Evidence tracing (niveaux L0-L4)
        ├─ Data readiness
        ├─ External settings checklist
        ├─ Strategy boundaries (T1/T5/T6/T9/T12)
        ├─ Classification (status/severity/confidence/automation)
        ├─ Conditional triggers (A-K)
        ├─ risk-engine scoring (déterministe, poids configurables)
        ├─ Remediation decision
        └─ Output (Markdown + JSON + manifeste)
        │
        ▼
 <output-dir>/
   ANTI_CHURN_AUDIT.md
   anti-churn-audit.json      ──▶ scripts/validate_report.py
   REMEDIATION_PLAN.md
   remediation-manifest.json  ──▶ scripts/validate_manifest.py
   EXTERNAL_CHECKLIST.md
   evidence/evidence-index.json
```

## Pourquoi pas de framework

Le pipeline est une séquence de phases textuelles décrites dans
`docs/EXECUTION_FLOW.md` et exécutées par le modèle, pas du code applicatif.
Les seuls artefacts exécutables sont :

- `scripts/validate_report.py` et `scripts/validate_manifest.py` — validation
  JSON pure stdlib ;
- les schémas JSON qui définissent le contrat de sortie ;
- les fixtures/evals qui vérifient le comportement du pipeline.

Cela évite d'introduire une dépendance lourde (ORM, service, queue) pour un
outil qui doit rester exécutable dans n'importe quel repo, hors ligne.

## risk-engine

Le sous-système de scoring (voir `docs/SCORING_MODEL.md` et
`references/scoring.md`) est nommé **`risk-engine`** en interne. Il est
volontairement déterministe en P0 (pondérations fixes mais configurables,
pas de modèle entraîné) avec un point d'extension explicite pour brancher
plus tard une calibration statistique ou un modèle ML (voir
`docs/SCORING_MODEL.md#interface-dextension`).

## Séparation public / privé

Ce dépôt est la **source de vérité fonctionnelle**. Un overlay privé
(`anti-churn-audit-private`, hors de ce dépôt) peut ajouter des conventions
personnelles et une intégration à un agent personnel, sans dupliquer manuellement les
règles publiques — voir le build déterministe décrit dans le README du
dépôt privé.
