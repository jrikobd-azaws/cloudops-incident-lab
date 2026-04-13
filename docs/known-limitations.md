# Known Limitations

## Purpose
This document states the main simplifications and boundaries of the CloudOps Incident Lab.

## Current limitations

### Single-instance design
The lab currently runs on a single EC2 instance. It demonstrates operations, monitoring, and recovery thinking, but it is not a full HA service.

### Simulated dependency outage
The voice-provider outage scenario is simulated through controlled logs and dependency-failure patterns rather than a live upstream provider integration.

### Lightweight application scope
The API service is intentionally simple. It exists to support operational scenarios such as:
- memory degradation
- network reachability failure
- dependency-side degradation

### No real payment processing
The project is PCI-aware in its operational controls, but it does not process real cardholder data or integrate with a real payment gateway.

### Limited automated recovery
The project emphasizes detection, triage, and documented recovery rather than automated failover orchestration.

### Monitoring scope
CloudWatch monitoring is implemented for the needs of the lab, but not every possible signal or synthetic check is present.

## Why these limitations are acceptable
The project is designed as an operations-first portfolio lab. The priority is to demonstrate:
- monitoring interpretation
- Linux and AWS troubleshooting
- structured incident handling
- escalation and handover quality
- resilience thinking

rather than full enterprise-scale implementation.
