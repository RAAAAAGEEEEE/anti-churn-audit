# Execution Flow — Pipeline obligatoire

Ce document décrit l'ordre d'exécution que `SKILL.md` doit suivre pour
chaque exécution en mode AUDIT. FIX/PLAN/VERIFY réutilisent des sous-parties
de ce pipeline (voir `SKILL.md`).

## PHASE 0 — Preflight

1. Identifier la racine du repo audité.
2. Vérifier que l'accès est en lecture seule pour l'audit (aucune écriture
   hors du dossier de sortie).
3. Relever le SHA Git courant (`git rev-parse HEAD`), ou noter `NO_GIT` si
   absent.
4. Relever les fichiers modifiés non commités (`git status --porcelain`).
5. Ne jamais `reset`/`checkout`/`stash` automatiquement.
6. Choisir le répertoire de sortie (demander si ambigu).
7. Rechercher un rapport précédent dans ce dossier de sortie.
8. Relever la date ISO-8601 courante.

## PHASE 1 — Discovery

Détecter, séparément pour chaque axe (ne jamais fusionner en une seule
supposition) :

- langages et frameworks ;
- monorepo ou non ;
- services (backend / frontend / workers) ;
- système de comptes/organisations (B2B compte vs B2C user) ;
- providers de paiement, **audités séparément par provider** ;
- analytics ;
- emails, support ;
- jobs/cron/queues ;
- base de données ;
- tests existants ;
- infrastructure versionnée (IaC).

Si plusieurs providers de paiement coexistent, ne jamais produire un statut
global unique — voir règle F de `references/audit-patterns.md`.

## PHASE 2 — Product Context

Déterminer ou demander à l'utilisateur :

- fréquence d'usage attendue (daily / weekly / periodic / transactional /
  seasonal / custom) ;
- modèle de compte (B2B organisation vs B2C utilisateur individuel) ;
- core action, outcome event, fenêtre de valeur attendue.

Si ce contexte manque : ne pas bloquer l'audit statique indépendant.
Marquer le scoring comportemental `DATA_REQUIRED` ou `CONTEXT_REQUIRED` et
continuer les phases suivantes.

## PHASE 3 — Static Mechanism Audit

Auditer les points T mécaniques (jamais les points stratégiques ici) :

- T2 onboarding/activation
- T3 paiements échoués
- T4 silent churn / instrumentation
- T7 GRR/NRR
- T8 expansion
- T10 cancellation flow
- T11 win-back

Et les signaux de risque séparément :

- S1 usage trend, S2 days inactive, S3 payment failures,
  S4 feature adoption breadth, S5 contract type, S6 support,
  S7 seat utilization, S8 MRR decline/downgrade.

