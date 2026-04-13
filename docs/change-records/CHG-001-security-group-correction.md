# CHG-001 Security group correction for API service connectivity

## Change summary

This change restored the inbound security group rule for TCP port `5000` on the EC2 instance hosting the `voice-api` service.

## Related incident

- [INC-002 Network blackhole due to security group misconfiguration](../incidents/INC-002-network-blackhole/incident-record.md)

## Reason for change

The inbound rule for port `5000` had been removed during a controlled incident simulation. This caused external browser/public access to fail while the service remained healthy and reachable locally on the EC2 host.

## Change performed

The following security group rule was restored:

- **Type:** Custom TCP
- **Port:** `5000`
- **Source:** appropriate allowed source for external validation

## Validation

The following checks confirmed successful recovery:

- browser access to `http://PUBLIC_IP:5000/health` succeeded after the change
- local EC2 validation remained healthy
- `voice-api` stayed active under `systemd`
- the application continued listening on port `5000`

## Risk

**Low.**  
This change restored a previously working inbound rule for the service validation path and did not alter the application itself.

## Outcome

**Successful.**  
API connectivity was restored and the linked incident was resolved.

## Related records

- [Incident record](../incidents/INC-002-network-blackhole/incident-record.md)
- [Triage notes](../incidents/INC-002-network-blackhole/triage-notes.md)
- [Handover note](../incidents/INC-002-network-blackhole/handover-note.md)
- [Stakeholder update](../incidents/INC-002-network-blackhole/stakeholder-update.md)
- [Incidents index](../incidents/README.md)