# Remediation Rules

Règles d'automatisation détaillées pour la Phase 11 (Remediation Decision).
Voir `docs/STATUS_MODEL.md#catégories-dautomatisation` pour la liste des
catégories.

## AUTO_SAFE

- Génération de rapport (Markdown/JSON).
- Ajout de documentation.
- Génération de tests non destructifs (qui ne modifient pas de
  comportement existant, seulement ajoutent une couverture).
- Instrumentation sans PII, si validée par l'utilisateur au préalable.
- Validation JSON (schémas).
- Création de checklist externe.

Ces actions peuvent être exécutées sans confirmation supplémentaire au-delà
de celle déjà donnée pour lancer l'audit.

## AUTO_WITH_APPROVAL

- Modification de code applicatif.
- Nouvelle migration de base de données.
- Ajout/modification de webhook.
- Envoi d'email (template, séquence).
- Cron/job planifié.
- Changement de droits/entitlements.
- Changement du cancel flow.

**Aucune de ces actions ne doit être exécutée sans accord explicite de
l'utilisateur pour le `finding_id` précis concerné.** Le manifeste doit
porter `requires_explicit_approval: true` pour tout item de cette
catégorie.

## MANUAL_EXTERNAL

- Dashboards providers (Stripe, Paddle, Lemon Squeezy, Chargebee).
- DNS.
- Configuration email provider (SPF/DKIM/DMARC, listes de suppression).
- App Store Connect / Google Play Console.

Ces actions ne sont jamais automatisables par ce skill — produire une
checklist claire (`EXTERNAL_CHECKLIST.md`) avec les étapes exactes.

## STRATEGY_HUMAN

- Choix d'un discount ou d'une offre de rétention.
- Décision de retenir (ou non) un segment de clients.
- Définition de l'aha moment / de l'outcome produit.
- Qualification bad-fit (voir « Non-regrettable churn »).
- Choix du plan/pricing à recommander.

Ces décisions ne sont jamais prises par le skill — il propose des questions
d'interview et des hypothèses, jamais une conclusion définitive.

## Champs obligatoires par item (voir schema remediation-manifest)

`finding_id`, `title`, `why_it_matters`, `evidence`, `status`, `severity`,
`confidence`, `automation`, `prerequisites`, `proposed_files`,
`external_steps`, `tests_required`, `rollback`, `expected_result`,
`success_metric`, `owner`, `estimated_effort`, `dependencies`,
`blocking_reason`.
