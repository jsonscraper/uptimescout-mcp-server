# UptimeScout MCP server

Regional service availability observations, explicit freshness and history.

## Install

```sh
python -m pip install "git+https://github.com/jsonscraper/uptimescout-mcp-server.git@0.1.3"
```

Run `UPTIMESCOUT_LICENSE_KEY=... uptimescout-mcp`, or connect your HTTP client to `https://mcp.uptimescout.com/mcp` with an Authorization Bearer header.

Purchase and manage licenses at [Evelode.com](https://evelode.com/downloads/uptimescout/). The same license works with REST, MCP and every SDK.

Methods: services, status, statuses, summary, history, stats, incidents. Statuses include observation time, region and freshness. Check `stale`, `observed_at` and region. Signals are not guaranteed confirmed outages; sample ratios are not measured uptime. Missing intervals are unknown.

[OpenAPI](https://uptimescout.com/openapi.json) · [Website](https://uptimescout.com) · [Methods](docs/endpoints.md)

Request usage resets on license renewal or plan change, never on a calendar boundary. Annual plans provide twelve monthly allowances as one pool for the full license term. Successful data calls count as one request. History accumulates from launch.

MIT licensed.

Request rates (60-second windows): Free 60/min, Starter 300/min, Builder 600/min, Pro 1,800/min, Scale 3,600/min. Annual plans use the same rates. Inspect `limits_info.rate_limit` and `limits_info.rate_limit_window_seconds`; respect HTTP 429 and `Retry-After`. Prices and license-period request allowances are unchanged.

Regional selection, localized service descriptions and versioned logo URLs are supported by all seven methods. See [the endpoint reference](docs/endpoints.md#regional-observations-and-localized-metadata).
