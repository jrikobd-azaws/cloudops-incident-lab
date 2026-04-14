# Resilience Design

## Purpose

This document explains how resilience is considered in the **CloudOps Incident Lab**, even though the lab is intentionally lightweight.

The aim is not to claim full production-grade high availability. The aim is to show structured resilience thinking: how faults are detected, how recovery is approached, and how service continuity is supported through monitoring, documentation, and operational discipline.

## Current implementation

The current lab uses:

- one Ubuntu EC2 instance
- one API service running under `systemd`
- CloudWatch logs, metrics, and alarms
- Jira-based operational workflow
- documented incident response, escalation, and recovery procedures

## Current resilience posture

The lab is **not** a full high-availability platform.

It is a controlled single-instance environment designed to demonstrate:

- monitoring and alert interpretation
- first-line triage
- fault-domain assessment
- escalation and handover quality
- documented recovery thinking

This means the project is resilience-aware, but intentionally not overbuilt.

## What resilience means in this lab

Resilience in this project is demonstrated through:

- service supervision with `systemd`
- CloudWatch visibility for host and application signals
- documented handover and escalation process
- documented recovery steps
- controlled rollback for network-related failure scenarios
- clear separation between host failure, network failure, and dependency failure

In this lab, resilience is not just about redundancy. It is also about **detecting issues clearly, responding correctly, and recovering in a controlled way**.

## Warm-standby design concept

A future resilience enhancement could use:

- a secondary EC2 instance
- synchronised application deployment
- monitored recovery or failover process
- documented manual failover steps
- validation checks before traffic is considered restored

This would improve recovery posture while keeping the design understandable and operationally realistic for a small platform.

## Backup and recovery concept

A practical recovery approach for this lab would include:

- the repository as the source of truth for application and documentation
- instance rebuild from documented setup and deployment steps
- security group recreation from known-good settings
- service restart and validation using `/health`
- post-recovery monitoring review to confirm stable state

## RTO / RPO thinking

Because this is a portfolio lab, formal targets are illustrative rather than contractual.

- **Example RTO:** 15 to 30 minutes for service rebuild and validation
- **Example RPO:** low, because persistent transactional data is not central to this lab design

The main value here is to show that recovery expectations have been considered, even in a lightweight environment.

## Design trade-off

The lab prioritises **operational clarity over full HA complexity**.

The goal is to demonstrate how to:

- detect faults
- classify fault domains correctly
- recover in a controlled way
- communicate status clearly
- document lessons and follow-up actions

It is intentionally designed to show platform-operations judgement rather than large-scale infrastructure engineering.

## Related records

- [Main README](../README.md)
- [Monitoring README](../monitoring/README.md)
- [API service README](../app/api-service/README.md)
- [Incident documentation index](./incidents/README.md)
- [ITIL framework and operational process notes](./itil-framework/README.md)
- [Disaster recovery runbook](./disaster-recovery-runbook.md)