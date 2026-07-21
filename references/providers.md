# Providers — détails de détection

Ce fichier complète `docs/PROVIDER_MATRIX.md` avec des heuristiques de
détection statique (noms de packages, variables d'environnement typiques,
routes de webhook courantes). Ces heuristiques servent à orienter la
recherche, pas à conclure automatiquement — toujours vérifier la chaîne
complète (voir `docs/EXECUTION_FLOW.md#phase-4-evidence-tracing`).

## Stripe

- Packages : `stripe`, `@stripe/stripe-js`, `stripe-python`, `stripe-ruby`.
- Variables d'environnement typiques : `STRIPE_SECRET_KEY`,
  `STRIPE_WEBHOOK_SECRET`.
- Route de webhook typique : `/api/webhooks/stripe`, `/webhooks/stripe`.
- Vérification de signature : `stripe.webhooks.constructEvent` (Node),
  `stripe.Webhook.construct_event` (Python).
- Points d'attention : utilisation du corps brut (raw body) avant tout
  parsing JSON, sinon la vérification de signature échoue silencieusement
  ou est contournée.

## Paddle

- Packages : `@paddle/paddle-node-sdk`, `paddle-billing`.
- Variables typiques : `PADDLE_API_KEY`, `PADDLE_WEBHOOK_SECRET`.
- Modèle : merchant of record — les retries de paiement sont natifs.

### Paddle Billing vs Paddle Classic — ne pas confondre

Paddle a deux générations d'API/webhooks incompatibles entre elles. Les
confondre fausse le format de signature attendu et la checklist externe à
produire.

| Signal observable dans le code | Paddle Billing (actuel) | Paddle Classic (legacy) |
|---|---|---|
| Noms d'événements | à points, ex. `subscription.past_due`, `transaction.completed` (namespace `transaction.*` inexistant côté Classic) | underscore, ex. `subscription_payment_failed`, `subscription_cancelled` (double L, orthographe britannique) |
| Format du corps webhook | JSON | form-encoded (paramètres `p_*` sérialisés PHP) |
| Vérification de signature | HMAC sur le corps brut, en-tête `Paddle-Signature` | signature RSA `p_signature` sur les données triées et sérialisées PHP |
| API/SDK | `@paddle/paddle-node-sdk`, endpoints `api.paddle.com` | endpoints `vendors.paddle.com`, SDKs legacy |

**Règle** : si le code présente des noms d'événements à points et un corps
JSON, classer `paddle_version=billing` avec confidence `MEDIUM` (déduction
par convention de nommage, pas une confirmation directe) et le documenter
comme tel dans les preuves. Si les signaux sont mixtes ou absents (aucun
event_type identifiable, pas de corps clair), **ne pas deviner** — marquer
la version `CONTEXT_REQUIRED` plutôt que de supposer Billing par défaut,
et signaler explicitement l'ambiguïté dans les limites du rapport.

## Lemon Squeezy

- Packages : `@lemonsqueezy/lemonsqueezy.js`.
- Variables typiques : `LEMONSQUEEZY_API_KEY`, `LEMONSQUEEZY_WEBHOOK_SECRET`.
- Modèle : merchant of record — 4 retries natifs sur deux semaines
  (voir `SOURCES.md`, confidence HIGH).

## Chargebee

- Packages : `chargebee`.
- Variables typiques : `CHARGEBEE_SITE`, `CHARGEBEE_API_KEY`.
- Ne jamais supposer MoR par défaut — vérifier si Chargebee Reach (ou
  équivalent) est explicitement configuré.

## RevenueCat

- Packages : `react-native-purchases`, `purchases-ios`, `purchases-android`,
  `@revenuecat/purchases-js`.
- Orchestration au-dessus de l'App Store / Google Play / Stripe — le
  `commercial_model` réel dépend du store sous-jacent.

## Apple App Store / Google Play

- Détection : présence de configuration StoreKit / Billing Library,
  fichiers `app.json`/`eas.json` avec IAP, `google-services.json`.
- `recovery_owner` : provider/hybrid — les réglages de grace period et de
  relance sont gérés côté store, rarement dans le code applicatif.

## PayPal / Braintree

- Packages : `braintree`, `@paypal/checkout-server-sdk`.
- `recovery_owner` dépend fortement de l'intégration (Billing Agreements
  vs Subscriptions API) — vérifier au cas par cas.

## Règle multi-provider

Si plusieurs providers sont détectés dans le même repo, produire une
sous-section indépendante par provider dans le rapport (voir règle F,
`references/audit-patterns.md`). Ne jamais calculer un `risk_score` unique
qui mélangerait des statuts de providers non normalisés entre eux sans
documenter cette normalisation.
