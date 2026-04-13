# CloudOps Incident Lab

A simulated AWS-hosted voice/payment operations lab focused on monitoring, incident triage, Linux support, Jira-style service management, escalation, handover, and resilience design.

## Planned core incidents
- INC-001: Memory degradation on Linux app service
- INC-002: Network blackhole / security group issue
- INC-003: Voice provider / SIP outage

## Why this project uses a Voice API instead of a full telephony platform

This project is intentionally scoped as an operations-first lab rather than a full PBX or contact-centre build. The goal is to demonstrate platform operations skills that align with the target role: AWS monitoring, Linux triage, alert interpretation, structured incident handling, Jira-style workflow, handovers, and resilience thinking.

A lightweight API service provides a realistic operational anchor for:
- host-level incidents such as memory pressure,
- network reachability failures,
- service health validation,
- and “platform up, service degraded” scenarios when a simulated voice dependency fails.

This approach keeps the project finishable and interview-defendable while still reflecting real voice-platform operational patterns.

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
