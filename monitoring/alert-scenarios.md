# Alert Scenarios

This file explains what each core CloudWatch alarm means operationally and what first-line checks make sense when it triggers.

It is written from the perspective of a Platform Operations analyst performing initial triage.

For the alarm configuration itself, see [`cloudwatch-alarms.md`](./cloudwatch-alarms.md).

## 1. `COIL-EC2-StatusCheckFailed`

### Operational meaning
This is an infrastructure-level EC2 health signal.

It suggests that the instance may be impaired at the platform or host level, which could affect reachability or service continuity even before deeper application investigation begins.

### Likely impact
- service may become unavailable
- SSH access may fail
- the application may stop responding even if no recent application deployment occurred

### Immediate checks
- check EC2 instance state in the AWS console
- review instance status checks
- confirm whether the host is reachable
- verify whether the API endpoint still responds
- review recent host or platform changes

### Triage focus
Start with infrastructure health first. Do not assume the issue is application-specific until host reachability is understood.

## 2. `COIL-EC2-HighCPU`

### Operational meaning
This alarm indicates sustained CPU pressure on the EC2 instance.

It may reflect process contention, abnormal workload, or degraded response times.

### Likely impact
- slower API responses
- elevated latency
- reduced host headroom
- possible knock-on service instability if CPU pressure continues

### Immediate checks
- `top`
- `ps aux --sort=-%cpu | head`
- `uptime`
- `systemctl status voice-api`
- `journalctl -u voice-api --no-pager | tail -n 50`

### Triage focus
Confirm whether CPU pressure is affecting the application directly or whether it is only a transient host-level spike.

## 3. `COIL-App-HighMemory`

### Operational meaning
This alarm indicates elevated memory usage on the application host using the CloudWatch Agent custom metric `mem_used_percent`.

This is the primary monitoring signal for **INC-001**.

### Likely impact
- degraded application performance
- increased risk of process instability
- reduced host capacity for sustained service operation

### Immediate checks
- `free -m`
- `top`
- `ps aux --sort=-%mem | head`
- `systemctl status voice-api`
- `journalctl -u voice-api --no-pager | tail -n 50`

### Triage focus
Determine whether memory growth is transient, workload-related, or suggestive of recurring application/resource pressure.

## 4. `COIL-App-SimulatedError`

### Operational meaning
This is an application-level alarm derived from CloudWatch Logs using a metric filter.

It triggers when the known log message:

```text
Simulated application error triggered
