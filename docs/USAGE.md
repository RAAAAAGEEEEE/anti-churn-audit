# Utilisation

Voir aussi : [INSTALLATION.md](INSTALLATION.md),
[REPORT_FORMAT.md](REPORT_FORMAT.md), [EXECUTION_FLOW.md](EXECUTION_FLOW.md),
[STATUS_MODEL.md](STATUS_MODEL.md).

## Modes

| Mode | Commande | Écrit dans le repo audité |
|---|---|---|
| Audit (défaut) | `/anti-churn-audit audit` | Non, uniquement dans le dossier de sortie validé |
| Plan | `/anti-churn-audit plan F-001` | Non |
| Fix | `/anti-churn-audit fix F-001` | Oui, après confirmation explicite de ce finding |
| Verify | `/anti-churn-audit verify all` | Met à jour le rapport existant seulement |

L'ordre est audit, puis plan, puis fix, puis verify. `fix` exige un finding
produit par un audit précédent et refuse les findings dont `automation` vaut
`MANUAL_EXTERNAL` ou `STRATEGY_HUMAN`.

## Session type

```
/anti-churn-audit audit
```

Le skill déroule les phases 0 à 12 ([EXECUTION_FLOW.md](EXECUTION_FLOW.md)),
demande un dossier de sortie, et écrit les six artefacts listés dans
[REPORT_FORMAT.md](REPORT_FORMAT.md). Valider ensuite les JSON :

```bash
python3 scripts/validate_report.py <output-dir>/anti-churn-audit.json
python3 scripts/validate_manifest.py <output-dir>/remediation-manifest.json
```

Les deux affichent `[OK]` en cas de succès et sortent avec un code non nul en
cas d'échec.

## Entrées et sorties

- Entrée : le dépôt du répertoire courant, plus quelques réponses quand le
  code ne suffit pas (fréquence d'usage, comptes B2B ou B2C, core action).
- Sortie : `ANTI_CHURN_AUDIT.md`, `anti-churn-audit.json`,
  `REMEDIATION_PLAN.md`, `remediation-manifest.json`,
  `EXTERNAL_CHECKLIST.md`, `evidence/evidence-index.json`.

## Exemple de sortie

Une paire de JSON illustrative (pas un audit réel enregistré) construite à
partir du fixture d'éval `stripe-incomplete` se trouve dans
[`examples/stripe-incomplete/`](../examples/stripe-incomplete/). Son finding
principal :

```
F-001  T3  invoice.payment_failed sans handler
       status=ABSENT  severity=P0  confidence=HIGH  automation=AUTO_WITH_APPROVAL
       preuve L2  webhook.js:23-25
scoring : risk_score non affiché (data_coverage 0.10 < 0.50, INSUFFICIENT_DATA)
```

## Scénarios d'évaluation

`evals/evals.json` liste 12 scénarios, chacun pointant vers un fixture
synthétique sous `evals/fixtures/<id>/` avec un `EXPECTED.md`. On les vérifie
en comparant la sortie d'un audit aux attentes, ou avec un futur harnais noté
par un modèle. Ce ne sont pas des tests unitaires exécutables : le pipeline
est exécuté par le modèle, pas par du code déterministe.
