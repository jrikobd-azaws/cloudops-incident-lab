# Triage Notes - INC-003

## Initial signal
Voice-service degradation was simulated through provider-style SIP failure patterns, including registration failures and `503 Service Unavailable` responses.

## Immediate checks
- Reviewed voice dependency log output
- Checked for `503`, registration failure, and call-establishment failure patterns
- Validated local platform health with `curl http://127.0.0.1:5000/health`
- Confirmed `voice-api` remained active using `systemctl status`

## Key observations
- Repeated provider-style registration failures were present
- Upstream `503 Service Unavailable` messages were visible
- Outbound call-establishment failure was visible in the simulated logs
- The EC2 host remained healthy
- The `voice-api` service remained active
- The `/health` endpoint continued to return healthy responses

## Fault-domain assessment
This was a dependency/service-layer failure, not a host, operating system, or local application outage. The correct fault domain was the upstream voice-provider path.

## Why this mattered
The incident demonstrates why operations teams must avoid treating every degraded service event as a server failure. In this case, local platform health checks showed that restarting the service would not have addressed the dependency issue.