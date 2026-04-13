# Escalation Matrix

## Purpose

This document defines **when to escalate**, **to whom**, and **what information must be included** in the CloudOps Incident Lab.

The goal is to show structured operational judgement: escalate early enough to reduce risk, but with enough validated context to make the escalation useful.

## Escalation triggers

Escalate when one or more of the following apply:

- severity is **Sev 1** or **Sev 2**
- the fault domain is still unclear after initial checks
- dependency or vendor involvement is likely
- service remains degraded after initial mitigation
- specialist access or deeper technical knowledge is required
- a shift handover is required with unresolved risk
- the issue cannot be resolved safely within first-line ownership

## Escalation targets

| Scenario | Escalate to | Reason |
|---|---|---|
| Host instability or persistent resource alarm | Platform / infrastructure owner | Requires deeper host, Linux, or AWS review |
| Network path or security rule issue | Network / platform owner | Requires AWS connectivity or access-control review |
| Dependency or upstream service issue | Vendor / dependency contact | Local platform remains healthy but upstream service is failing |
| Repeated incident pattern | Problem management / follow-up owner | Root cause analysis and preventive action are needed |
| Access, threshold, or controlled config change | Service request / operations owner | Formal operational change or fulfilment is required |

## Required escalation context

Every escalation should include:

- incident ID
- current status
- affected service
- business impact
- timeline so far
- checks already completed
- current hypothesis or fault-domain assessment
- exact next action needed from the receiving owner

## Escalation quality principle

A good escalation should answer three questions clearly:

1. **What is happening?**
2. **What has already been checked?**
3. **Why is this being escalated now?**

This helps prevent vague handoffs and reduces duplicate troubleshooting effort.

## Example escalation decisions

- **INC-001 — Memory degradation**  
  Escalate if memory pressure persists, service stability declines, or host-level remediation is no longer enough.

- **INC-002 — Network blackhole**  
  Escalate when external access fails and security controls or network-path configuration are implicated.

- **INC-003 — Voice provider outage**  
  Escalate as a dependency-side issue when local platform health remains normal but upstream provider behaviour indicates degraded service.

## Notes

Escalation should be based on **operational need**, not hesitation or guesswork.

The aim is to escalate with enough evidence to support action, while avoiding delay when impact, uncertainty, or risk has already crossed the threshold for wider involvement.

## Related records

- [ITIL framework index](./README.md)
- [Jira workflow](./jira-workflow.md)
- [SLA and severity matrix](./sla-severity-matrix.md)
- [Handover template](./handover-template.md)
- [Example shift handover](./example-shift-handover.md)
- [Incident documentation index](../incidents/README.md)
- [Main README](../../README.md)
