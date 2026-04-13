# Jira Workflow

## Purpose

This workflow is used to track operational work in the **CloudOps Incident Lab** in a structured, support-oriented way.

It is designed to reflect the kind of lifecycle control expected in platform operations environments: clear triage, accurate status movement, controlled escalation, and complete closure documentation.

## Core issue types

The project uses the following Jira-style issue categories:

- **Incident** — unplanned service-impacting or risk-impacting event requiring triage and response
- **Problem** — recurring issue, pattern, or structural weakness requiring deeper analysis
- **Change** — controlled corrective or preventive action
- **Service Request** — operational request that does not represent an incident
- **Task** — supporting work item used for implementation or documentation activity

## Incident lifecycle

### 1. New
- issue created after detection, alerting, or report
- initial summary and scope recorded
- early impact and urgency noted

### 2. Investigating
- technical checks begin
- impact and fault domain assessed
- evidence captured
- initial stakeholder communication prepared where needed

### 3. Escalated
- additional team, owner, or dependency engaged
- escalation reason documented
- clear handover or escalation context recorded

### 4. Mitigated
- immediate risk reduced
- service impact lowered or controlled
- workaround, rollback, or partial recovery in place
- monitoring continues

### 5. Resolved
- service restored or validation complete
- findings documented
- linked problem, change, or follow-up work identified

### 6. Closed
- final documentation complete
- no further operational action required
- issue retained as a reference record

## Problem lifecycle

### 1. New
- problem identified from an incident or recurring pattern

### 2. Analysis
- evidence reviewed
- underlying causes or contributing conditions assessed

### 3. Root cause identified
- root cause or root cause category documented

### 4. Fix or recommendation defined
- corrective action, preventive action, or recommendation recorded

### 5. Closed
- no further problem-management action required

## Change lifecycle

### 1. Proposed
- change need identified
- change scope and reason documented

### 2. Approved
- change accepted for implementation

### 3. Implementing
- change applied in the target environment

### 4. Validation
- service and recovery checks completed
- outcome confirmed

### 5. Completed
- change record closed
- linked incident or follow-up updated

## Service request lifecycle

### 1. Submitted
- request logged

### 2. Reviewed
- request scope and relevance checked

### 3. Approved
- fulfilment authorised

### 4. Fulfilled
- request completed

### 5. Closed
- record completed with no further action needed

## Workflow principle

The workflow is intentionally simple and operationally focused.

It emphasizes:

- triage quality
- correct fault-domain assessment
- escalation timing
- handover clarity
- evidence capture
- clean closure documentation

The goal is not administrative complexity. The goal is to show disciplined operational ownership.

## How this appears in the project

This workflow is reflected across the repository through:

- incident records
- problem records
- change records
- stakeholder updates
- handover notes
- Jira screenshots showing structured status progression

## Related records

- [ITIL framework index](./README.md)
- [SLA severity matrix](./sla-severity-matrix.md)
- [Escalation matrix](./escalation-matrix.md)
- [Handover template](./handover-template.md)
- [Example shift handover](./example-shift-handover.md)
- [Incident documentation index](../incidents/README.md)
- [Main README](../../README.md)
