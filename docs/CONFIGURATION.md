# Configuration

Voir aussi : [SCORING_MODEL.md](SCORING_MODEL.md),
[PROVIDER_MATRIX.md](PROVIDER_MATRIX.md), [USAGE.md](USAGE.md).

Le skill n'a pas de fichier de configuration et ne lit aucune variable
d'environnement. Il n'y a donc pas de `.env.example`.

## Ce qui est ajustable

| Quoi | Où | Remarque |
|---|---|---|
| Dossier de sortie | Demandé au début d'un audit | Seul endroit où le mode audit écrit |
| Poids des signaux (S1 à S8) | `docs/SCORING_MODEL.md`, `references/scoring.md` | Valeurs par défaut heuristiques, à recalibrer par produit |
| Paliers de risque | Mêmes fichiers | Par défaut LOW 0-29, MEDIUM 30-49, HIGH 50-69, CRITICAL 70-100 |
| Contexte produit | Répondu en phase 2 | Fréquence d'usage, modèle de compte, core action, outcome event |
| Traitement par provider | `docs/PROVIDER_MATRIX.md` | Chaque provider est audité séparément |

Pour garder un profil de poids propre à un produit, renseignez son nom dans
`scoring.weights_profile` du rapport et documentez les valeurs à côté de votre
sortie d'audit. Ne modifiez pas les valeurs par défaut sur place si vous
comptez récupérer les mises à jour.
