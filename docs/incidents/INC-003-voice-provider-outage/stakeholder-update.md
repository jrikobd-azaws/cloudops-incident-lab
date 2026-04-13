# Stakeholder Update - INC-003

## Status

**Resolved**

## Summary

A simulated upstream voice-provider degradation was introduced to validate operational triage and escalation procedures.

Provider-style registration failures and `503 Service Unavailable` responses were observed, while the EC2 host and `voice-api` platform remained healthy throughout the event.

The scenario was correctly classified as a **dependency-side service degradation** rather than an internal platform outage, and the validation exercise was completed successfully.

## Customer impact

- No real customer-facing outage occurred
- This was a controlled validation exercise rather than an unplanned production failure
- The event demonstrated degraded upstream voice-service behaviour while the local platform remained healthy

## Outcome

The incident confirmed that:

- upstream dependency failure can degrade service even when platform health remains normal
- local health validation is essential before treating a service issue as a host or application outage
- dependency-focused escalation is the correct operational response for this fault domain
- platform restart or host-level remediation would not have addressed the underlying issue

## Next step

The incident is closed. The captured evidence and escalation pattern can be used as a reference case for future dependency-related service degradation scenarios.

## Related records

- [Incident record](./incident-record.md)
- [Triage notes](./triage-notes.md)
- [Handover note](./handover-note.md)
- [Vendor escalation note](./vendor-escalation-note.md)
- [Incidents index](../README.md)