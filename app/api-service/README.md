# API Service

This is the small Linux-hosted service for the CloudOps Incident Lab.

## Purpose
- Provide a simple application to monitor in AWS
- Generate logs for CloudWatch and Linux triage
- Support incident simulation and health checks

## Endpoints
- `/` : basic service info
- `/health` : health check endpoint
- `/simulate-error` : returns HTTP 500 for testing

## Planned usage
This service will run on EC2 under systemd and be used for:
- CloudWatch monitoring
- Linux troubleshooting
- Incident scenarios such as memory degradation and connectivity issues
