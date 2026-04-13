# Triage Notes - INC-001

## Initial signal
CloudWatch high-memory alarm triggered for the EC2 API host.

## Immediate checks
- Verified memory usage with `free -m`
- Reviewed top processes with `top`
- Identified memory-heavy process with `ps aux --sort=-%mem`
- Confirmed service state with `systemctl status`
- Reviewed service logs with `journalctl`

## Key observations
- `stress-ng` consumed the highest memory during the test
- `voice-api` remained active and reachable
- `/health` endpoint continued to return healthy status
- No crash or service restart occurred during the test

## Technical interpretation
This was a host-resource pressure event rather than an application crash. The platform remained available, but the condition showed how sustained memory pressure could degrade service quality or lead to instability if not mitigated.