# Triage Notes - INC-002

## Initial signal
External access to the API `/health` endpoint failed after the inbound rule for port 5000 was removed from the EC2 security group.

## Immediate checks
- Verified browser/public access failure to `http://PUBLIC_IP:5000/health`
- Checked local API health from the EC2 host with `curl http://127.0.0.1:5000/health`
- Confirmed service state with `systemctl status voice-api`
- Confirmed listening socket with `ss -tulpn | grep 5000`
- Reviewed security group inbound rules in AWS Console

## Key observations
- Browser/public access timed out
- Local curl returned `{"status":"healthy"}`
- `voice-api` stayed active under `systemd`
- Port `5000` was still listening locally
- Security group no longer allowed inbound access on port 5000

## Fault-domain assessment
This was not an application failure and not an EC2 host failure. The failure domain was the network access path controlled by the security group.

## Why this mattered
Without local validation, the incident could have been misclassified as an application outage. The triage process showed the importance of separating:
- external reachability
- local process health
- host health
- security control configuration

## Resolution path
The issue was resolved by restoring the inbound security group rule for TCP port 5000 through the linked change record.