# Audit Patterns — règles de déclenchement conditionnel (Phase 9)

Après l'audit statique (phases 0-8), déclencher **uniquement** les modules
applicables aux résultats obtenus. Ne jamais exécuter systématiquement tous
les modules.

## A — Aucun analytics / core event détecté

- Ne pas générer de health score SQL.
- Déclencher un plan d'instrumentation (P0/P1 selon contexte produit).
- Marquer le scoring comportemental `DATA_REQUIRED`.

## B — Comptes B2B mais tracking user-only

- Déclencher un plan account-level (mapping user → account).
- Ne pas calculer de seat/adoption account-level comme fiable tant que ce
  mapping n'existe pas.

## C — Stripe direct détecté

- Vérifier les webhooks dans le code.
- Créer une checklist Smart Retries pour le dashboard (réglage externe,
  jamais du code).
- Privilégier les mécanismes natifs Stripe.
- Ne proposer un moteur de retry custom qu'en `P2`, avec besoin démontré.

## D — Paddle / Lemon Squeezy détecté

- Ne pas signaler l'absence de retry custom comme un manque (MoR gère
  nativement les retries).
- Auditer les événements de statut (`subscription.past_due`,
  `subscription_payment_failed`, etc.).
- Auditer la synchronisation des droits produit.
- Auditer la restauration après récupération de paiement.

## E — Chargebee détecté

- Ne jamais classer automatiquement `merchant_of_record`.
- Déterminer explicitement le gateway et le propriétaire du recovery.
- Vérifier le provider de dunning et les webhooks associés.

## F — Plusieurs providers détectés

- Produire une sous-section par provider.
- Relever les divergences d'état entre providers.
- Vérifier la normalisation des statuts avant tout score global.

## G — Produit < 14 jours ou compte cold-start

- Router vers l'onboarding plutôt que le silent churn.
- Ne pas produire d'alerte silent churn fiable pour ces comptes.

## H — Usage périodique / saisonnier

- Ne pas appliquer le seuil `+14 jours sans connexion`.
- Utiliser la cadence attendue, le renouvellement, l'outcome et le
  paiement comme signaux prioritaires.

## I — Signal lagging détecté

Si l'un de ces signaux est présent :

- paiement échoué répété ;
- demande d'annulation ;
- souscription annulée ;
- downgrade récent ;
- expiration imminente ;

alors recommander une **escalade immédiate**, pas un outreach standard.

## J — Cancel flow brut (sans capture de motif)

- Déclencher un plan pause/downgrade/motif.
- Ne jamais choisir automatiquement un discount.
- Recommander une expérimentation avec garde-fou bad-fit (ne pas retenir
  automatiquement un client qui ne devrait pas rester — voir
  « Non-regrettable churn » dans `docs/REPORT_FORMAT.md`).

## K — Win-back absent

- Proposer J+7 comme hypothèse initiale, pas comme règle universelle.
- Ne jamais présenter « 50% en 30 jours » comme vérité universelle (voir
  `SOURCES.md`, confidence LOW pour ce chiffre).
- Exiger la gestion de désinscription et la conformité email avant toute
  recommandation de campagne.
