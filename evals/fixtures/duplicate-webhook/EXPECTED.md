# Expected — duplicate-webhook

- Aucun identifiant d'événement (`event_id` ou équivalent) n'est extrait
  ni vérifié avant traitement dans `webhook.py`.
- Si Lemon Squeezy livre deux fois le même événement (comportement
  documenté des webhooks — livraison "at least once"), le handler
  applique l'action deux fois sans le détecter.
- Finding attendu : contrôle event_id/idempotence marqué `ABSENT`,
  `severity=P1` ou `P0` selon l'impact (ici `restore_entitlements` appelé
  deux fois est sans risque, mais `mark_past_due` en double peut fausser
  des métriques ou déclencher des relances en double si couplé à un
  système d'emailing).
- `automation=AUTO_WITH_APPROVAL` (ajout d'une table/contrôle
  d'idempotence = modification de code).
