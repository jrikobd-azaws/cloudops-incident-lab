# Incident Documentation

This section contains the incident evidence pack for the three core operational scenarios in the **CloudOps Incident Lab**.

The incident documents are designed to reflect a structured platform-operations workflow rather than informal troubleshooting notes. Each incident is documented as a small operational record set showing detection, triage, communication, and outcome.

## Incident set

### INC-001 — Memory degradation on the Linux API service
This incident demonstrates host memory pressure on the EC2-hosted API service, CloudWatch alarm detection, Linux triage, service validation, and post-incident problem thinking.

Files:
- [`incident-record.md`](./INC-001-memory-degradation/incident-record.md)
- [`triage-notes.md`](./INC-001-memory-degradation/triage-notes.md)
- [`handover-note.md`](./INC-001-memory-degradation/handover-note.md)
- [`stakeholder-update.md`](./INC-001-memory-degradation/stakeholder-update.md)

Linked record:
- [`../../problem-records/PRB-001-recurring-memory-growth.md`](../problem-records/PRB-001-recurring-memory-growth.md)

### INC-002 — Network blackhole / security group issue
This incident demonstrates the difference between local application health and external service availability when network controls break endpoint reachability.

Files:
- [`incident-record.md`](./INC-002-network-blackhole/incident-record.md)
- [`triage-notes.md`](./INC-002-network-blackhole/triage-notes.md)
- [`handover-note.md`](./INC-002-network-blackhole/handover-note.md)
- [`stakeholder-update.md`](./INC-002-network-blackhole/stakeholder-update.md)

Linked record:
- [`../../change-records/CHG-001-security-group-correction.md`](../change-records/CHG-001-security-group-correction.md)

### INC-003 — Voice provider dependency outage
This incident demonstrates the “platform up, service degraded” pattern, where the EC2-hosted service remains healthy while an upstream voice dependency fails.

Files:
- [`incident-record.md`](./INC-003-voice-provider-outage/incident-record.md)
- [`triage-notes.md`](./INC-003-voice-provider-outage/triage-notes.md)
- [`handover-note.md`](./INC-003-voice-provider-outage/handover-note.md)
- [`stakeholder-update.md`](./INC-003-voice-provider-outage/stakeholder-update.md)

Additional record:
- vendor escalation note if included in the incident folder

## Documentation pattern

Each incident is documented using a consistent structure:

- **incident record** — summary, impact, detection, timeline, outcome
- **triage notes** — operational checks, commands, interpretation
- **handover note** — status snapshot for the next shift or team
- **stakeholder update** — concise non-technical or mixed-audience communication

Where relevant, incidents are linked to:

- problem records
- change records
- Jira evidence
- CloudWatch alarm screenshots
- Linux validation output
- recovery-state screenshots

## Why this matters

The aim of this section is to show that operational work is not just about finding a technical fault. It is also about:

- understanding business impact
- interpreting alerts correctly
- documenting actions clearly
- communicating status professionally
- closing incidents in a structured way
- capturing lessons for future prevention

## Suggested reading order

1. [`INC-001-memory-degradation/incident-record.md`](./INC-001-memory-degradation/incident-record.md)
2. [`INC-002-network-blackhole/incident-record.md`](./INC-002-network-blackhole/incident-record.md)
3. [`INC-003-voice-provider-outage/incident-record.md`](./INC-003-voice-provider-outage/incident-record.md)

## Related areas

- [Main README](../../README.md)
- [Monitoring README](../../monitoring/README.md)
- [API service README](../../app/api-service/README.md)
- [Linux operations](../../linux-ops/README.md)
- [ITIL framework and operational process notes](../itil-framework/README.md)
