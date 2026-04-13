## How the API links to the core incidents

- Incident 001 — Memory degradation:
  the API runs on the monitored EC2 host and provides a real process/service to stress and troubleshoot.

- Incident 002 — Network blackhole:
  the API exposes a real endpoint on port 5000 that can be made unreachable through security-group changes while the host remains otherwise healthy.

- Incident 003 — Voice provider outage:
  the API remains up while the simulated voice dependency fails, representing the “platform up, service degraded” operational pattern common in voice environments.