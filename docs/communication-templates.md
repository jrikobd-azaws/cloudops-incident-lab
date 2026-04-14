# Communication Templates

## Purpose

These templates provide short, reusable communication patterns for the **CloudOps Incident Lab**.

They are designed to reflect the kind of structured, professional updates expected in platform operations work: clear status, accurate impact language, and concise next steps.

## Internal engineering update

**Incident:** `[ID]`  
**Status:** `[Status]`  
**Service:** `[Service]`  
**Impact:** `[Impact]`  
**Current assessment:** `[Assessment]`  
**Actions completed:** `[Actions]`  
**Next step:** `[Next step]`

### Example

**Incident:** `INC-002`  
**Status:** `Investigating`  
**Service:** `voice-api /health endpoint`  
**Impact:** `External reachability failure; local service remains healthy`  
**Current assessment:** `Likely network-path issue after security group change`  
**Actions completed:** `Validated local health, confirmed systemd service state, confirmed listener on port 5000`  
**Next step:** `Review and restore inbound security group rule through linked change path`

## Customer-safe update

We are currently investigating a service issue affecting **[service/function]**.

Initial checks are in progress and we are continuing to assess impact and recovery status. Further updates will be provided as more information becomes available.

### Example

We are currently investigating a service issue affecting **external access to the API health endpoint**.

Initial checks are in progress and we are continuing to assess impact and recovery status. Further updates will be provided as more information becomes available.

## Vendor / dependency escalation

We have confirmed that the local platform remains healthy and reachable.

Current evidence indicates repeated upstream dependency failures affecting **[function/service]**. Please review the attached symptoms and advise on current provider-side status, likely cause, and recommended next actions.

### Example

We have confirmed that the local platform remains healthy and reachable.

Current evidence indicates repeated upstream dependency failures affecting **voice-service registration and outbound call establishment**. Please review the attached symptoms and advise on current provider-side status, likely cause, and recommended next actions.

## Shift handover summary

**Shift handover:** `[time range]`  
**Open items:** `[incident IDs / work items]`  
**Current priorities:** `[priorities]`  
**Outstanding risks:** `[risks]`  
**Next actions:** `[actions]`

### Example

**Shift handover:** `08:00-16:00`  
**Open items:** `INC-003`  
**Current priorities:** `Confirm dependency fault domain and maintain service-status clarity`  
**Outstanding risks:** `Upstream provider degradation may continue; no local platform fault currently indicated`  
**Next actions:** `Monitor dependency evidence, preserve incident timeline, continue escalation path if symptoms persist`

## Communication principles

All operational communication in this project should aim to be:

- clear
- concise
- accurate
- proportionate to impact
- explicit about current status and next steps

Good communication should avoid overstating certainty when investigation is still ongoing.

## Related records

- [Main README](../README.md)
- [Incident documentation index](./incidents/README.md)
- [ITIL framework and operational process notes](./itil-framework/README.md)
- [Jira workflow](./itil-framework/jira-workflow.md)
- [Handover template](./itil-framework/handover-template.md)
- [Example shift handover](./itil-framework/example-shift-handover.md)