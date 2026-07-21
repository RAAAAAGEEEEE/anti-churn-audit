# Upstream Watch — ChurnGuard AI

Procédure pour revérifier périodiquement l'état légal de
[ChurnGuard AI](https://github.com/ShreyasDasari/churnguard-ai) et décider si
une intégration upstream devient envisageable. Voir
`docs/LEGAL_AND_ATTRIBUTION.md` pour le contexte complet.

## Dernière vérification

- Date ISO : 2026-07-21
- SHA vérifié : `2958000bb8fff4f330d3dd7e11fde9ecf24e26d3`
- LICENSE présent : non
- Licence déclarée dans le README : MIT (non opposable sans fichier LICENSE)
- Décision : clean-room, aucune réutilisation de code

## Ce qu'il faut revérifier à chaque passage

1. **Présence d'un fichier `LICENSE`** à la racine du dépôt.
   ```
   curl -s https://api.github.com/repos/ShreyasDasari/churnguard-ai/contents/LICENSE
   ```
   Un code 200 indique la présence du fichier ; un code 404 indique son
   absence.

2. **Type de licence** via l'API GitHub :
   ```
   curl -s https://api.github.com/repos/ShreyasDasari/churnguard-ai | grep -A3 '"license"'
   ```
   Vérifier que le champ `license` n'est plus `null` et que la clé `spdx_id`
   correspond à une licence permissive compatible (MIT, Apache-2.0, BSD-2/3).

3. **Nouveau SHA courant** :
   ```
   curl -s https://api.github.com/repos/ShreyasDasari/churnguard-ai/commits/main
   ```
   Consigner le nouveau SHA et la date de vérification.

4. **Historique de commits** depuis le dernier SHA vérifié, pour repérer un
   commit d'ajout de licence ou un changement de mainteneur.

5. **Compatibilité avec notre licence MIT** : si une licence est ajoutée,
   vérifier qu'elle autorise la redistribution et la modification sans
   condition incompatible avec MIT (copyleft fort type GPL serait
   incompatible avec une intégration directe de code sous notre licence
   actuelle).

## Règles pendant la revérification

- Ne pas contacter l'auteur.
- Ne pas ouvrir d'issue ou de pull request sur le dépôt upstream.
- Ne pas cloner ni lire le notebook dans le but d'en extraire du code —
  seule la présence/absence de `LICENSE` et les métadonnées publiques
  (API GitHub) sont à consulter.
- Toute décision de changer de posture (clean-room → fork/intégration)
  nécessite l'accord explicite du mainteneur de ce dépôt avant toute action.

## Journal des vérifications

| Date       | SHA vérifié                               | LICENSE présent | Décision                |
|------------|--------------------------------------------|------------------|--------------------------|
| 2026-07-21 | 2958000bb8fff4f330d3dd7e11fde9ecf24e26d3   | Non              | Clean-room, pas de reuse |
