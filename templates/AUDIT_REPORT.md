# Audit anti-churn — {{repo}}

Date : {{date_iso}}
SHA : {{sha}}
Stack : {{stack}}
Architecture : {{architecture}}
Type d'usage : {{product_usage_type}}
Modèle de compte : {{account_model}}
Providers : {{providers_list}}
Analytics : {{analytics_summary}}
Data coverage : {{data_coverage}}
Conclusion globale : {{global_conclusion}}

## Résumé exécutif

{{executive_summary}}

## Top 3 quick wins

1. {{quick_win_1}}
2. {{quick_win_2}}
3. {{quick_win_3}}

## Provider matrix

| Provider | Modèle commercial | Propriétaire du recovery | Webhook signé | Idempotence | Restauration droits |
|---|---|---|---|---|---|
| {{provider}} | {{commercial_model}} | {{recovery_owner}} | {{webhook_signature_verified}} | {{idempotency_verified}} | {{entitlement_restore_verified}} |

## Résultats Tibo

| ID | Point | Statut | Sévérité | Preuve | Automatisation |
|----|-------|--------|----------|--------|----------------|
| {{finding_id}} | {{point_id}} — {{title}} | {{status}} | {{severity}} | {{evidence_level}} ({{file}}:{{line_start}}) | {{automation}} |

## Signaux de risque

| ID | Signal | Disponible | Seuil/config | Niveau de preuve |
|----|--------|------------|--------------|------------------|
| {{signal_id}} | {{name}} | {{available}} | {{threshold_or_config}} | {{evidence_level}} |

## Signaux lagging

{{lagging_signals_summary}}

## Data readiness

{{data_readiness_summary}}

## Réglages externes à vérifier

{{external_settings_summary}} — voir `EXTERNAL_CHECKLIST.md`.

## Actions automatisables

{{auto_safe_items}}

## Actions nécessitant validation

{{auto_with_approval_items}}

## Actions manuelles

{{manual_external_items}}

## Hors périmètre / stratégie humaine

{{strategy_human_items}}

## Non-regrettable churn

Certains clients ne devraient pas être retenus (mauvais fit produit,
usage abusif, coût de support disproportionné). Ce rapport ne recommande
jamais de rétention automatique pour ces cas — voir les items marqués
`STRATEGY_REQUIRED`.

## Plan P0

{{p0_plan}}

## Plan P1

{{p1_plan}}

## Plan P2

{{p2_plan}}

## Limites et niveau de confiance

{{limitations}}

## Sources

Voir `SOURCES.md` pour le niveau de confiance de chaque benchmark cité.

---

Pour appliquer un correctif :
`/anti-churn-audit fix <finding-id>`
