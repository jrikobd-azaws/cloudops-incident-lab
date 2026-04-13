# Stakeholder Update - INC-002

## Status

**Resolved**

## Summary

A controlled network-access test was performed against the EC2-hosted API service by removing the inbound security group rule for port `5000`.

External access failed as expected, while local validation on the server confirmed that the API service remained healthy and active.

The issue was resolved by restoring the security group rule, and public access to the `/health` endpoint was successfully recovered.

## Customer impact

- No real customer-facing outage occurred
- This was a controlled validation exercise rather than an unplanned production failure
- The event demonstrated loss of external reachability while the service itself remained healthy

## Outcome

The incident confirmed that:

- public access can fail due to network controls even when the application remains healthy
- local validation is essential before classifying a service issue as an application outage
- restoring the inbound security group rule was the correct recovery action
- the linked change process provided a clean rollback path

## Next step

The incident is closed. Follow-up improvement ideas, including future external health-check alerting and runbook guidance, can be tracked separately.

## Related records

- [Incident record](./incident-record.md)
- [Triage notes](./triage-notes.md)
- [Handover note](./handover-note.md)
- [Change record — CHG-001 Security group correction](../../change-records/CHG-001-security-group-correction.md)
- [CloudWatch alarms](../../../monitoring/cloudwatch-alarms.md)
- [Incidents index](../README.md)