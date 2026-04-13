# Alert Interpretation Guide

## Purpose
This guide connects monitoring signals to likely meaning, immediate checks, and escalation decisions.

| Alert | Likely meaning | Immediate checks | Escalation / action |
|---|---|---|---|
| `COIL-App-HighMemory` | Host memory pressure may degrade service stability | `free -m`, `top`, `ps aux --sort=-%mem`, `systemctl status voice-api`, `journalctl -u voice-api` | Escalate if sustained or if service stability declines |
| `COIL-EC2-HighCPU` | CPU pressure may indicate process load, inefficient workload, or abnormal activity | EC2 metrics, `top`, service logs, recent workload | Investigate process cause and monitor trend |
| `COIL-EC2-StatusCheckFailed` | Underlying EC2 health issue or host-level failure condition | AWS instance checks, console status, service availability | Treat as infrastructure risk and escalate quickly |
| `COIL-App-SimulatedError` | Application emitted a known error pattern in logs | Review log events, test `/health`, confirm current service state | Use as application error validation signal |

## Incident mapping
- `COIL-App-HighMemory` -> `INC-001`
- Reachability failure with healthy local service -> `INC-002`
- Healthy platform with dependency-side voice failure -> `INC-003`

## Guidance
An alert is only the starting point. Correct classification depends on checking host health, service state, network path, and dependencies before deciding on escalation.