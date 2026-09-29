# Dépannage

Voir aussi : [USAGE.md](USAGE.md), [INSTALLATION.md](INSTALLATION.md),
[STATUS_MODEL.md](STATUS_MODEL.md).

| Symptôme | Cause | Solution |
|---|---|---|
| `/anti-churn-audit` n'est pas proposé | Skill absent de `.claude/skills/` ou `~/.claude/skills/` | Vérifier que `SKILL.md` est directement dans le dossier `anti-churn-audit`, puis relancer la session |
| `python3: command not found` sous Windows | Seul `python` ou `py` est installé | Utiliser `python scripts/validate_report.py ...` ou `py scripts/validate_report.py ...` |
| Le validateur affiche `[FAIL] ...: file not found` | Mauvais chemin, ou l'audit n'a pas atteint la phase 12 | Passer le chemin exact de `anti-churn-audit.json` dans le dossier de sortie |
| Le validateur liste `missing required property` | Le rapport a omis un champ obligatoire | Relancer l'audit, ou `/anti-churn-audit verify all` |
| Le validateur liste `additional property ... not allowed` | Le rapport contient un champ inconnu du schéma | Le retirer, ou aligner le rapport sur `schemas/audit-report.schema.json` |
| `risk_score` est null | Couverture de données sous 0,50 (`INSUFFICIENT_DATA`) | Comportement attendu. Fournir le contexte produit et des données d'événements, ou lire les findings seuls |
| `fix` est refusé | Finding `MANUAL_EXTERNAL` ou `STRATEGY_HUMAN` | Comportement attendu. Suivre `EXTERNAL_CHECKLIST.md` ou prendre la décision soi-même |
| Un réglage de dashboard apparaît en `EXTERNAL_UNKNOWN` | Non versionné dans le dépôt | Le vérifier à la main avec les étapes de `EXTERNAL_CHECKLIST.md` |
