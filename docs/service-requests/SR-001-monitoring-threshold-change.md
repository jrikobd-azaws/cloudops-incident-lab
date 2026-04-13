# SR-001 Monitoring threshold change

## Request summary
Request to review and update monitoring threshold guidance for the CloudOps Incident Lab after validating the high-memory incident scenario.

## Request type
Service Request

## Reason
Incident 001 demonstrated how quickly host memory pressure can rise on a small EC2 instance. Threshold review is requested to ensure that alerting remains useful without creating excessive noise.

## Requested action
- Review the current `COIL-App-HighMemory` threshold
- Confirm whether the current evaluation window is appropriate
- Document any threshold adjustment decision
- Ensure alert interpretation guidance remains aligned with the chosen setting

## Related records
- `INC-001 Memory degradation on Linux API service`
- `PRB-001 Recurring memory growth`

## Outcome guidance
This request should result in either:
- no threshold change, with justification
or
- a documented threshold adjustment and monitoring note update