# Sources & Benchmarks

Chaque chiffre cité porte un niveau de confiance. Aucun de ces chiffres
n'est une règle universelle — ce sont des hypothèses de départ ou des
points de comparaison, à recalibrer par produit/cohorte.

## Légende

- **HIGH** : documentation officielle ou donnée primaire claire.
- **MEDIUM** : étude sérieuse mais contexte limité (secteur, taille
  d'échantillon, période).
- **LOW** : cas marketing, source secondaire, ou non reproductible.

## Benchmarks cités avec nuance

| Chiffre | Contexte réel | Confidence |
|---|---|---|
| ~3,8% de churn mensuel | Recurly, certaines catégories B2B analysées — pas généralisable à tout SaaS | MEDIUM |
| Forte attrition précoce mesurée comme activité | Amplitude — mesure de l'activité produit, pas nécessairement l'annulation payante B2B | MEDIUM |
| 2000 messages / ~93% de continuation | Cas Slack spécifique, un seul produit, un seul contexte d'usage | LOW |
| Smart Retries : ~8 essais sur deux semaines | Stripe, recommandation actuelle observée (dashboard, évolutif) | HIGH |
| Retries natifs jusqu'à 7 sur 30 jours | Paddle, documentation officielle | HIGH |
| 4 retries sur deux semaines | Lemon Squeezy, documentation officielle | HIGH |

## Chiffres marqués LOW ou retirés des règles automatiques

Les valeurs suivantes ne doivent **jamais** être utilisées comme preuve
définitive ou seuil universel dans un rapport généré par ce skill. Elles
peuvent servir d'hypothèses configurables, documentées comme telles :

- « 70% du churn dans les 90 jours »
- « -40% de sessions = 78% de précision prédictive »
- « <30% d'adoption = 80% de churn »
- « 50% des clients reviennent dans les 30 jours » (win-back universel)
- « 50/50 entre carte expirée et échecs de retries »
- « 70% d'usage mobile »
- « recovery 8-12 tentatives → 28-35% universel »
- « mensuel = exactement 2× annuel »
- « 3 tickets support / 30 jours = signal universel »

## Pourquoi cette distinction compte

Un rapport qui présente un chiffre LOW comme une vérité générale induit de
mauvaises décisions produit. Le skill doit toujours restituer le niveau de
confiance à côté de tout chiffre cité dans `ANTI_CHURN_AUDIT.md` (section
Sources) et ne jamais bâtir une règle de blocage (`BLOCKED`) sur un chiffre
LOW.
