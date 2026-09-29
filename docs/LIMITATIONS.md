# Limites

Voir aussi : [SCORING_MODEL.md](SCORING_MODEL.md),
[STATUS_MODEL.md](STATUS_MODEL.md), [../SOURCES.md](../SOURCES.md).

- **Analyse statique uniquement.** Le skill lit du code. Il ne voit ni les
  données de production, ni un dashboard, ni un client.
- **Les réglages de dashboard sont inconnaissables depuis le code.** Smart
  Retries de Stripe, réglages de retry de Paddle et Lemon Squeezy, DNS et
  délivrabilité sont rapportés `EXTERNAL_UNKNOWN` avec une checklist manuelle,
  jamais comme absents.
- **`risk_score` est heuristique**, pas une prédiction calibrée. Sous 0,50 de
  couverture de données, il n'est pas présenté comme définitif. Ni ML, ni
  calibration, ni explication de type SHAP dans cette version.
- **Aucune garantie de récupération de revenu.** Un finding corrigé n'est pas
  un pourcentage de revenu récupéré.
- **Couverture des providers non exhaustive.** Voir
  [PROVIDER_MATRIX.md](PROVIDER_MATRIX.md).
- **Les points stratégiques (T1, T5, T6, T9, T12) ne sont jamais tranchés
  automatiquement.** Remises, pricing et gestion du bad-fit demandent une
  décision humaine.
- **Les evals ne sont pas des tests automatisés.** Ce sont des scénarios
  auxquels comparer un audit ; aucun harnais ne les exécute encore.
- **Les benchmarks sont du contexte, pas des règles.** Chaque chiffre porte un
  niveau de confiance dans [../SOURCES.md](../SOURCES.md).
- **Statut alpha.** Le pipeline et les schémas peuvent changer entre versions
  0.x.
