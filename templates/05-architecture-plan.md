# Architecture Plan — {{PRODUCT_NAME}}

## Stack

| Layer | Choice | Justified against | Alternatives rejected |
|---|---|---|---|
| | | PRIN-nn / DOM-nn | |

## Architecture decisions

### ADR-001 — {{title}}
**Context:**
**Options considered:**
**Decision:**
**Consequences (including the bad ones):**
**Enforces:** PRIN-nn

## Data model

| Entity | Owns | Relationships | Tenancy boundary | Retention | Required by |
|---|---|---|---|---|---|
| | | | | | FR-nnn |

## Integrations

| System | Purpose | Auth | Rate limit | Data freshness | Failure mode | Product implication |
|---|---|---|---|---|---|---|

**Product implication** is the important column. If an API refreshes daily rather than in real time, the PRD's notification language must change — amend the PRD, do not paper over it in code.

## Security & compliance posture
- AuthN / AuthZ model:
- Encryption at rest / in transit:
- Audit logging scope:
- PII / PHI handling:
- Data residency:
- Maps to: NFR-nnn, DOM-nn regulatory obligations

## Environments & deployment
## Observability
- Logs / metrics / traces:
- Alert thresholds tied to: NFR-nnn

## Rollback strategy
## Build sequencing constraints
| Must exist first | Before | Why |
|---|---|---|
