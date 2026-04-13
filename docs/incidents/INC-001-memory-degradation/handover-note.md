# Handover Note - INC-001

## Current state

**Resolved.** The `COIL-App-HighMemory` alarm returned to `OK` after the controlled memory-pressure test ended.

## Incident summary

A controlled memory-pressure test triggered the CloudWatch high-memory alarm for the EC2-hosted API service. First-line Linux triage confirmed elevated host memory usage while the `voice-api` service remained active and the `/health` endpoint continued to respond.

## Business impact

- No customer-facing outage occurred
- This was a controlled validation exercise for monitoring, triage, and recovery workflow
- The event demonstrated a realistic degraded-risk condition rather than a service crash

## Actions completed

- generated memory pressure using `stress-ng`
- confirmed CloudWatch alarm transition to `ALARM`
- collected Linux triage evidence
- verified `voice-api` remained active under `systemd`
- verified `/health` endpoint remained available
- confirmed the alarm returned to `OK`
- documented the incident and linked supporting records

## Outstanding actions

- review whether memory thresholds should be tuned for future testing
- expand runbook guidance for memory-pressure triage if needed
- track recurring patterns through the linked problem record

## Handover assessment

No immediate operational action is required. The incident is resolved, evidence has been captured, and the event can now be used as a reference case for memory-related monitoring and triage scenarios.

## Related records

- [Incident record](./incident-record.md)
- [Triage notes](./triage-notes.md)
- [Stakeholder update](./stakeholder-update.md)
- [Problem record — PRB-001 recurring memory growth](../../problem-records/PRB-001-recurring-memory-growth.md)
- [CloudWatch alarms](../../../monitoring/cloudwatch-alarms.md)
- [Alert scenarios](../../../monitoring/alert-scenarios.md)
- [Incidents index](../README.md)
