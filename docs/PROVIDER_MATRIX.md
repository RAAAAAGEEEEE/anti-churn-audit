# Provider Matrix

## Modèle à deux axes

- `commercial_model` : `merchant_of_record` | `merchant_direct` | `app_store` | `unknown`
- `recovery_owner` : `provider` | `application` | `hybrid` | `unknown`

## Matrice initiale

| Provider | commercial_model | recovery_owner |
|---|---|---|
| Paddle | merchant_of_record | provider/hybrid |
| Lemon Squeezy | merchant_of_record | provider/hybrid |
| Stripe direct | merchant_direct | provider/hybrid selon Stripe Billing |
| Stripe Managed Payments | merchant_of_record | provider/hybrid |
| Chargebee | merchant_direct par défaut (MoR seulement si Reach ou équivalent confirmé) | provider/hybrid |
| RevenueCat | dépend du store/provider sous-jacent (orchestration) | dépend du store/provider |
| Apple App Store / Google Play | app_store | provider/hybrid |
| PayPal / Braintree | merchant_direct | selon intégration |

Cette matrice documente des événements représentatifs, **sans prétendre à
l'exhaustivité** — toujours vérifier la documentation officielle du provider
avant de conclure.

## Événements représentatifs par provider

**Stripe**
- `invoice.payment_failed`
- `invoice.paid`
- `customer.subscription.updated`
- `customer.subscription.deleted`

**Paddle**
- `subscription.past_due`
- `subscription.canceled`
- `subscription.updated`
- `transaction.completed`
- `transaction.payment_failed`

**Lemon Squeezy**
- `subscription_payment_failed`
- `subscription_payment_recovered`
- `subscription_payment_success`
- `subscription_updated`
- `subscription_cancelled`
- `subscription_expired`

**RevenueCat**
- `BILLING_ISSUE`
- `CANCELLATION`
- `EXPIRATION`
- `RENEWAL`
- `UNCANCELLATION`
- `PRODUCT_CHANGE`

## Checklist par provider

Pour chaque provider détecté, auditer :

- signature webhook vérifiée ;
- corps brut (raw body) utilisé si requis pour la vérification de signature ;
- `event_id`/déduplication (idempotence) ;
- traitement asynchrone du webhook ;
- gestion du retry de livraison webhook par le provider ;
- absence d'hypothèse sur l'ordre garanti des événements ;
- restauration des droits après récupération d'un paiement ;
- journalisation des événements traités ;
- tests couvrant ces mécanismes.

## Règles de déclenchement conditionnel (voir aussi `references/audit-patterns.md`)

- **Stripe direct** : vérifier les webhooks dans le code, créer une
  checklist manuelle pour Smart Retries (réglage dashboard, pas de code),
  privilégier les mécanismes natifs Stripe. Un moteur de retry custom ne
  doit être proposé qu'en `P2`, avec un besoin démontré.
- **Paddle / Lemon Squeezy** : ne jamais signaler l'absence de retry custom
  comme un manque — ces providers gèrent nativement les retries (MoR).
  Auditer les événements de statut et la synchronisation des droits.
- **Chargebee** : ne jamais classer automatiquement `merchant_of_record` —
  déterminer explicitement le gateway et le propriétaire du recovery.
- **Multi-provider** : produire une sous-section par provider, relever les
  divergences d'état, vérifier la normalisation des statuts entre
  providers avant tout score global.
