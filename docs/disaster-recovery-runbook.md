# Disaster Recovery Runbook

## Purpose

This runbook describes how to recover the **CloudOps Incident Lab** service if the primary EC2 host or the `voice-api` service becomes unavailable and normal recovery actions are no longer sufficient.

The goal is to show a practical manual recovery approach for a lightweight AWS-hosted platform.

## Trigger conditions

Use this runbook if one or more of the following apply:

- the EC2 instance becomes unavailable
- AWS status checks fail persistently
- the service cannot be restored through normal restart procedures
- the host is considered unrecoverable within a reasonable timeframe

## Preparation assumptions

This runbook assumes that:

- the GitHub repository contains the latest working source and documentation
- AWS account access is available
- SSH key access is available
- security group configuration is known
- the service can be redeployed from documented steps
- the `voice-api.service` unit file and Python dependencies are available in the repository

## Recovery steps

### 1. Assess scope

Before rebuilding, confirm the failure domain as clearly as possible.

- check whether the issue is host-level, application-level, or network-level
- review AWS instance state and status checks
- determine whether the service can be restored without rebuilding the instance
- confirm whether local restart or rollback actions have already failed

### 2. Launch replacement host if required

If the primary host is not recoverable, launch a replacement Ubuntu EC2 instance.

- launch a new EC2 Ubuntu instance
- apply the correct inbound rules for SSH and service validation
- attach the required IAM role for CloudWatch if monitoring is to be restored
- confirm basic instance reachability

### 3. Reinstall base packages

Prepare the replacement host for service deployment.

- install Python 3, `pip`, `git`, `curl`, and any required utilities
- create required directories such as `/opt/cloudops-incident-lab` and `/var/log/voice-api`
- confirm the environment is ready for application deployment

### 4. Restore application

Rebuild the application layer from the repository.

- clone the GitHub repository
- create the Python virtual environment
- install the Python requirements
- restore the `voice-api.service` unit file
- enable and start the service with `systemd`

### 5. Validate recovery

Confirm that service function has been restored.

- test `curl http://127.0.0.1:5000/health`
- test browser access to `http://PUBLIC_IP:5000/health`
- check `systemctl status voice-api`
- review recent logs with `journalctl`
- confirm the application is listening on port `5000`

### 6. Restore monitoring

Confirm that the replacement host is visible to the monitoring layer.

- confirm the CloudWatch agent is installed and running
- confirm the log group and metrics are flowing
- confirm alarms are visible and evaluating
- verify that expected host and application signals appear normally

## Rollback / failure handling

If recovery on the replacement host fails:

- stop and review service logs
- review permissions, path settings, and security group rules
- verify Python virtual environment and `systemd` configuration
- repeat validation after corrections
- escalate if the recovery path is blocked by AWS access, dependency issues, or unclear host state

## Recovery outcome

Recovery is considered successful when:

- the `voice-api` service is active under `systemd`
- the `/health` endpoint responds locally
- external validation succeeds where intended
- monitoring is visible again in CloudWatch
- the replacement host is stable enough for continued operation

## Documentation follow-up

After recovery:

- update the incident record or incident ticket
- record the recovery timeline and the actions taken
- note any improvements needed in resilience design, monitoring, or deployment guidance
- link any follow-up problem or change records if required

## Related records

- [Main README](../README.md)
- [Resilience design](./resilience-design.md)
- [Monitoring README](../monitoring/README.md)
- [API service README](../app/api-service/README.md)
- [Incident documentation index](./incidents/README.md)
- [ITIL framework and operational process notes](./itil-framework/README.md)