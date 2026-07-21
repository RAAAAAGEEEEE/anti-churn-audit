# Checklist rapide — avant de livrer un audit

- [ ] Phase 0 exécutée : SHA relevé, fichiers non commités listés, aucune
      écriture hors du dossier de sortie.
- [ ] Discovery : stack, providers (séparés), analytics, comptes détectés.
- [ ] Contexte produit déterminé ou marqué `CONTEXT_REQUIRED`.
- [ ] Chaque mécanisme audité a une chaîne de preuve tracée (pas de simple
      grep) avec un niveau L0-L4 explicite.
- [ ] Aucun `VERIFIED` sans preuve L3/L4.
- [ ] Aucun réglage dashboard marqué `ABSENT` — `EXTERNAL_UNKNOWN` à la
      place.
- [ ] T1/T5/T6/T9/T12 marqués `STRATEGY_REQUIRED` pour leur conclusion.
- [ ] Modules déclenchés uniquement selon les règles A-K applicables
      (`references/audit-patterns.md`).
- [ ] `risk_score` accompagné de `data_coverage` ; `INSUFFICIENT_DATA`
      affiché si `data_coverage < 0.50`.
- [ ] Chaque finding a tous les champs requis (voir
      `docs/REPORT_FORMAT.md#champs-dun-finding`).
- [ ] Les 6 artefacts de sortie sont présents.
- [ ] `anti-churn-audit.json` validé par `scripts/validate_report.py`.
- [ ] `remediation-manifest.json` validé par `scripts/validate_manifest.py`.
- [ ] Aucun secret (clé, token, mot de passe) reproduit dans les rapports.
- [ ] Aucune action `AUTO_WITH_APPROVAL` exécutée sans confirmation
      explicite de l'utilisateur.
- [ ] Le rapport se termine par l'invite `/anti-churn-audit fix <finding-id>`.
