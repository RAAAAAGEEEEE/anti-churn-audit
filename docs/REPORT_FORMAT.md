# Report Format

## Fichiers de sortie obligatoires

```
<output-dir>/
├── ANTI_CHURN_AUDIT.md
├── anti-churn-audit.json
├── REMEDIATION_PLAN.md
├── remediation-manifest.json
├── EXTERNAL_CHECKLIST.md
└── evidence/
    └── evidence-index.json
```

Le Markdown doit rester compréhensible par un non-codeur. Le JSON doit
respecter `schemas/audit-report.schema.json` et
`schemas/remediation-manifest.schema.json` — valider avec
`scripts/validate_report.py` / `scripts/validate_manifest.py` avant de
livrer.

## Structure de `ANTI_CHURN_AUDIT.md`

```markdown
# Audit anti-churn — <repo>

Date :
SHA :
Stack :
Architecture :
Type d'usage :
Modèle de compte :
Providers :
Analytics :
Data coverage :
Conclusion globale :

## Résumé exécutif
## Top 3 quick wins
## Provider matrix
## Résultats Tibo

| ID | Point | Statut | Sévérité | Preuve | Automatisation |
|----|-------|--------|----------|--------|----------------|

## Signaux de risque

| ID | Signal | Disponible | Seuil/config | Niveau de preuve |
|----|--------|------------|--------------|------------------|

## Signaux lagging
## Data readiness
## Réglages externes à vérifier
## Actions automatisables
## Actions nécessitant validation
## Actions manuelles
## Hors périmètre / stratégie humaine
## Non-regrettable churn
## Plan P0
## Plan P1
## Plan P2
## Limites et niveau de confiance
## Sources
```

Se termine toujours par une invite d'action concrète, jamais une promesse
vague :

```
Pour appliquer un correctif :
/anti-churn-audit fix <finding-id>
```

## Champs d'un finding

Chaque finding (Markdown et JSON) doit contenir :

`finding_id`, `title`, `why_it_matters`, `evidence`, `status`, `severity`,
`confidence`, `automation`, `prerequisites`, `proposed_files`,
`external_steps`, `tests_required`, `rollback`, `expected_result`,
`success_metric`, `owner`, `estimated_effort`, `dependencies`,
`blocking_reason`.

Voir `templates/AUDIT_REPORT.md`, `templates/REMEDIATION_PLAN.md`, et
`templates/EXTERNAL_CHECKLIST.md` pour les gabarits prêts à remplir.
