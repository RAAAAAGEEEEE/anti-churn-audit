# anti-churn-audit

Skill Claude qui audite statiquement un repo SaaS pour repérer les
mécanismes anti-churn réellement branchés dans le code — et distingue
honnêtement ce qui est vérifiable du code de ce qui dépend de données, de
réglages de dashboard, ou d'une décision humaine.

## Problème résolu

La plupart des audits « anti-churn » mélangent trois choses différentes :
ce qui existe dans le code, ce qui marche en pratique (données requises),
et ce qui relève d'un choix stratégique (discount, pricing, bad-fit). Ce
skill les sépare explicitement à chaque étape, avec un niveau de preuve
tracé (pas un simple grep) pour chaque affirmation.

## Périmètre honnête

- **Fait** : audit statique du code, détection de providers de paiement,
  traçage de preuve (import → config → handler → persistance → action →
  test), scoring heuristique déterministe avec couverture de données
  explicite.
- **Ne fait pas** : prédiction ML calibrée, garantie de récupération de
  revenu, modification automatique d'un dashboard externe, contact
  automatique de clients.
- **Read-only par défaut** — seul le mode `fix`, avec confirmation
  explicite, peut modifier du code.

## Quick start

Installation projet (dans un repo à auditer) :

```
mkdir -p .claude/skills
cp -r /chemin/vers/anti-churn-audit .claude/skills/anti-churn-audit
```

Installation utilisateur (disponible dans tous vos projets) :

```
cp -r /chemin/vers/anti-churn-audit ~/.claude/skills/anti-churn-audit
```

Puis, dans une session Claude Code sur le repo à auditer :

```
/anti-churn-audit audit
```

## Modes

| Mode | Commande | Effet |
|---|---|---|
| Audit (défaut) | `/anti-churn-audit audit` | Lecture seule, produit les rapports |
| Plan | `/anti-churn-audit plan <finding-id>` | Plan précis, aucune modification |
| Fix | `/anti-churn-audit fix <finding-id>` | Modifie le code après confirmation |
| Verify | `/anti-churn-audit verify <finding-id|all>` | Vérifie les corrections appliquées |

## Exemple de sortie

```
<output-dir>/
├── ANTI_CHURN_AUDIT.md        # rapport lisible par un non-codeur
├── anti-churn-audit.json      # données structurées (schema validé)
├── REMEDIATION_PLAN.md
├── remediation-manifest.json  # source de vérité pour l'automatisation
├── EXTERNAL_CHECKLIST.md      # réglages dashboard à vérifier manuellement
└── evidence/evidence-index.json
```

## Providers supportés

Stripe, Paddle, Lemon Squeezy, Chargebee, RevenueCat, Apple App Store /
Google Play, PayPal/Braintree — voir `docs/PROVIDER_MATRIX.md`. Support
non exhaustif : chaque provider est audité séparément, jamais fusionné en
un statut global.

## Politique de confidentialité

Aucune donnée du repo audité n'est envoyée à un service tiers par ce
skill. Tous les artefacts restent locaux dans le dossier de sortie choisi.
Voir `docs/SECURITY.md`.

## Scoring heuristique — limites

Le `risk_score` est un score heuristique déterministe (moteur interne
`risk-engine`), pas une prédiction ML calibrée. Il est accompagné d'un
`data_coverage` : en dessous de 50% de couverture, le score n'est pas
affiché comme définitif (`INSUFFICIENT_DATA`). Voir
`docs/SCORING_MODEL.md`.

## Statut clean-room

Ce projet est une **réimplémentation originale inspirée par les travaux
publics existants** (notamment ChurnGuard AI), pas un fork. Aucun code,
prompt, ou contenu de notebook tiers n'a été repris — voir
`docs/LEGAL_AND_ATTRIBUTION.md` pour la justification complète et
`docs/UPSTREAM_WATCH.md` pour la procédure de revérification.

## Roadmap

- **P0** (ce dépôt) : pipeline complet, provider matrix, preuves L0-L4,
  scoring déterministe, schémas JSON validés, evals.
- **P1** : GRR/NRR account-level, distinction volontaire/involontaire,
  seat utilization, outcomes d'intervention, signaux support, cohortes,
  multi-currency.
- **P2** : calibration statistique des poids, modèle ML (avec validation
  temporelle), explications type SHAP, moteur de retry custom uniquement
  si un provider natif s'avère insuffisant.

## Contribution

Issues et PR bienvenues. Toute proposition touchant à l'attribution ou à
la posture légale (`docs/LEGAL_AND_ATTRIBUTION.md`) doit être discutée
avant merge.

## Licence

MIT — voir `LICENSE`. Ne couvre que le code original de ce dépôt, pas les
travaux tiers cités en inspiration.
