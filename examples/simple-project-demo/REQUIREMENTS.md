# Telemetry Widget Requirements

> Functional and non-functional requirements for the Telemetry Widget demonstration project.

---

## Functional Requirements
1. **Metric Ingestion**: Accept real-time system metrics (CPU, Memory, Disk) over a REST endpoint.
2. **Dashboard Display**: Render widget cards with current utilization and historical sparklines.
3. **Threshold Alerts**: Highlight values exceeding configurable thresholds in warning/critical colors.

---

## Non-Functional Requirements
- **Performance**: Render updates within 100ms of ingestion.
- **Portability**: Run cleanly in containerized and local developer environments.
- **Test Coverage**: Maintain >= 80% unit test coverage for calculation logic.
