# Expected — bad-fit

- Signal fort de "bad fit" produit : volumétrie du client largement hors
  cible, tickets support répétés uniquement liés aux limites de plan, pas
  de bug produit sous-jacent.
- Le rapport ne doit **jamais** recommander automatiquement une action de
  rétention (discount, upgrade forcé, exception de plan) pour ce compte.
- Finding correspondant marqué `status=STRATEGY_REQUIRED`,
  `automation=STRATEGY_HUMAN`.
- Le rapport doit mentionner explicitement le concept de
  **non-regrettable churn** : ce client ne correspond pas au produit, et
  le retenir pourrait coûter plus cher (support, risque de churn négatif
  amplifié) que de le laisser partir.
- Proposer des questions d'interview plutôt qu'une conclusion définitive
  (ex : "existe-t-il un plan enterprise adapté à ce volume ?").
