# Vendor Escalation Note - INC-003

## Escalation summary

Local platform checks remain healthy, the service is active under `systemd`, and the `/health` endpoint is reachable both locally and externally.

Failure evidence is isolated to the simulated upstream provider path, including registration failure and outbound call-establishment errors.

## Dependency failure evidence

- outbound registration failure
- `503 Service Unavailable`
- unable to establish outbound call
- retry scheduled for upstream registration failure

## Local validation completed

- `curl http://127.0.0.1:5000/health` returned a healthy response
- `voice-api` remained active under `systemd`
- no host-level outage indicators were observed
- no evidence suggested a local application crash or restart condition

## Assessment

Treat this as a **provider / dependency fault-domain event** rather than an internal platform outage.

The key operational distinction is:

- the platform remained healthy
- the application remained available
- the degraded condition was isolated to the upstream dependency path

Because of this, restarting the application or treating the incident as a host failure would not have addressed the underlying issue.

## Escalation objective

The purpose of this escalation note is to document the correct handling pattern for a **“platform up, dependency degraded”** voice-service event.

## Operational conclusion

This incident should be used as a reference case for future dependency-related degradation scenarios where upstream service behaviour, not local platform health, determines the response path.

## Related records

- [Incident record](./incident-record.md)
- [Triage notes](./triage-notes.md)
- [Handover note](./handover-note.md)
- [Stakeholder update](./stakeholder-update.md)
- [Incidents index](../README.md)