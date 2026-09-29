# anti-churn-audit

Skill Claude qui audite statiquement un repo SaaS pour repérer les
mécanismes anti-churn réellement branchés dans le code, et distingue
honnêtement ce qui est vérifiable du code de ce qui dépend de données, de
réglages de dashboard ou d'une décision humaine.

## Problème résolu

La plupart des audits « anti-churn » mélangent trois choses différentes : ce
qui existe dans le code, ce qui marche en pratique (données requises) et ce
qui relève d'un choix stratégique (remise, pricing, client mal adapté). Ce
skill les sépare à chaque étape, avec un niveau de preuve tracé (pas un simple
grep) pour chaque affirmation.

## Pour qui

Fondateurs et petites équipes SaaS qui utilisent Claude Code et veulent savoir,
avant de dépenser en acquisition, si le code gère bien les paiements échoués,
les webhooks, l'annulation et le win-back.

## Statut

**Alpha, v0.1.1.** Le pipeline, les schémas JSON et les deux validateurs
existent et les validateurs ont été exécutés sur l'exemple fourni. Les 12
scénarios d'éval sont des fixtures à comparer à la main : aucun harnais
automatique ne les exécute encore. Lire [docs/LIMITATIONS.md](docs/LIMITATIONS.md).

## Prérequis

- Claude Code, avec les skills chargés depuis `.claude/skills/`.
- Python 3.8+ (bibliothèque standard) pour les validateurs uniquement.
- Le dépôt à auditer en local.

## Démarrage rapide

```bash
git clone https://github.com/RAAAAAGEEEEE/anti-churn-audit ~/.claude/skills/anti-churn-audit
```

Puis, dans une session Claude Code ouverte sur le repo à auditer :

```
/anti-churn-audit audit
```

Installation par projet et Windows : [docs/INSTALLATION.md](docs/INSTALLATION.md).

## Exemple minimal

Valider l'exemple fourni :

```bash
python3 scripts/validate_report.py examples/stripe-incomplete/anti-churn-audit.json
python3 scripts/validate_manifest.py examples/stripe-incomplete/remediation-manifest.json
```

Sortie attendue : deux lignes `[OK]`. Finding principal de cet exemple
illustratif (pas un audit réel) :

```
F-001  T3  invoice.payment_failed sans handler
       status=ABSENT  severity=P0  automation=AUTO_WITH_APPROVAL  preuve L2
```

## Modes

| Mode | Commande | Effet |
|---|---|---|
| Audit (défaut) | `/anti-churn-audit audit` | Lecture seule, produit les rapports |
| Plan | `/anti-churn-audit plan <finding-id>` | Plan précis, aucune modification |
| Fix | `/anti-churn-audit fix <finding-id>` | Modifie le code après confirmation |
| Verify | `/anti-churn-audit verify <finding-id\|all>` | Vérifie les corrections appliquées |

Sortie d'un audit : `ANTI_CHURN_AUDIT.md`, `anti-churn-audit.json`,
`REMEDIATION_PLAN.md`, `remediation-manifest.json`, `EXTERNAL_CHECKLIST.md`,
`evidence/evidence-index.json`. Détail dans [docs/USAGE.md](docs/USAGE.md).

## Architecture

Un skill Claude, sans serveur ni base de données : un pipeline en phases
0 à 14 lit le repo, trace des preuves (niveaux L0 à L4), classe chaque finding
(statut, sévérité, confiance, automatisation), calcule un score heuristique
`risk-engine` avec sa couverture de données, puis écrit le rapport. Voir
[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Configuration

Aucun fichier de configuration ni variable d'environnement. Poids et paliers
du score : [docs/CONFIGURATION.md](docs/CONFIGURATION.md).

## Providers supportés

Stripe, Paddle, Lemon Squeezy, Chargebee, RevenueCat, Apple App Store /
Google Play, PayPal/Braintree. Support non exhaustif, chaque provider est
audité séparément : [docs/PROVIDER_MATRIX.md](docs/PROVIDER_MATRIX.md).

## Sécurité et confidentialité

Lecture seule par défaut, aucun appel réseau, aucune donnée envoyée à un
tiers, secrets jamais reproduits dans les rapports. Voir
[docs/PRIVACY_AND_SECURITY.md](docs/PRIVACY_AND_SECURITY.md) et
[SECURITY.md](SECURITY.md).

## Limites

- Analyse statique : aucune donnée de production, aucun dashboard.
- `risk_score` heuristique, pas une prédiction calibrée ; non définitif sous
  0,50 de couverture de données.
- Aucune récupération de revenu garantie.
- Les points stratégiques ne sont jamais tranchés automatiquement.

Liste complète : [docs/LIMITATIONS.md](docs/LIMITATIONS.md).

## Statut clean-room

Réimplémentation originale inspirée par des travaux publics (notamment
ChurnGuard AI), pas un fork. Aucun code, prompt ou contenu de notebook tiers
n'a été repris : [docs/LEGAL_AND_ATTRIBUTION.md](docs/LEGAL_AND_ATTRIBUTION.md).

## Feuille de route (non contractuelle)

- P1 : GRR/NRR au niveau compte, distinction churn volontaire/involontaire,
  utilisation des sièges, résultats d'interventions, signaux support,
  cohortes, multi-devises.
- P2 : calibration statistique des poids, modèle ML avec validation
  temporelle, explications de type SHAP.

## Contribuer

Issues et pull requests bienvenues : [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

MIT, voir [LICENSE](LICENSE). Ne couvre que le code original de ce dépôt, pas
les travaux tiers cités en inspiration. Auteur : Anto1nx.

## Documentation détaillée

- [Installation](docs/INSTALLATION.md)
- [Utilisation](docs/USAGE.md)
- [Configuration](docs/CONFIGURATION.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Déroulé des phases](docs/EXECUTION_FLOW.md)
- [Format des rapports](docs/REPORT_FORMAT.md)
- [Modèle de statuts](docs/STATUS_MODEL.md)
- [Modèle de scoring](docs/SCORING_MODEL.md)
- [Matrice des providers](docs/PROVIDER_MATRIX.md)
- [Dépannage](docs/TROUBLESHOOTING.md)
- [Limites](docs/LIMITATIONS.md)
- [Confidentialité et sécurité](docs/PRIVACY_AND_SECURITY.md)
- [Mentions légales et attributions](docs/LEGAL_AND_ATTRIBUTION.md)
- [Veille amont](docs/UPSTREAM_WATCH.md)
- [Sources et benchmarks](SOURCES.md)
- [Changelog](CHANGELOG.md)
