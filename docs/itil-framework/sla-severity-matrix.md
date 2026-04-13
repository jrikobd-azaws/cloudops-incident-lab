# SLA and Severity Matrix

## Purpose
This matrix defines how incidents are prioritized based on impact and urgency.

## Severity levels

| Severity | Description | Example | Expected response |
|---|---|---|---|
| Sev 1 | Critical service outage or severe customer impact | Core service unavailable, widespread transaction failure | Immediate response and active coordination |
| Sev 2 | Major degradation with meaningful impact | Dependency issue, partial feature failure, sustained alarm condition | Prompt investigation and escalation if required |
| Sev 3 | Limited or low-impact issue | Intermittent issue, minor degradation, low-risk alarm | Investigate in normal operational flow |
| Sev 4 | Informational or housekeeping issue | Documentation fix, minor request, non-urgent cleanup | Planned or backlog handling |

## Severity guidance

### Sev 1
Use when:
- service is fully unavailable, or
- impact is widespread and urgent, or
- business-critical workflow is blocked

### Sev 2
Use when:
- service is still up but degraded, or
- a dependency failure affects a meaningful subset of capability, or
- there is clear operational risk if not addressed soon

### Sev 3
Use when:
- issue is contained,
- workaround exists,
- impact is limited or non-critical

### Sev 4
Use when:
- no active customer/service impact exists,
- work is administrative or advisory,
- urgency is low

## Incident mapping in this lab
- `INC-001 Memory degradation` -> Sev 2
- `INC-002 Network blackhole` -> Sev 2
- `INC-003 Voice provider outage` -> Sev 2

## Notes
Severity should reflect actual impact and urgency, not just how technical the issue looks.