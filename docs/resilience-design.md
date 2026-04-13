# Resilience Design

## Purpose
This document explains how resilience is considered in the CloudOps Incident Lab, even though the lab is intentionally lightweight.

## Current implementation
The current lab uses:
- one EC2 Ubuntu instance
- one API service running under `systemd`
- CloudWatch logs, metrics, and alarms
- Jira-based operational workflow
- documented incident response and recovery procedures

## Current resilience posture
The lab is not a full high-availability platform. It is a controlled single-instance environment designed to demonstrate monitoring, triage, escalation, and recovery thinking.

## What resilience means in this lab
Resilience in this project is demonstrated through:
- service supervision with `systemd`
- CloudWatch visibility for host and application signals
- documented handover and escalation process
- documented recovery steps
- controlled rollback for network-related failure scenarios
- clear separation between host failure, network failure, and dependency failure

## Warm-standby design concept
A future resilience enhancement could use:
- a secondary EC2 instance
- synchronized application deployment
- monitored recovery/failover process
- documented manual failover steps

## Backup and recovery concept
A practical recovery approach for this lab would include:
- repository as source of truth for application and documentation
- instance rebuild from documented steps
- security group recreation from known-good settings
- service restart and validation using `/health`

## RTO / RPO thinking
Because this is a portfolio lab, formal targets are illustrative:
- Example RTO: 15 to 30 minutes for service rebuild and recovery
- Example RPO: low, because persistent transactional data is not central to this lab design

## Design tradeoff
The lab prioritizes operational clarity over full HA complexity. The goal is to demonstrate how to detect, classify, and recover from faults, not to build a large production cluster.