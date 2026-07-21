# Expected — periodic-product

- `product_context.usage_type = "periodic"` détecté via
  `product_config.json`.
- Le seuil générique `+14 jours sans connexion` (S2) ne doit **pas** être
  appliqué tel quel à ce produit.
- À la place, prioriser : cadence attendue (annuelle ici), proximité de
  `next_filing_deadline` (renouvellement), `filing_accepted` (outcome), et
  le statut de paiement.
- Si ce contexte n'était pas fourni explicitement, le skill devrait le
  demander avant de conclure sur S2 — voir Phase 2 et règle H.
