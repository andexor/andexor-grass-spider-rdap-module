<!--
Sync Impact Report
- Version change: [TEMPLATE] → 1.0.0 (initial ratification)
- Modified principles: n/a (initial adoption; all five principles newly authored)
- Added sections: Core Principles (I-V), Technology & Platform Constraints,
  Development Workflow & Quality Gates, Governance
- Removed sections: none
- Templates requiring updates: dependent Spec Kit templates (plan/spec/tasks) read this
  file at runtime; no changes made here to those templates per scope guard.
- Follow-up TODOs:
  - TODO(RATIFICATION_DATE): original ratification date unknown; using the date this
    constitution was first authored (2026-09-22) as the ratification date. Confirm or
    correct with the actual project kickoff date if different.
-->

# Andexor Grass Spider RDAP Module Constitution

## Purpose

This is part of the Andexor Grass Spider
collection of services and agents that
Andexor Network, Inc., uses for SEO audits
and routine monitoring.

This repo is for hosting documentation only.
All functionality described here
is to be implemented in other repos.

## Core Principles

### I. Specification-First Development
Every feature or fix begins with an issue written like a user story, containing a
Description, Acceptance Criteria, and (when needed) Technical Details section. If a
formal specification exists or is warranted, it MUST be created or updated before
implementation work starts, and architecture documentation (use case, mind map, state,
activity, and sequence diagrams under `doc/uml`) MUST be added or updated alongside it.
Code changes that lack a corresponding issue or spec update are not accepted.

**Rationale**: This project is an SEO-audit RDAP client used by other Andexor Grass
Spider services; undocumented, spec-less changes make it impossible for downstream
agents and bootstrap/authoritative services to trust its contracts and behavior.

### II. Test-First & Verified Quality (NON-NEGOTIABLE)
Unit tests, integration tests, security tests, and performance tests MUST be written
and included with every change, along with test plans, test data, and results.
Negative examples (demonstrating the gap being fixed) and positive examples
(demonstrating the resolved behavior) MUST accompany the change. At least 80% of
included tests MUST pass before a PR is submitted for review. Auto-generated tests
that pass but verify nothing are prohibited and MUST be rejected in review.

**Rationale**: RDAP responses vary by registry and are easy to mishandle silently;
without enforced, meaningful test coverage, regressions in domain-registration data
retrieval would surface downstream in SEO audits rather than in CI.

### III. Compliance & Provenance on Every Commit
Every commit MUST be signed off (`git commit -s`) to indicate acceptance of the
Contributor Covenant 3.0 Code of Conduct, the Developer Certificate of Origin v1.1, and
the Apache License, Version 2.0. Commit messages MUST reference the originating issue
(`Closes #XX` or `Fixes #XX` for bug fixes) and MUST follow the Conventional Commits
specification (`feat:`, `fix:`, `docs:`, `docs(spec):`, etc.) so that releases can be
automated. Pull requests containing unsigned commits MUST NOT be merged.

**Rationale**: These requirements are fixed organizational policy (CONTRIBUTING.md,
DCO, LICENSE) that protects contributors and Andexor Network, Inc. legally and keeps
the release-automation tooling functional.

### IV. Secure, Validated Handling of External Data
Because this module queries third-party RDAP services over the network, all external
input (RDAP JSON responses, TLDs, domain names) MUST be validated before use, with
explicit error handling for malformed, incomplete, or hostile responses. TLDs SHOULD be
validated against the IANA/publicsuffix list before querying. Security tests MUST be
part of the standard test suite (Principle II), and no real credentials, tokens, API
keys, or other secrets may ever be committed or logged.

**Rationale**: RDAP endpoints are untrusted third-party services; this module's output
feeds automated SEO audits, so malformed or adversarial responses must fail safely
rather than corrupt downstream data or leak sensitive material.

### V. Minimal, Portable Footprint
New functionality MUST target the currently supported Python version declared in
`pyproject.toml` and MUST avoid adding dependencies beyond what is strictly necessary
for the feature. Development and production targets are open-source Linux (latest
Ubuntu LTS preferred); Alpine Linux and Docker "scratch"-based images SHOULD be
supported when it requires little additional effort. Windows support is prohibited
except for native apps that explicitly require it. Simplicity is preferred: do not add
abstractions, configuration options, or dependencies for hypothetical future needs.

**Rationale**: This module is one small piece of the larger Andexor Grass Spider
agent/service collection; keeping it lean and portable across the supported OS matrix
keeps deployment and container image size predictable across that collection.

## Technology & Platform Constraints

- Language/runtime: Python, version pinned via `requires-python` in `pyproject.toml`
  (currently >=3.14); dependency management via `uv`.
- Core dependencies (`httpx[http2]`, `whodap`) are the sanctioned way to perform RDAP
  and HTTP/2 network operations; new HTTP or RDAP client libraries MUST NOT be
  introduced without a documented reason in the triggering issue/spec.
- Documentation is built with PlantUML (for UML diagrams under `doc/uml`) and
  AsciiDoctor; new architecture or process documentation MUST use these tools and
  follow the existing `doc/` file structure and naming conventions.
- Licensing: Apache License, Version 2.0. All source files and dependencies MUST remain
  compatible with this license; license and dependency audit reports under `reports/`
  MUST be kept current (e.g., via `install-uv.sh`/audit tooling) as dependencies change.

## Development Workflow & Quality Gates

1. Open or reference an issue written as a user story (Description + Acceptance
   Criteria, optional Technical Details) before starting work; note the issue number.
2. Create a feature branch; update the specification and architecture diagrams first
   if the change affects behavior or contracts (Principle I).
3. Implement the change together with unit, integration, security, and performance
   tests, test plans, test data, and results, plus negative and positive examples
   (Principle II).
4. Update user-facing documentation when behavior changes; automate any new
   maintenance procedure, or document it if automation is not feasible.
5. Sync the branch with the remote before requesting review to avoid unmergeable PRs.
6. Commit with `git commit -s`, a Conventional Commits-formatted message, and an issue
   reference (`Closes #XX` / `Fixes #XX`) (Principle III).
7. Push the branch, open a pull request, and notify maintainers for review.
8. AI-assisted contributions are permitted but MUST meet the same bar as human-authored
   work: readable code, meaningful tests (>=80% passing), spec alignment, considered
   edge cases with input validation and error handling, and no AI-generated filler text
   left unedited in documentation, commits, or code comments.

## Governance

This constitution supersedes other informal project practices for matters it covers;
where it is silent, `CONTRIBUTING.md`, `SECURITY.md`, and `CODE_OF_CONDUCT.md` govern.
Amendments are proposed via a pull request that edits this file, must state the
rationale for the change, and follow the same signoff and Conventional Commits
requirements as any other change (`docs:` prefix). Versioning follows semantic
versioning: MAJOR for backward-incompatible governance or principle removals/
redefinitions, MINOR for new principles or materially expanded guidance, PATCH for
clarifications and non-semantic wording fixes. All pull requests and reviews MUST
verify compliance with the principles above; any deviation MUST be explicitly justified
in the PR description or it MUST be rejected. Use `CONTRIBUTING.md` for day-to-day
contributor workflow guidance and `SECURITY.md` for vulnerability disclosure procedure.

**Version**: 1.0.0 | **Ratified**: 2026-09-22 | **Last Amended**: 2026-09-22
