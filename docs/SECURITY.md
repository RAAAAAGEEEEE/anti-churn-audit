# Security

## Périmètre de l'audit

Le mode `audit` (par défaut) est **strictement lecture seule** sur le repo
audité. Aucune écriture n'a lieu en dehors du dossier de sortie
explicitement choisi par l'utilisateur.

Le mode `fix` peut modifier le repo, mais uniquement :

- après confirmation explicite de l'utilisateur pour un `finding_id`
  précis ;
- avec les fichiers ciblés affichés avant toute modification ;
- sans jamais toucher aux modifications non liées déjà présentes ;
- sans `reset`, `push`, ou déploiement automatique ;
- sans modification d'un dashboard externe (ce qui est par nature hors
  périmètre du code).

## Aucune donnée envoyée par défaut

Ce skill ne transmet aucune donnée du repo audité à un service tiers. Tous
les artefacts (rapports Markdown/JSON) restent locaux, dans le dossier de
sortie choisi par l'utilisateur.

## Secrets

- Ne jamais faire apparaître de clé API, token, mot de passe ou identifiant
  privé dans les rapports générés, même si trouvé dans le code audité —
  signaler leur présence par référence de fichier/ligne, sans reproduire
  la valeur.
- Les scripts (`scripts/validate_report.py`, `scripts/validate_manifest.py`)
  ne font aucun appel réseau et ne lisent aucune variable d'environnement
  sensible.
- Les fixtures d'évaluation (`evals/fixtures/`) ne contiennent que des
  données synthétiques, jamais de données de production réelles.

## Rapport d'une vulnérabilité

Ouvrir une issue sur ce dépôt en décrivant le problème sans détails
permettant une exploitation immédiate si la vulnérabilité est critique ;
pour un problème sensible, contacter le mainteneur en privé avant
publication.
