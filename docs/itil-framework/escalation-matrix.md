# Escalation Matrix

## Purpose
This document defines when to escalate, to whom, and what information must be included.

## Escalation triggers
Escalate when one or more of the following apply:
- severity is Sev 1 or Sev 2
- fault domain is unclear after initial checks
- dependency or vendor involvement is likely
- service remains degraded after initial mitigation
- specialist knowledge is required
- shift handover is required with unresolved risk

## Escalation targets

| Scenario | Escalate to | Reason |
|---|---|---|
| Host instability or persistent resource alarm | Platform / infrastructure owner | Requires deeper host or AWS review |
| Network path or security rule issue | Network / platform owner | Requires AWS access-control review |
| Dependency or upstream service issue | Vendor / dependency contact | Local platform remains healthy but upstream service is failing |
| Repeated incident pattern | Problem management / follow-up owner | Root cause and prevention needed |
| Access or threshold request | Service request / operations owner | Controlled operational change needed |

## Required escalation context
Every escalation should include:
- incident ID
- current status
- affected service
- business impact
- timeline so far
- checks already completed
- current hypothesis
- exact next action needed

## Example escalation decisions
- `INC-001` -> escalate if memory pressure persists or service stability declines
- `INC-002` -> escalate when external access fails and security controls are implicated
- `INC-003` -> escalate as a dependency-side issue when local platform health remains normal