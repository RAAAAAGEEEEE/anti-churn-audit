# Changelog

All notable changes to this project are documented here.
Format loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [0.1.1] - 2026-09-29

### Added
- Portable `SKILL.md` frontmatter: `license`, `compatibility`, `allowed-tools`,
  `metadata` (author, version, repository).
- `CONTRIBUTING.md`, `SECURITY.md`, and `docs/` pages: `INSTALLATION.md`,
  `USAGE.md`, `CONFIGURATION.md`, `TROUBLESHOOTING.md`, `LIMITATIONS.md`.
- `examples/stripe-incomplete/`: illustrative report and manifest that pass both
  validators.
- Glossary of `T`, `S`, `L` and `F` identifiers in `docs/REPORT_FORMAT.md`.

### Changed
- The security page is renamed `docs/PRIVACY_AND_SECURITY.md`; vulnerability
  reporting moved to the root `SECURITY.md`.
- README rewritten to the documentation standard (status, prerequisites,
  quickstart, limits, roadmap).
- An unexplained label on audit points is replaced by "point T", now defined in the glossary.
- `LICENSE` names the author instead of "contributors".

### Removed
- The "public / private separation" section of `docs/ARCHITECTURE.md`, which
  referred to a private overlay outside this repository.

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
