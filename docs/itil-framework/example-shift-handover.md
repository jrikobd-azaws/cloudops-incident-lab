# Example Shift Handover

## Purpose

This example shows what a clear incident handover can look like in the **CloudOps Incident Lab**.

It is based on the style of continuity expected in platform operations: concise status, current risk, checks already completed, and a clear next-action path.

## Incident ID

`INC-002`

## Current status

`Resolved`

## Affected service

`voice-api` external `/health` endpoint on port `5000`

## Business impact

External/public access to the API was unavailable after the inbound security group rule for port `5000` was removed.  
Local service health remained normal on the EC2 host.

This was a controlled validation exercise, so no real customer-facing outage occurred.

## Timeline summary

- `10:05` Baseline validation confirmed `/health` worked externally and locally
- `10:10` Inbound port `5000` rule removed from the EC2 security group
- `10:12` External access failure confirmed in browser
- `10:14` Local `curl` to `127.0.0.1:5000/health` returned healthy
- `10:16` `systemctl status voice-api` confirmed service active
- `10:18` `ss -tulpn | grep 5000` confirmed local listener still present
- `10:22` Change action `CHG-001` used to restore inbound port `5000`
- `10:25` External access validated as restored
- `10:30` Incident and change records updated and resolved

## Checks completed

- verified external access failure
- verified local `/health` endpoint remained healthy
- confirmed `voice-api` stayed active under `systemd`
- confirmed port `5000` was still listening locally
- reviewed security group rule state in AWS
- validated service recovery after rule restoration

## Current hypothesis

The incident was caused by **security-group misconfiguration affecting the network path**, not by host failure or application failure.

## Outstanding risks

- no active service risk remains
- future external reachability checks could be improved with additional monitoring guidance

## Next actions

- retain the incident and change records as reference documentation
- consider adding a short runbook for public-reachability triage
- review whether an external health-check alerting path should be added later

## Escalations or dependencies

- linked change record used for controlled recovery: `CHG-001`
- no further escalation required after validation of recovery

## Notes for next shift

The incident is resolved.  
The key lesson is that **local service health and external service reachability must be assessed separately**. If a similar event recurs, check the network/security path before treating it as an application outage.

## Related records

- [Handover template](./handover-template.md)
- [Jira workflow](./jira-workflow.md)
- [Escalation matrix](./escalation-matrix.md)
- [SLA and severity matrix](./sla-severity-matrix.md)
- [INC-002 incident record](../incidents/INC-002-network-blackhole/incident-record.md)
- [CHG-001 Security group correction](../change-records/CHG-001-security-group-correction.md)
- [Incident documentation index](../incidents/README.md)
