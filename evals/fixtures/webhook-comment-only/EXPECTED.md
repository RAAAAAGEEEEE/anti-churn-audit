# Expected — webhook-comment-only

- Les termes « vérifier la signature », « idempotence », « event_id »
  n'apparaissent que dans un commentaire `TODO`, jamais dans du code
  exécuté : `express.json()` parse le body sans vérification de
  signature, aucun contrôle `event_id` n'existe dans le handler.
- `evidence_level = L0` pour la vérification de signature et l'idempotence
  (terme trouvé, aucune implémentation réelle).
- **Le statut ne doit jamais être `VERIFIED`** pour ces deux mécanismes,
  même si les mots-clés attendus sont présents textuellement dans le
  fichier. Statut correct : `ABSENT` (le TODO documente une intention non
  réalisée).
- Finding `severity=P0` : un webhook non vérifié en signature est un
  risque de sécurité et de fiabilité (n'importe qui peut poster un faux
  event).
