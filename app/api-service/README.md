# API Service

This folder contains the lightweight Flask-based API used as the live application layer for the **CloudOps Incident Lab**.

The service is intentionally simple. Its purpose is not to showcase application complexity, but to provide a real EC2-hosted service that can be monitored, managed with `systemd`, validated through HTTP endpoints, and used to demonstrate realistic platform-operations incident scenarios.

## Why this service exists

The wider project is focused on **cloud/platform operations**, not full application development.

This API gives the lab a practical operational anchor for:

- Linux service management
- CloudWatch-based monitoring
- endpoint validation
- incident detection and triage
- recovery testing
- demonstrating the difference between host health, service health, and dependency health

A small service is enough to show operational ownership clearly, without diluting the project with unnecessary application complexity.

## Service overview

The API runs on an Ubuntu EC2 instance, is managed with `systemd`, and exposes a small set of HTTP endpoints for validation and controlled incident simulation.

![API service overview](../../assets/screenshots/architecture/api-service-overview.png)

This design keeps the service easy to understand while still making it useful for monitoring, triage, and incident documentation.

## Real EC2 deployment evidence

This project uses a real AWS EC2 instance as the application host rather than a purely local simulation.

![EC2 instance running with active SSH session](../../assets/screenshots/aws-ec2-ubuntu/aws-ec2-01-instance-running-and-ssh-session.png)

This helps show that the service was deployed and tested in an actual AWS-hosted Linux environment.

## What the service does

The API exposes a few simple endpoints that support service validation and controlled error generation.

| Endpoint | Purpose |
|---|---|
| `/` | Returns a basic service status response |
| `/health` | Returns a health-check response for validation and monitoring |
| `/simulate-error` | Returns a controlled HTTP 500 response for testing alerting and triage behaviour |

## How it supports the incident lab

This service is the operational anchor for the three main incident scenarios documented in the repository.

### INC-001 — Memory degradation on the app host
The API represents the monitored application running on the Linux host. This supports memory-related alerting, service checks, and host-level triage.

### INC-002 — Network blackhole / security group issue
The API helps demonstrate a key operations concept: the application can still be healthy on the instance while becoming unreachable externally because of network controls.

### INC-003 — Voice provider dependency outage
The API remains available while an upstream voice-related dependency is degraded. This helps model the “platform up, service degraded” pattern that matters in voice and telecom operations.

## Deployment model

The service is deployed on Ubuntu EC2 with a Python virtual environment and managed using a `systemd` unit.

Key characteristics of the deployment:

- Ubuntu EC2 host
- repository deployed under `/opt/cloudops-incident-lab`
- Python virtual environment stored under `.venv`
- Flask app listening on port `5000`
- `systemd` used for service control and restart behaviour

The service unit used in this folder reflects the actual deployment pattern used in the lab.

## Quick validation commands

The following checks were used to validate that the service was running correctly on EC2:

```bash
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/health
curl -i http://127.0.0.1:5000/simulate-error
systemctl status voice-api --no-pager