# PCI DSS Operational Controls

## Purpose

This document explains how the **CloudOps Incident Lab** is handled in a PCI-aware way without processing, storing, or transmitting real payment card data.

The aim is to show operational awareness relevant to a secure payment environment while keeping the lab safe, lightweight, and suitable for a public portfolio.

## Scope position

This project simulates operational patterns relevant to a secure payment context, but it does **not**:

- process real cardholder data
- connect to a live payment gateway
- handle real customer payment transactions
- store sensitive authentication data

The lab is therefore **PCI-aware in design thinking**, but it is **not a live PCI payment environment**.

## Core controls

### No real payment data

- no real PAN, CVV, expiry date, or cardholder data is used
- any transaction references in the lab are dummy identifiers only
- no voice recording or application log should contain sensitive payment data
- screenshots and documentation must not include real payment or customer-sensitive content

### Logging hygiene

- application and system logs must not contain cardholder data or sensitive authentication data
- logs should contain operational information only, such as service state, error patterns, alerting evidence, and recovery steps
- debug logging should be used carefully and only for operational troubleshooting
- log content included in the public repository should be reviewed before publication

### Access control

- access to the EC2 host, logs, and AWS console should be restricted to authorised users only
- SSH access should be limited to approved source IPs where possible
- least privilege should be used for AWS access and CloudWatch-related permissions
- operational access should be separated from public documentation wherever practical

### Secrets handling

- secrets must not be hardcoded in source code or committed into the repository
- credentials, tokens, and sensitive values should be stored outside code and injected securely in a real environment
- this lab avoids production secrets entirely
- any demo or placeholder values should be clearly non-production

### Change discipline

- configuration changes that affect availability, access, or monitoring should be tracked through a change record
- network changes, such as security group modifications, should be validated and reversible
- rollback thinking should be built into operational changes wherever possible

### Integrity and auditability

- operational work should leave a clear trail through Jira updates, incident records, change notes, and CloudWatch logs
- repository updates should reflect the final working state of the lab
- incident evidence should be structured enough to support review and follow-up

## Voice-platform note

If voice interactions were part of a real payment flow, recordings, transcripts, and logs would require strict controls to ensure that sensitive authentication data is not captured, retained, or exposed.

That is especially important in environments where voice channels interact with payment or identity workflows.

## Practical outcome

The project is designed to reflect **PCI-aware operational thinking** without introducing real payment-data handling risk.

This means the lab demonstrates:

- secure operational judgement
- logging discipline
- access-control awareness
- change control awareness
- audit-friendly documentation

without creating unnecessary exposure through real payment processing or real customer data.

## Related records

- [Main README](../README.md)
- [Monitoring README](../monitoring/README.md)
- [Incident documentation index](./incidents/README.md)
- [ITIL framework and operational process notes](./itil-framework/README.md)
- [Resilience design](./resilience-design.md)
- [Disaster recovery runbook](./disaster-recovery-runbook.md)