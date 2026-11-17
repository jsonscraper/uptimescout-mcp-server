# UptimeScout MCP server

Cached regional service availability observations, explicit freshness and history.

## Install

```sh
python -m pip install "git+https://github.com/jsonscraper/uptimescout-mcp-server.git@0.1.1"
```

Run `UPTIMESCOUT_LICENSE_KEY=... uptimescout-mcp`, or connect your HTTP client to `https://mcp.uptimescout.com/mcp` with an Authorization Bearer header.

Purchase and manage licenses at [Evelode.com](https://evelode.com/downloads/uptimescout/). The same license works with REST, MCP and every SDK.

Methods: services, status, statuses, summary, history, stats, incidents. All calls read stored observations. No client call triggers collection. Check `stale`, `observed_at` and region. Signals are not guaranteed confirmed outages; sample ratios are not measured uptime. Missing intervals are unknown.

[OpenAPI](https://uptimescout.com/openapi.json) · [Website](https://uptimescout.com) · [Methods](docs/endpoints.md)

Monthly quotas reset on the first calendar day (UTC), including annual subscriptions. Successful data calls count as one request. History accumulates from launch.

MIT licensed.
