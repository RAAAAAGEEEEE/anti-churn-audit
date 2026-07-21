# Remediation Plan — {{repo}}

Date : {{date_iso}}
SHA : {{sha}}

Ce plan liste chaque finding avec son plan d'action complet. Voir
`remediation-manifest.json` pour la version structurée (source de vérité
pour l'automatisation).

## {{finding_id}} — {{title}}

- **Pourquoi c'est important** : {{why_it_matters}}
- **Statut** : {{status}} · **Sévérité** : {{severity}} · **Confiance** : {{confidence}}
- **Automatisation** : {{automation}}
- **Preuve** : {{evidence_summary}}
- **Prérequis** : {{prerequisites}}
- **Fichiers concernés (proposés)** : {{proposed_files}}
- **Étapes externes (dashboard, DNS, etc.)** : {{external_steps}}
- **Tests requis** : {{tests_required}}
- **Rollback** : {{rollback}}
- **Résultat attendu** : {{expected_result}}
- **Métrique de succès** : {{success_metric}}
- **Owner suggéré** : {{owner}}
- **Effort estimé** : {{estimated_effort}}
- **Dépendances** : {{dependencies}}
- **Raison de blocage (si applicable)** : {{blocking_reason}}

Pour lancer ce correctif après validation :
`/anti-churn-audit fix {{finding_id}}`

---

<!-- Répéter le bloc ci-dessus pour chaque finding, groupé par sévérité P0 / P1 / P2 / INFO -->
