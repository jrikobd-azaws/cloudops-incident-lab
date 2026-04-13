# CloudWatch Alarms

## Configured alarms
- `COIL-EC2-StatusCheckFailed`
- `COIL-EC2-HighCPU`
- `COIL-App-HighMemory`
- `COIL-App-SimulatedError`

## Purpose
These alarms provide first-line operational visibility for EC2 health, host resource pressure, and application error conditions.

## Incident mapping
- `COIL-App-HighMemory` -> Incident 001
- `COIL-EC2-StatusCheckFailed` -> infrastructure health / future resilience scenarios
- `COIL-EC2-HighCPU` -> future performance scenarios
- `COIL-App-SimulatedError` -> log-based application error validation