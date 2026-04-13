# PRB-001 Recurring memory growth

## Problem statement

The Linux API host is vulnerable to elevated memory-utilisation conditions that could degrade service performance or service stability if sustained over time.

## Related incident

- [INC-001 Memory degradation on Linux API service](../incidents/INC-001-memory-degradation/incident-record.md)

## Evidence

- CloudWatch `COIL-App-HighMemory` entered `ALARM`
- controlled testing with `stress-ng` demonstrated how quickly host memory pressure can rise on a small EC2 instance
- Linux diagnostics confirmed that this was a host-resource pressure event rather than an application crash
- the `voice-api` service remained available, but the condition showed clear degraded-risk potential

## Root cause category

**Host resource pressure / memory saturation scenario**

## Problem analysis

This problem record does not represent a confirmed application memory leak.  
Instead, it captures an operational weakness: a small EC2 host can move into a high-memory condition quickly enough to create service risk before a full outage occurs.

The incident demonstrated the importance of:

- early memory-pressure detection
- clear first-line Linux triage
- distinguishing host pressure from direct application failure
- defining follow-up actions before the same pattern becomes service-impacting in a non-controlled event

## Recommended follow-up

- create a runbook for high-memory triage
- review memory thresholds and alarm tuning
- consider service-level protection or scaling improvements
- add controlled memory-test guidance to documentation

## Related records

- [Incident record](../incidents/INC-001-memory-degradation/incident-record.md)
- [Triage notes](../incidents/INC-001-memory-degradation/triage-notes.md)
- [Handover note](../incidents/INC-001-memory-degradation/handover-note.md)
- [Stakeholder update](../incidents/INC-001-memory-degradation/stakeholder-update.md)
- [CloudWatch alarms](../../monitoring/cloudwatch-alarms.md)
- [Alert scenarios](../../monitoring/alert-scenarios.md)
- [Incidents index](../incidents/README.md)