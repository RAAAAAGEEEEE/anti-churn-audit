# Changelog

All notable changes to this project are documented here.
Format loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [0.1.0] - 2026-07-21

### Added
- Initial P0 release: audit pipeline (phases 0-14), four execution modes
  (audit / plan / fix / verify).
- Provider matrix for Stripe, Paddle, Lemon Squeezy, Chargebee, RevenueCat,
  App Store / Google Play, PayPal/Braintree.
- Deterministic heuristic scoring engine (`risk-engine`) with configurable
  weights, data-coverage gating, and per-signal evidence.
- JSON schemas for audit reports and remediation manifests, with stdlib-only
  Python validators.
- Markdown templates for audit report, remediation plan, external checklist.
- 12 eval scenarios with fixtures covering single/multi-provider, missing
  analytics, periodic usage, cold-start, bad-fit, and webhook-integrity
  edge cases.
- Clean-room legal posture documented in `docs/LEGAL_AND_ATTRIBUTION.md` and
  `docs/UPSTREAM_WATCH.md` regarding ChurnGuard AI (no compatible license
  found at verification time; no code, prompts, or notebook content reused).

### Known limitations
- No ML scoring, no SHAP-style explanations yet (planned P2, interface only).
- No account-level GRR/NRR computation yet (planned P1).
- No calibration against historical outcomes yet (planned P1/P2).
