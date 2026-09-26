# Requirements

**NOTE**: This document is for human reference only. Agents should not use this.

User Story

### Description

As a ...
I want to ...
So that ...

### Acceptance Criteria

in a .feature file

Feature: F

  Scenario: S1
    When ...
    Then ...

  Scenario: S2
    Given ...
    When ...
    Then ...

### Technical Details

Actor:
- User
- Agent
- Message
- Timer

Trigger:
- Synchronous Request/Response
  - REST
  - GraphQL
- Asynchronous Message-Driven
  - Fire And Forget Event Notification
  - Command/Reply
  - Task/ACK
  - Poll

### EARS

- **Ubiquitous**:   The <system> shall <response>
- **Event-Driven**: When <trigger>, the <system> shall <response>
- **State-Driven**: While <state>, the <system> shall <response>
- **Unwanted Behavior**: If <condition>, then the <system> shall <response>
- **Optional**: Where <feature is included/present/enabled/active>, the <system> shall <response>
- **Extended**: While <state>, when <trigger>, the <system> shall <response>

### Types Of System Requirements

#### Build

- **Product Manager's System Requirements**: Basic list of required features, optional features, unwanted behavior.
- **Enterprise Architect's Requirements**: Company-wide design policies designed to birth and nourish the PM's vision.
  - list all internal systems used
  - list all external vendors used
    - name, link
    - business contact
    - technical contact
    - emergency contact
- **Solutions Architect's Requirements**: Design decisions and policies that align multiple applications within and between systems, under the EA.
  - use cases
  - mind map
  - work breakdown structure
  - activity
  - sequence
  - class
  - data
  - state
  - deployment
- **Application Architect's Requirements**: Application-specific design decisions, including meta policies by application type, under the SA.
  - input data model
  - output data model + HTTP response status code
  - exceptions + HTTP response status code
- **Messaging Requirements**: Define data models, topics, queues following patterns established by SA and DBA.
  - incoming queue, input data model
  - outgoing topic, output data model
- **Scheduled Task Requirements**:
  - time (in UTC!)
  - task
- **Data Storage Requirements**: How and where to store data and in what format. Defined by the DBA, SA, and AA.
- **Data Residency Requirements**: Legal/geo-political requirements governing where data is collected, processed, and stored. Defined by the PM and DBA.
- **Data Sovereignty Requirements**: Legal/geo-political requirements describing whose laws govern the data. Defined by the PM and DBA.
- **Privacy Requirements**: Define what data is PII, where stored, for how long, and how to view/change/remove it. Defined by SA, DBA, and PM.
- **Personalization Requirements**: Defines what pieces of data can be abstracted into configurable options for users. Defined by the PM.
- **Data Retention Requirements**: Define how long to keep data live or archived. How to archive, how to delete. Defined by the PM and DBA.
- **Decommissioning Requirements**: What to deactivate, uninstall, or delete, and in what order, when this is no longer needed. Defined by the SA.
- **Performance Requirements**: Specify minimum TPS, max queue length, etc. Defined by SA and SREs with input from PM.
- **Security Requirements**: Who can access what data, who can issue what commands. Defined by the Security Officer with input from the PM and AA.
- **Compliance Requirements**: Note anything required for GDPR, SOC-2, ISO27001, HIPAA, HITRUST, PCI DSS, etc. Definied by the Security Officer.
- **Testing Requirements**: Unit, functional, security, performance, edge cases, convergence, chaos. Defined by DEV, QA, SA based on all of the above.

#### Run

- **Deployment Requirements**: Packaging format, deployment/upgrade/decommission scripts. Developed by SREs.
- **Infrastructure Monitoring Requirements**: Monitor node and service uptime, CPU, memory, and filesystem usage. Defined by SREs.
- **Partner Monitoring**: Monitor uptime of all external system dependencies. Defined by SREs with input from DEV, QA, SA.
- **Technical Performance Requirements**: Monitor service uptime, logs/metrics/traces/alerts, etc. Defined by SREs.
- **Event Monitoring Requirements**: Periodic scans of recent data to discover hidden meta events.
- **Scalability Requirements**: Define the rules for scaling components. Defined by SREs with input from PM.
- **GEO Failover Requirements**: Define the rules for failover to alternate facilities in the event of an emergency. Defined by SREs with input from PM.
- **Business Monitoring Requirements**: Define business metrics for live data and scheduled reports.
- **Operational Requirements**: Routine maintenance tasks.
