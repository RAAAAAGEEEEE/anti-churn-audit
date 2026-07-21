# External Checklist — {{repo}}

Réglages qui ne peuvent **pas** être confirmés depuis le code et doivent
être vérifiés manuellement dans un dashboard tiers. Un item non trouvé
dans le code n'est pas forcément `ABSENT` — voir `docs/STATUS_MODEL.md`.

## Stripe

- [ ] Smart Retries activé (Dashboard → Paramètres → Facturation → Retries)
- [ ] Nombre de tentatives configuré (référence actuelle observée : jusqu'à
      8 essais sur deux semaines — voir `SOURCES.md`)
- [ ] Emails de relance Stripe activés ou relayés par l'application
- [ ] Webhook endpoint configuré avec la bonne URL et le bon secret

## Paddle

- [ ] Paramètres Paddle Retain configurés si utilisé
- [ ] Retries natifs confirmés (jusqu'à 7 sur 30 jours par défaut)
- [ ] Webhook endpoint configuré dans le dashboard Paddle

## Lemon Squeezy

- [ ] Webhook endpoint configuré
- [ ] Retries natifs confirmés (4 sur deux semaines par défaut)

## Chargebee

- [ ] Règles de dunning configurées
- [ ] Gateway et propriétaire du recovery identifiés (Chargebee vs
      gateway sous-jacent)
- [ ] Webhooks configurés

## Email / deliverability

- [ ] SPF/DKIM/DMARC configurés pour le domaine d'envoi
- [ ] Liste de suppression / désinscription conforme (win-back, relances)
- [ ] Réputation IP/domaine surveillée

## App Store / Google Play

- [ ] Grace period configurée (App Store Connect / Play Console)
- [ ] Renouvellement automatique et messages de relance natifs vérifiés

## Autres

- [ ] {{custom_external_item}}

---

Chaque case cochée doit être confirmée manuellement par un humain ayant
accès au dashboard concerné — ce skill ne peut pas les vérifier lui-même.
