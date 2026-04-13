# Handover Note - INC-002

## Current state

**Resolved.** External API connectivity was restored after the inbound port `5000` rule was re-added to the EC2 security group.

## Incident summary

A controlled network blackhole was created by removing the inbound security group rule for the API service port. Public access failed, but the service remained healthy and reachable locally on the EC2 host.

## Business impact

- No real customer outage occurred
- This was a controlled validation of network triage and recovery workflow
- The incident demonstrated loss of external reachability without application failure

## Actions completed

- confirmed healthy baseline before the change
- removed inbound port `5000` rule
- verified external access failure
- verified local API health remained normal
- confirmed the service remained active under `systemd`
- confirmed the socket remained bound to port `5000`
- restored the inbound port `5000` rule
- verified public access recovery
- linked the incident to the related change record

## Outstanding actions

- review whether future external health-check alerting should be added
- consider adding a short runbook for public-reachability triage
- keep the linked change record as the formal rollback reference

## Handover assessment

No immediate operational action is required. The incident is resolved, the service is externally reachable again, and the evidence confirms that the failure domain was the security-group rule rather than the application or host.

## Related records

- [Incident record](./incident-record.md)
- [Triage notes](./triage-notes.md)
- [Stakeholder update](./stakeholder-update.md)
- [Change record — CHG-001 Security group correction](../../change-records/CHG-001-security-group-correction.md)
- [Monitoring README](../../../monitoring/README.md)
- [CloudWatch alarms](../../../monitoring/cloudwatch-alarms.md)
- [Alert scenarios](../../../monitoring/alert-scenarios.md)
- [Incidents index](../README.md)