# Linux Troubleshooting Cheat Sheet

## Purpose
This document captures the main Linux commands used during incident triage in the CloudOps Incident Lab.

## Service state
- `sudo systemctl status voice-api --no-pager`
- `sudo journalctl -u voice-api -n 50 --no-pager`

## Memory and process checks
- `free -m`
- `top -b -n 1 | head -20`
- `ps aux --sort=-%mem | head -10`

## Network and port checks
- `ss -tulpn | grep 5000`
- `curl http://127.0.0.1:5000/health`

## How these were used in the incidents

### Incident 001 — Memory degradation
Used to confirm host memory pressure and verify that the service stayed active during the stress test.

### Incident 002 — Network blackhole
Used to confirm that the application was still healthy locally while external reachability failed due to security-group changes.

### Incident 003 — Voice dependency outage
Used to confirm that the platform remained healthy while the simulated dependency failure affected the voice-service layer.