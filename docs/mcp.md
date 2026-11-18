# Connect an AI assistant

[README](../README.md) · [Tool methods](endpoints.md) · [MCP response envelope](responses.md#mcp-envelope)

## Dedicated hosted HTTP

Use `https://mcp.uptimescout.com/mcp` with Streamable HTTP and the private header `Authorization: Bearer YOUR_EVELODE_LICENSE_KEY`. The dedicated endpoint uses a UptimeScout license. It does not combine licenses for other products or provide the shared connector's OAuth flow.

Configure URL and header using your client's supported connection settings. Environment substitution in JSON headers is client-specific; do not assume a `${VARIABLE}` string will be expanded.

## Local stdio

Install Python 3.10+ and the bridge:

```sh
python -m pip install "git+https://github.com/jsonscraper/uptimescout-mcp-server.git@0.1.3"
export UPTIMESCOUT_LICENSE_KEY='your-license-key'
uptimescout-mcp
```

The bridge is a long-running stdin/stdout JSON-RPC process. An empty terminal is normal: it waits for the client to send messages. It connects to the hosted endpoint; it is not an offline data collector.

Example desktop configuration (replace the absolute executable path and placeholder key):

```json
{
  "mcpServers": {
    "uptimescout": {
      "command": "/absolute/path/to/uptimescout-mcp",
      "env": {"UPTIMESCOUT_LICENSE_KEY": "YOUR_EVELODE_LICENSE_KEY"}
    }
  }
}
```

Store client configuration privately. For a client that inherits environment variables, omit the `env` block and set the key outside the repository. Restart the client after changing configuration.

## Shared jsonscraper connector

For UptimeScout alongside independently licensed products, follow [jsonscraper MCP setup](https://jsonscraper.com/mcp#connect). Use the UptimeScout product's matching license field. The shared stdio connector uses `JSONSCRAPER_UPTIMESCOUT_LICENSE_KEY`; the dedicated Python bridge uses `UPTIMESCOUT_LICENSE_KEY`. They are different executables.

## Tools and workflow

The dedicated server exposes `uptimescout_services`, `uptimescout_status`, `uptimescout_statuses`, `uptimescout_summary`, `uptimescout_history`, `uptimescout_stats` and `uptimescout_incidents`.

1. Find catalog IDs with `uptimescout_services`.
2. Specify a region and request one status or a bounded batch.
3. Read freshness and observation time before interpreting the signal.
4. Request a bounded history window if needed.
5. Keep missing observations unknown.

For `uptimescout_statuses`, send `services` as a comma-separated string. The same successful-data-call accounting and plan limits apply to REST, SDK and MCP access.

## Troubleshooting

- **Command not found:** use the full path to the installed executable and verify the client uses the same Python environment.
- **Missing key:** set the variable in the desktop client's environment or private configuration, not only an unrelated terminal session.
- **Invalid license or rate limit:** inspect `isError`, error status and quota; avoid immediate retry loops.
- **No output in a terminal:** use an MCP client, or send the initialize / tools/list JSON-RPC messages shown in the MCP repository examples.
- **Unexpected healthy result:** inspect `service.status`, region, `observed_at` and `stale`; a successful API call does not imply normal availability.

Never place keys in tool arguments or prompts. Include only redacted diagnostics in bug reports.
