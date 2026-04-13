# Disaster Recovery Runbook

## Purpose
This runbook describes how to recover the CloudOps Incident Lab service if the primary EC2 host or service becomes unavailable.

## Trigger conditions
Use this runbook if:
- the EC2 instance becomes unavailable
- AWS status checks fail persistently
- the service cannot be restored through normal restart procedures
- the host is considered unrecoverable in a reasonable timeframe

## Preparation assumptions
- The GitHub repository contains the latest working source and documentation
- AWS account access is available
- SSH key access is available
- Security group configuration is known
- The service can be redeployed from documented steps

## Recovery steps

### 1. Assess scope
- Confirm whether the issue is host-level, application-level, or network-level
- Check AWS instance state and status checks
- Confirm whether the service is recoverable without rebuild

### 2. Launch replacement host if required
- Launch a new EC2 Ubuntu instance
- Apply the correct inbound rules for SSH and service testing
- Attach any required IAM role for CloudWatch

### 3. Reinstall base packages
- Install Python 3, pip, git, curl, and any required tools
- Create required directories such as `/opt/cloudops-incident-lab` and `/var/log/voice-api`

### 4. Restore application
- Clone the GitHub repository
- Create the Python virtual environment
- Install requirements
- restore the `voice-api.service` unit file
- enable and start the service

### 5. Validate recovery
- test `curl http://127.0.0.1:5000/health`
- test browser access to `http://PUBLIC_IP:5000/health`
- check `systemctl status voice-api`
- check recent logs with `journalctl`

### 6. Restore monitoring
- confirm CloudWatch agent is installed and running
- confirm log group and metrics are flowing
- confirm alarms are visible and evaluating

## Rollback / failure handling
If recovery on the replacement host fails:
- stop and review service logs
- review permissions, path settings, and security group rules
- verify virtual environment and systemd configuration
- repeat validation after corrections

## Documentation follow-up
After recovery:
- update the incident ticket
- record timeline and recovery steps
- note any improvements needed in resilience design or monitoring