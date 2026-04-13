# CloudOps Incident Lab

A focused AWS-hosted operations portfolio project demonstrating monitoring, incident triage, Linux support, Jira-style service management, escalation, and structured operational documentation in a voice/payment context.

## Current status

This public portfolio version is focused on the EC2-hosted application, monitoring, incident evidence, and operational documentation.

Completed incident scenarios in the repository:

- **INC-001 — Memory degradation on the app host**
- **INC-002 — Network blackhole / security group issue**
- **INC-003 — Voice provider dependency outage**

The goal of the project is to show operational judgment: alert interpretation, Linux triage, service recovery, structured incident handling, escalation quality, and clear stakeholder communication.

## Architecture overview

This lab is built around a lightweight EC2-hosted application that can be monitored, tested, and used as the operational anchor for realistic incident scenarios.

![CloudOps Incident Lab architecture overview](assets/screenshots/architecture/cloudops-incident-lab-overview.png)

The design is intentionally simple: it makes the monitoring, triage, recovery, and incident-management flow easy to understand without hiding the operational value behind unnecessary platform complexity.

## What is real vs simulated

This project is built as an **operations-first AWS lab**.

### Real in the lab
- An EC2-hosted Ubuntu environment
- A Flask-based Voice API service
- `systemd` service management
- CloudWatch monitoring and alarm configuration
- Linux diagnostics and service-level checks
- Jira-style incident tracking and structured documentation

### Simulated for the portfolio
- Selected incident triggers and dependency failures
- Voice-provider outage behaviour used to model telecom-style escalation
- Controlled failure scenarios used to demonstrate realistic incident handling without building a full public PBX platform

The incident scenarios are designed to reflect real operational patterns: host-level resource degradation, externally visible network failure despite local service health, and upstream dependency failure while the core platform remains available.

## Public repo scope

This public repository intentionally focuses on the parts of the project most relevant to a Platform Operations / Cloud Operations role:

- EC2-hosted application operations
- monitoring and alert interpretation
- incident documentation and recovery evidence
- Jira-style structured delivery
- Linux and service-level troubleshooting

Heavier infrastructure build-out and full telephony platform implementation are intentionally not the focus of this public version. The aim is to demonstrate operational ownership and incident handling rather than unnecessary platform sprawl.

## Why this project uses a Voice API instead of a full telephony platform

This project is intentionally scoped as an operations-first lab rather than a full PBX or contact-centre build.

The target role is centred on:
- AWS monitoring
- Linux triage
- alert interpretation
- incident ownership
- escalation discipline
- handovers
- resilience thinking
- clear operational communication

A lightweight API service provides a practical operational anchor for:
- host-level issues such as memory pressure
- endpoint reachability failures
- service health validation
- “platform up, service degraded” scenarios when a voice dependency fails

This approach keeps the project finishable, defensible in interview, and closely aligned to platform operations responsibilities.

## Core incidents

### INC-001 — Memory degradation on the app host
This scenario demonstrates how rising memory usage affects service health, how CloudWatch alarms support early detection, and how Linux triage is used to confirm impact and recovery steps.

### INC-002 — Network blackhole / security group issue
This scenario demonstrates the difference between local host health and external service availability. The application can still be healthy on the instance while becoming unreachable due to network controls.

### INC-003 — Voice provider dependency outage
This scenario demonstrates an important voice-operations pattern: the platform remains up, but service is degraded because an upstream dependency is failing. This supports vendor escalation, impact assessment, and stakeholder communication.

## Monitoring overview

CloudWatch is the primary monitoring layer for this lab. It is used to detect service-impacting conditions early, support first-line triage, and provide evidence for the incident workflow documented in the repository.

The monitoring setup includes four core alarm types:

- **`COIL-EC2-StatusCheckFailed`**  
  Confirms whether the underlying EC2 instance is healthy at the infrastructure level.

- **`COIL-EC2-HighCPU`**  
  Highlights sustained CPU pressure that may indicate contention, degraded response times, or abnormal process behaviour.

- **`COIL-App-HighMemory`**  
  Supports detection of memory growth and service degradation on the application host.

- **`COIL-App-SimulatedError`**  
  Captures simulated application error activity so incidents can be detected and investigated in an operationally realistic way.

## Monitoring in action

The lab includes CloudWatch alarms for host health, CPU pressure, high memory, and application error activity.

![Configured CloudWatch alarms](assets/screenshots/cloudwatch-alarms/06-configured-4-alarms.png)

This monitoring layer supports the incident scenarios documented later in the repository.

## Structured delivery and incident management

This project was planned and tracked using a Jira-style workflow to reflect the operational discipline expected in production support environments.

The Jira evidence is included to show that the project was not just built technically, but also managed in a structured way: scoped work, tracked progress, documented incident-related deliverables, and maintained a clear delivery path aligned to operational outcomes.

![Jira project tracking overview](assets/screenshots/jira/jira-project-tracking-overview.png)

This supports the service-management side of the portfolio, which is especially relevant for roles that expect strong Jira Service Management usage alongside technical triage.

## Repository guide

### Application
- `app/api-service/` — Flask-based Voice API service, dependencies, and service unit

### Monitoring
- `monitoring/cloudwatch-alarms.md` — alarm coverage and purpose
- `monitoring/alert-scenarios.md` — operational meaning of alerts and immediate checks

### Linux operations
- `linux-ops/` — service checks, diagnostics, and operational support material

### Incident documentation
- `docs/incidents/INC-001-memory-degradation/`
- `docs/incidents/INC-002-network-blackhole/`
- `docs/incidents/INC-003-voice-provider-outage/`

### Linked operational records
- `docs/problem-records/`
- `docs/change-records/`
- `docs/service-requests/`
- `docs/itil-framework/`

## Incident evidence

Each incident folder contains structured operational evidence such as:

- incident record
- triage notes
- handover note
- stakeholder update
- linked problem, change, or escalation records where relevant
- screenshots showing alarm state, failure condition, recovery state, and Jira tracking

## Why this project fits platform operations roles

This repository is intended to demonstrate the kind of work expected in cloud/platform operations environments:

- monitoring and alert interpretation
- calm first-line triage
- Linux service troubleshooting
- distinguishing host health from service health
- managing incidents in a structured lifecycle
- escalating dependencies clearly
- documenting actions, outcomes, and lessons learned

## Next reading path

A recruiter or hiring manager can review the project in this order:

1. This README for the overview
2. `monitoring/cloudwatch-alarms.md`
3. `docs/incidents/INC-001-memory-degradation/incident-record.md`
4. `docs/incidents/INC-002-network-blackhole/incident-record.md`
5. `docs/incidents/INC-003-voice-provider-outage/incident-record.md`

## Note on screenshots

The README uses only a small number of overview screenshots. Detailed evidence for each incident is kept inside the incident documentation so the main page stays readable while still preserving operational proof.