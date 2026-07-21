# Legal & Attribution

## Statut

Ce dépôt contient une **réimplémentation originale inspirée par les travaux
publics existants**. Il ne s'agit ni d'un fork, ni d'une traduction, ni d'une
paraphrase de quelque dépôt tiers que ce soit. N'utilisez jamais l'expression
« fork de ChurnGuard » pour décrire ce projet.

## Projet cité : ChurnGuard AI

- Auteur : Shreyas Dasari
- URL : https://github.com/ShreyasDasari/churnguard-ai
- SHA vérifié : `2958000bb8fff4f330d3dd7e11fde9ecf24e26d3`
- Date de vérification (ISO) : 2026-07-21

### État de licence constaté à la vérification

- Le README du dépôt déclare une licence MIT.
- Aucun fichier `LICENSE` n'était présent dans l'arborescence observée au SHA
  ci-dessus.
- L'API GitHub renvoyait `license: null` pour ce dépôt.
- Le code se trouve majoritairement dans un notebook (`churnguard_ai.ipynb`),
  sans package publié ni suite de tests établie.

**Une déclaration de licence dans un README, sans fichier `LICENSE` présent
dans le dépôt, ne constitue pas une licence opposable.** Par prudence, ce
projet traite ChurnGuard AI comme non réutilisable en l'état.

### Décision clean-room

ChurnGuard AI a inspiré l'exploration du **problème** (scoring de churn pour
SaaS, signaux comportementaux, importance de la donnée de paiement) mais
**aucun code n'a été repris**, en raison de l'absence de fichier `LICENSE`
lors de la vérification ci-dessus. Concrètement, n'ont jamais été copiés,
traduits ou paraphrasés :

- les cellules du notebook ;
- les fonctions, classes ou noms de variables ;
- les commentaires ;
- les prompts éventuels ;
- les données synthétiques ;
- les formulations du README ;
- la structure interne distinctive du projet.

Ce dépôt (`anti-churn-audit`) a été construit uniquement à partir de :

- fonctionnalités **publiquement décrites** dans le README de ChurnGuard AI
  (niveau concept, pas niveau implémentation) ;
- concepts généraux de churn scoring, non protégeables en tant que tels
  (signaux d'usage, paiements échoués, adoption de fonctionnalités, etc.) ;
- la documentation officielle des providers de paiement (Stripe, Paddle,
  Lemon Squeezy, Chargebee, RevenueCat, Apple, Google) ;
- des architectures, formules de scoring, schémas de données, prompts et
  tests conçus spécifiquement pour ce projet.

Le moteur de scoring de ce dépôt est nommé en interne **`risk-engine`** afin
d'éviter toute ambiguïté de nommage avec le projet cité.

### Attribution

Nous remercions Shreyas Dasari pour avoir publié ChurnGuard AI, qui a
contribué à motiver l'exploration de ce sujet. Cette attribution est un
geste de courtoisie et de transparence ; elle ne constitue pas une licence,
et ne doit pas être interprétée comme une autorisation d'usage du code
d'origine.

## Procédure si l'auteur ajoute une licence compatible

Si, à l'avenir :

1. l'auteur ajoute un fichier `LICENSE` compatible avec MIT (MIT, Apache-2.0,
   BSD, etc.), **ou**
2. l'auteur donne une autorisation écrite explicite,

alors une **réévaluation** peut être envisagée pour :

- transformer une partie de ce projet en véritable fork ou intégration
  upstream ;
- citer plus précisément les portions de code éventuellement réutilisées ;
- mettre à jour ce document avec la nouvelle base légale.

Cette réévaluation n'est jamais automatique. Voir `docs/UPSTREAM_WATCH.md`
pour la procédure de revérification. Toute décision d'intégration upstream
nécessite un accord explicite du mainteneur de ce dépôt — ne pas contacter
l'auteur de ChurnGuard AI ni ouvrir d'issue sans cet accord.

## Autres attributions

Voir `SOURCES.md` pour les benchmarks et statistiques citées (Stripe, Paddle,
Lemon Squeezy, Recurly, Amplitude, Slack), avec leur niveau de confiance.
