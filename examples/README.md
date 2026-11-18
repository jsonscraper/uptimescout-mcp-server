# Ready-to-run examples

[README](../README.md) · [Methods](../docs/endpoints.md) · [Response example](../docs/responses.md)

Each example makes one data call. Set `UPTIMESCOUT_LICENSE_KEY` privately first. Clone this repository and run commands from its root. `--help` makes no API call.

| Example | Run from repository root |
| --- | --- |
| [Search the service catalog](calls/services.json) | `Use `calls/services.json` after initialization` |
| [Read one regional signal](calls/status.json) | `Use `calls/status.json` after initialization` |
| [Check several services in one call](calls/statuses.json) | `Use `calls/statuses.json` after initialization` |
| [Summarize selected services](calls/summary.json) | `Use `calls/summary.json` after initialization` |
| [Read observation history](calls/history.json) | `Use `calls/history.json` after initialization` |
| [Inspect observation statistics](calls/stats.json) | `Use `calls/stats.json` after initialization` |
| [Find fresh elevated signals](calls/incidents.json) | `Use `calls/incidents.json` after initialization` |

## Inspect the hosted tool list without a data call

```sh
curl --request POST 'https://mcp.uptimescout.com/mcp' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json, text/event-stream' \
  --data @examples/initialize.json

curl --request POST 'https://mcp.uptimescout.com/mcp' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json, text/event-stream' \
  --data @examples/tools-list.json
```

These handshake/discovery calls do not request service data. Normal MCP clients perform initialization automatically. The dedicated endpoint accepts stateless POST messages and does not require a saved session ID.

## Execute one licensed data call

```sh
curl --request POST 'https://mcp.uptimescout.com/mcp' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json, text/event-stream' \
  --header "Authorization: Bearer $UPTIMESCOUT_LICENSE_KEY" \
  --data @examples/calls/status.json
```

This performs one `uptimescout_status` call. For another method, replace the JSON filename with a row above. Check top-level JSON-RPC `error` and `result.isError` before reading `result.structuredContent`.

## Local stdio discovery

```sh
printf '%s\n' \
  '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"uptimescout-example","version":"1.0.0"}}}' \
  '{"jsonrpc":"2.0","method":"notifications/initialized"}' \
  '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}' \
  | uptimescout-mcp
```

The bridge requires the key in its environment even for discovery. No service data is requested by this sequence. Use your actual MCP client for interactive requests and credential management.

## Workflow prompts

- “Compare GitHub's current signals in GB, DE and JP. Give the observation time for each and keep stale or missing signals unknown.”
- “Check GitHub and Cloudflare in GB in one batch. Summarize only fresh observations.”
- “Read the last 24 hours of GitHub observations in GB, one page first. Ask before retrieving more pages.”

[Connection guide](../docs/mcp.md) · [Response envelope](../docs/responses.md#mcp-envelope)

## Responses for every method

Public demonstration snapshots captured on **2026-11-18**. Each file includes its exact request arguments and complete response. These historical signals are examples, not current status claims. They contain no license key or customer usage fields.

| Method | Request and response JSON |
| --- | --- |
| `services` | [services.json](responses/services.json) |
| `status` | [status.json](responses/status.json) |
| `statuses` | [statuses.json](responses/statuses.json) |
| `summary` | [summary.json](responses/summary.json) |
| `history` | [history.json](responses/history.json) |
| `stats` | [stats.json](responses/stats.json) |
| `incidents` | [incidents.json](responses/incidents.json) |
