# Alert Scenarios

## Incident 001 - Memory degradation
- Alarm: `COIL-App-HighMemory`
- Signal: `mem_used_percent`
- Meaning: host memory pressure may degrade performance or destabilize the service
- Immediate checks:
  - `free -m`
  - `top`
  - `ps aux --sort=-%mem`
  - `systemctl status voice-api`
  - `journalctl -u voice-api`

## Simulated application error validation
- Alarm: `COIL-App-SimulatedError`
- Source: metric filter on application log group
- Meaning: application emitted a known error pattern
- Use: validate log-based alerting path