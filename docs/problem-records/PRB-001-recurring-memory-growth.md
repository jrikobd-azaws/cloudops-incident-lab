# PRB-001 Recurring memory growth

## Problem statement
The Linux API host is vulnerable to elevated memory utilization conditions that could degrade service performance or stability if sustained.

## Related incident
- `INC-001 Memory degradation on Linux API service`

## Evidence
- CloudWatch memory alarm entered `ALARM`
- `stress-ng` demonstrated how quickly host memory pressure can rise on a small EC2 instance
- Linux diagnostics confirmed the host-level nature of the event

## Root cause category
Host resource pressure / memory saturation scenario

## Recommended follow-up
- Create a runbook for high-memory triage
- Review memory thresholds and alarm tuning
- Consider service-level protection or scaling improvements
- Add controlled memory test guidance to documentation