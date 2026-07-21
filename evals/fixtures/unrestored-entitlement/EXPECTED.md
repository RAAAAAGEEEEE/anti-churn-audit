# Expected — unrestored-entitlement

- `invoice.payment_failed` → `markPastDue` + `restrictAccess` (l'accès est
  restreint).
- `invoice.paid` (paiement récupéré) → `clearPastDue` seulement.
  `restrictAccess` n'est **jamais annulé** — l'accès reste restreint même
  après un paiement réussi.
- Finding attendu : "droits non restaurés après récupération de paiement",
  `severity=P0` (un client qui paie mais reste bloqué va légitimement
  churner, et c'est un bug direct de revenu/expérience).
- `evidence_level` : L3 (chaîne tracée complètement — c'est justement en
  suivant la chaîne jusqu'au bout qu'on détecte l'absence de restauration,
  pas au simple grep sur "invoice.paid").
- `automation=AUTO_WITH_APPROVAL`.
