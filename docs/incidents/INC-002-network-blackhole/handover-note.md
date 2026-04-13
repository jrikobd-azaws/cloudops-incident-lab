# Handover Note - INC-002

## Current state
Resolved. External API connectivity was restored after the inbound port 5000 rule was re-added to the EC2 security group.

## Incident summary
A controlled network blackhole was created by removing the inbound security group rule for the API service port. Public access failed, but the service remained healthy and reachable locally on the EC2 host.

## Business impact
No real customer outage occurred. This was a controlled validation of network triage and recovery workflow.

## Actions completed
- Confirmed healthy baseline before change
- Removed inbound port 5000 rule
- Verified external access failure
- Verified local API health remained normal
- Confirmed service remained active under `systemd`
- Confirmed socket remained bound to port 5000
- Restored the inbound port 5000 rule
- Verified public access recovery

## Outstanding actions
- Add incident evidence and screenshots to GitHub
- Finalize Incident 002 documentation
- Link change record clearly in repository docs
- Consider adding a future external health-check alerting path