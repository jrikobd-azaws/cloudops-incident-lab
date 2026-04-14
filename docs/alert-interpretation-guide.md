# Alert Interpretation Guide

## Purpose

This guide connects monitoring signals to their likely operational meaning, the most useful immediate checks, and the right escalation or response path.

The aim is to show that an alert is a **starting signal**, not the final diagnosis.

## Alert interpretation matrix

| Alert | Likely meaning | Immediate checks | Escalation / action |
|---|---|---|---|
| `COIL-App-HighMemory` | Host memory pressure may degrade service stability or responsiveness | `free -m`, `top -b -n 1 | head -20`, `ps aux --sort=-%mem | head -10`, `systemctl status voice-api`, `journalctl -u voice-api` | Escalate if memory pressure is sustained, if service stability declines, or if host risk remains unclear |
| `COIL-EC2-HighCPU` | CPU pressure may indicate process load, inefficient workload, or abnormal activity | EC2 metrics, `top`, service logs, recent workload or test activity | Investigate the top CPU consumer, assess service impact, and monitor the trend before deciding whether escalation is required |
| `COIL-EC2-StatusCheckFailed` | Underlying EC2 health issue or host-level failure condition | AWS instance checks, EC2 console status, SSH reachability, service availability | Treat as infrastructure risk and escalate quickly if host health or reachability is impaired |
| `COIL-App-SimulatedError` | Application emitted a known error pattern in logs | review log events, test `/health`, confirm current service state, confirm whether the error was intentionally triggered | Use as an application-error validation signal and confirm whether the event reflects controlled testing or a broader issue |

## Incident mapping

The alerts and operational scenarios in this lab map as follows:

- `COIL-App-HighMemory` -> [INC-001 Memory degradation on Linux API service](./incidents/INC-001-memory-degradation/incident-record.md)
- external reachability failure with healthy local service -> [INC-002 Network blackhole / security group issue](./incidents/INC-002-network-blackhole/incident-record.md)
- healthy platform with dependency-side voice failure -> [INC-003 Voice provider outage / simulated SIP dependency failure](./incidents/INC-003-voice-provider-outage/incident-record.md)

## Interpretation guidance

An alert is only the **starting point**.

Correct classification depends on checking:

- host health
- service state
- local versus external reachability
- dependency behaviour
- current business impact

This matters because the same visible symptom can belong to different fault domains.

For example:

- a service may be unreachable externally while still healthy on the host
- a platform may remain healthy while an upstream dependency causes service degradation
- a resource alarm may indicate risk before a full outage occurs

## Operational principle

Good alert handling means answering three questions quickly:

1. **What does the alert suggest?**
2. **What should be checked first?**
3. **What fault domain is most likely?**

Only after that should escalation or remediation be chosen.

## Related records

- [Main README](../README.md)
- [Monitoring README](../monitoring/README.md)
- [CloudWatch alarms](../monitoring/cloudwatch-alarms.md)
- [Alert scenarios](../monitoring/alert-scenarios.md)
- [Incident documentation index](./incidents/README.md)
- [Linux operations](../linux-ops/README.md)
- [ITIL framework and operational process notes](./itil-framework/README.md)