# CloudOps Incident Lab

A simulated AWS-hosted voice/payment operations lab focused on monitoring, incident triage, Linux support, Jira-style service management, escalation, handover, and resilience design.

## Planned core incidents
- INC-001: Memory degradation on Linux app service
- INC-002: Network blackhole / security group issue
- INC-003: Voice provider / SIP outage

## Current status

- EC2 Ubuntu instance deployed in AWS
- API service running under `systemd`
- CloudWatch logs, metrics, and alarms configured
- Incident 001 (memory degradation) completed and validated

## Monitoring implemented

- `COIL-EC2-StatusCheckFailed`
- `COIL-EC2-HighCPU`
- `COIL-App-HighMemory`
- `COIL-App-SimulatedError`
