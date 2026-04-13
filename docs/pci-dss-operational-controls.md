# PCI DSS Operational Controls

## Purpose
This document explains how the CloudOps Incident Lab is handled in a PCI-aware way without processing or storing real payment card data.

## Scope position
This project simulates operational patterns relevant to a secure payment environment, but it does not process real cardholder data and does not connect to a live payment gateway.

## Core controls

### No real payment data
- No real PAN, CVV, expiry date, or cardholder data is used
- Any transaction references in the lab should be dummy identifiers only
- No voice recording or application log should contain sensitive payment data

### Logging hygiene
- Application and system logs must not contain cardholder or authentication data
- Logs should contain operational information only, such as service state, error patterns, and monitoring evidence
- Debug logging should be used carefully and only for operational troubleshooting

### Access control
- Access to the EC2 host, logs, and cloud console should be restricted to authorized users only
- SSH access should be limited to specific source IPs
- Least privilege should be used for AWS access and CloudWatch-related permissions

### Secrets handling
- Secrets must not be hardcoded in source code or committed into the repository
- Credentials, tokens, and sensitive values should be stored outside code and injected securely in a real environment
- This lab avoids production secrets entirely

### Change discipline
- Configuration changes that affect availability or access should be tracked through a change record
- Network changes, such as security group modifications, should be validated and reversible

### Integrity and auditability
- Operational work should leave a clear trail through Jira updates, incident records, change notes, and CloudWatch logs
- Repository updates should reflect the final working state of the lab

## Voice-platform note
If voice interactions were part of a real payment flow, recordings and logs would require strict controls to ensure that sensitive payment authentication data is not captured or retained.

## Practical outcome
The project is designed to reflect PCI-aware operational thinking without introducing real payment-data handling risk.