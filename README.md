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

## How the API links to the core incidents

- Incident 001 — Memory degradation:
  the API runs on the monitored EC2 host and provides a real process/service to stress and troubleshoot.

- Incident 002 — Network blackhole:
  the API exposes a real endpoint on port 5000 that can be made unreachable through security-group changes while the host remains otherwise healthy.

- Incident 003 — Voice provider outage:
  the API remains up while the simulated voice dependency fails, representing the “platform up, service degraded” operational pattern common in voice environments.
  
## Current status

- EC2 Ubuntu instance deployed in AWS
- API service running under `systemd`
- CloudWatch logs, metrics, and alarms configured
- Incident 001 (memory degradation) completed and validated
- Incident 002 (memory degradation) completed and validated
- Incident 003 (memory degradation) completed and validated

## Monitoring implemented

- `COIL-EC2-StatusCheckFailed`
- `COIL-EC2-HighCPU`
- `COIL-App-HighMemory`
- `COIL-App-SimulatedError`

## Project management approach

This project was planned and tracked in Jira using epics, tasks, subtasks, incidents, and change records. That structure was used to manage implementation across AWS setup, monitoring, incident scenarios, and documentation rather than treating the project as a one-off demo build.

![Jira project tracking overview](assets/screenshots/jira/jira-project-tracking-overview.png)