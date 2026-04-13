# SLA and Severity Matrix

## Purpose

This matrix defines how incidents are prioritised in the **CloudOps Incident Lab** based on **impact** and **urgency**.

The aim is to show a practical, operations-focused approach to severity assessment rather than a rigid enterprise policy model.

## Severity levels

| Severity | Description | Example | Expected response |
|---|---|---|---|
| **Sev 1** | Critical service outage or severe customer impact | Core service unavailable, widespread transaction failure | Immediate response and active coordination |
| **Sev 2** | Major degradation with meaningful impact | Dependency issue, partial feature failure, sustained alarm condition | Prompt investigation and escalation if required |
| **Sev 3** | Limited or low-impact issue | Intermittent issue, minor degradation, low-risk alarm | Investigate in normal operational flow |
| **Sev 4** | Informational or housekeeping issue | Documentation fix, minor request, non-urgent cleanup | Planned or backlog handling |

## Severity guidance

### Sev 1

Use when:

- service is fully unavailable
- impact is widespread and urgent
- a business-critical workflow is blocked
- immediate coordination is required to reduce active service impact

### Sev 2

Use when:

- service is still up but degraded
- a dependency failure affects a meaningful subset of capability
- operational risk is clear even if total outage has not occurred
- escalation may be required if the condition continues

### Sev 3

Use when:

- the issue is contained
- a workaround exists
- impact is limited or non-critical
- the event still requires investigation, but not immediate high-priority coordination

### Sev 4

Use when:

- no active customer or service impact exists
- the work is administrative, advisory, or preventive
- urgency is low
- the item can be handled through planned follow-up or backlog work

## How severity is judged in this project

Severity is assessed using two main questions:

1. **How much service or business impact exists?**
2. **How urgent is the response required?**

This means severity should reflect operational reality, not just technical complexity.

A technically interesting issue may still be low severity if impact is low.  
Likewise, a simple issue may be high severity if it causes major service loss.

## Incident mapping in this lab

- **INC-001 — Memory degradation on Linux API service** → **Sev 2**  
  The service remained available, but host resource pressure created meaningful operational risk and required prompt triage.

- **INC-002 — Network blackhole / security group issue** → **Sev 2**  
  External service access failed while the application remained healthy locally, creating meaningful service degradation and requiring controlled recovery.

- **INC-003 — Voice provider outage / simulated SIP dependency failure** → **Sev 2**  
  The platform remained healthy, but an upstream dependency degraded a meaningful service function and required dependency-focused escalation.

## Notes

Severity should reflect **actual impact and urgency**, not just how technical the issue looks.

This is important in platform operations because good incident handling depends on:

- correct prioritisation
- accurate fault-domain assessment
- proportionate escalation
- clear communication

## Related records

- [ITIL framework index](./README.md)
- [Jira workflow](./jira-workflow.md)
- [Escalation matrix](./escalation-matrix.md)
- [Handover template](./handover-template.md)
- [Example shift handover](./example-shift-handover.md)
- [Incident documentation index](../incidents/README.md)
- [Main README](../../README.md)
