# INC-001 Memory degradation on Linux API service

## Summary
Controlled memory pressure was generated on the EC2-hosted API service to validate CloudWatch high-memory alerting and Linux triage workflow.

## Detection
- Monitoring source: CloudWatch
- Alarm: `COIL-App-HighMemory`
- Metric: `mem_used_percent`
- Threshold: `>= 80 for 2 datapoints within 3 minutes`

## Impact
- Service remained reachable
- Risk of degraded performance and service instability was demonstrated
- Purpose was to validate monitoring and operational response

## Environment
- Host: EC2 Ubuntu instance
- Service: `voice-api`
- Service manager: `systemd`
- Endpoint: `/health`

## Timeline
- Memory stress started using `stress-ng`
- CloudWatch high-memory alarm entered `ALARM`
- Linux triage commands executed
- Health endpoint remained available
- Alarm returned to `OK` after memory pressure ended

## Commands used
- `stress-ng --vm 1 --vm-bytes 700M --timeout 4m`
- `free -m`
- `top -b -n 1 | head -20`
- `ps aux --sort=-%mem | head -10`
- `sudo systemctl status voice-api --no-pager`
- `sudo journalctl -u voice-api -n 50 --no-pager`

## Outcome
The incident successfully validated memory-based detection, alarm state transition, Linux triage workflow, and service continuity checks.

## Linked records
- Problem record: `PRB-001-recurring-memory-growth`
- Jira issue: `INC-001 Memory degradation on Linux API service`