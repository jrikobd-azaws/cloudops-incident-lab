# CHG-001 Security group correction for API service connectivity

## Change summary
This change restored the inbound security group rule for TCP port 5000 on the EC2 instance hosting the `voice-api` service.

## Related incident
- `INC-002 Network blackhole due to security group misconfiguration`

## Reason for change
The inbound rule for port 5000 had been removed during a controlled incident simulation, causing external browser/public access failure while the service remained healthy locally.

## Change performed
- Re-added security group inbound rule:
  - Type: Custom TCP
  - Port: `5000`
  - Source: appropriate allowed source for external validation

## Validation
- Browser access to `http://PUBLIC_IP:5000/health` succeeded after the change
- Local EC2 validation remained healthy
- `voice-api` stayed active under `systemd`

## Risk
Low. The change restored a previously working inbound rule for the service validation path.

## Outcome
Successful. API connectivity was restored and the linked incident was resolved.