# Contribuer

Issues et pull requests bienvenues.

## Avant d'ouvrir une pull request

1. Garder `SKILL.md` court. Le détail va dans `docs/` ou `references/`, et un
   sujet n'a qu'une seule source de vérité.
2. Mettre la documentation à jour dans le même commit que le comportement
   qu'elle décrit, et ajouter une ligne dans [CHANGELOG.md](CHANGELOG.md).
3. Toute commande documentée doit avoir été exécutée.
4. Lancer les validateurs sur l'exemple fourni :

   ```bash
   python3 scripts/validate_report.py examples/stripe-incomplete/anti-churn-audit.json
   python3 scripts/validate_manifest.py examples/stripe-incomplete/remediation-manifest.json
   ```

5. Un nouveau scénario d'éval va dans `evals/evals.json`, avec un fixture sous
   `evals/fixtures/<id>/` (code synthétique uniquement, un `EXPECTED.md` à
   côté).

## Sujets sensibles

Toute proposition qui touche à la posture clean-room
([docs/LEGAL_AND_ATTRIBUTION.md](docs/LEGAL_AND_ATTRIBUTION.md)) doit être
discutée dans une issue avant la pull request.

Ne jamais committer de données clients réelles, de clés ou de tokens, y
compris dans les fixtures.

## Licence

Toute contribution est publiée sous la licence MIT de ce dépôt.