Ne jamais confondre un identifiant `T` (mécanisme/point d'audit) avec un
identifiant `S` (signal de scoring).

## PHASE 4 — Evidence Tracing

Ne pas se contenter d'un grep. Pour chaque mécanisme, tracer la chaîne :

```
déclaration/import → configuration → handler/requête → persistance → action → test
```

Niveaux de preuve (voir `docs/STATUS_MODEL.md`) :

- **L0** — terme trouvé (grep seul, aucune garantie de branchement)
- **L1** — import ou configuration présents
- **L2** — handler ou requête branché
- **L3** — chaîne fonctionnelle reliée bout en bout
- **L4** — test automatisé pertinent couvrant le mécanisme

`VERIFIED` nécessite normalement **L3 ou L4**. Un terme trouvé uniquement
dans un commentaire ou une chaîne de log reste **L0**, jamais `VERIFIED`
(voir eval #9).

**La simple présence d'un fichier de test ne suffit jamais à justifier
L4.** L4 exige de confirmer que le test (a) exerce réellement la branche
concernée (assertions qui échoueraient si le mécanisme était cassé, pas
seulement un statut HTTP générique), et (b) est exécutable dans le
périmètre audité (dépendances/modules qu'il importe réellement présents).
Si l'un des deux n'est pas confirmable statiquement, plafonner à **L3**
et documenter la limitation précisément (voir eval `stripe-complete`,
finding sur la vérification de signature webhook, où un test présent
mais non contraignant — `expect(res.status).toBeLessThan(500)` — et
dépendant de modules absents du périmètre a été plafonné à L3 plutôt que
promu à L4 sur la seule foi de son existence).

Chaque finding contient : chemin relatif, ligne ou plage si disponible,
extrait court, niveau de preuve, explication, et limite de la preuve.

## PHASE 5 — Data Readiness

Vérifier (voir `references/data-contract.md`) :

account_id stable, mapping user→account, mapping provider_customer→account,
support multi-souscription, idempotence event_id, cohérence des timestamps,
devises en unités mineures, présence d'événements produit, core action,
outcome event, cohérence historique, données d'intervention, labels de
churn, distinction volontaire/involontaire.

## PHASE 6 — External Settings

Identifier ce qui est impossible à confirmer depuis le repo (Smart Retries
Stripe, réglages Paddle Retain/Lemon Squeezy/Chargebee, webhooks configurés
dans un dashboard, DNS/deliverability, listes de suppression, configuration
App Store/Google Play). Produire une checklist manuelle précise.

**Ne jamais marquer `ABSENT` un réglage de dashboard non versionné.**
Utiliser `EXTERNAL_UNKNOWN`.

## PHASE 7 — Strategy Boundaries

Pour T1, T5, T6, T9, T12 : ne jamais conclure automatiquement sur la
stratégie. Vérifier seulement si l'instrumentation ou les mécanismes
existent, marquer `STRATEGY_REQUIRED` pour la conclusion réelle, proposer
des questions d'interview, rappeler le non-regrettable churn, ne jamais
chercher à retenir automatiquement un client bad-fit.

## PHASE 8 — Classification

Voir `docs/STATUS_MODEL.md` pour la liste complète des statuts, niveaux de
confiance, sévérités et catégories d'automatisation.

## PHASE 9 — Conditional Triggers

Voir `references/audit-patterns.md` pour les règles A à K qui déterminent
quels modules se déclenchent selon les résultats de la discovery et du
contexte produit.

## PHASE 10 — Scoring

Voir `docs/SCORING_MODEL.md`. Le score s'appelle `risk_score` (jamais
« ML score », « churn probability » ou « predictive accuracy » sans modèle
entraîné, validé temporellement et calibré).

## PHASE 11 — Remediation Decision

Pour chaque finding, produire tous les champs listés dans
`docs/REPORT_FORMAT.md#champs-dun-finding`. Respecter strictement les
catégories d'automatisation (`AUTO_SAFE`, `AUTO_WITH_APPROVAL`,
`MANUAL_EXTERNAL`, `STRATEGY_HUMAN`) — voir `references/remediation-rules.md`.

## PHASE 12 — Output

Produire au minimum les 6 artefacts listés dans `docs/REPORT_FORMAT.md`.
Valider les deux fichiers JSON avec `scripts/validate_report.py` et
`scripts/validate_manifest.py` avant de considérer l'audit terminé.

## PHASE 13 — Optional Apply (mode FIX uniquement)

Uniquement si l'utilisateur a explicitement demandé FIX et confirmé un
`finding_id`. Avant modification : afficher les fichiers ciblés, expliquer
l'impact, relever `git status`. Ne jamais toucher aux modifications
utilisateur non liées, ne jamais reset/push/déployer, ne jamais modifier un
dashboard externe. Après modification : tests ciblés, lint/typecheck si
disponibles, `git diff --stat`, résumé des changements, statut des tests,
plan de rollback.

## PHASE 14 — Verify (mode VERIFY)

Vérifier : fichiers générés, schémas JSON, preuves/liens, statuts, absence
de secret, cohérence score/data coverage, provider matrix, tests, diff
limité au scope du finding concerné.
