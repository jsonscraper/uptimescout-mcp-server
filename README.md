# UptimeScout MCP Server

[![Latest release](https://img.shields.io/github/v/tag/jsonscraper/uptimescout-mcp-server?label=release&style=flat-square)](https://github.com/jsonscraper/uptimescout-mcp-server/tags)
[![Runtime](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white&style=flat-square)](#quick-start)
[![Last commit](https://img.shields.io/github/last-commit/jsonscraper/uptimescout-mcp-server?style=flat-square)](https://github.com/jsonscraper/uptimescout-mcp-server/commits)
[![MIT license](https://img.shields.io/github/license/jsonscraper/uptimescout-mcp-server?style=flat-square)](LICENSE)

Connect AI assistants to regional service availability, observation history and disruption signals through seven read-only MCP tools.

**Package:** `uptimescout-mcp` · **[Quick start](#quick-start)** · **[Methods](#main-methods)** · **[Examples](examples/README.md)** · **[Integration guide](docs/guide.md)**

<picture>
  <source media="(max-width: 640px) and (prefers-color-scheme: dark)" srcset="docs/quickstart-mobile-dark.svg">
  <source media="(max-width: 640px)" srcset="docs/quickstart-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="docs/quickstart-dark.svg">
  <img src="docs/quickstart.svg" alt="UptimeScout: API key, region, service signal and observation history" width="880">
</picture>

## Quick start

**1. Get an API key.** Compare the [Free trial and paid plans](https://jsonscraper.com/services/uptimescout-api?utm_source=github&utm_medium=sdk&utm_campaign=uptimescout-mcp-server&utm_content=readme#pricing). Licenses are sold and managed by Evelode. The same UptimeScout license works with REST, MCP and every UptimeScout SDK.

Set the key in your server environment:

```sh
export UPTIMESCOUT_LICENSE_KEY='your-license-key'
```

PowerShell: `$env:UPTIMESCOUT_LICENSE_KEY = 'your-license-key'`.

**2. Choose a transport.**

| Connection | Use it when | Setup |
| --- | --- | --- |
| Hosted Streamable HTTP | Your client supports a URL and Bearer authorization | `https://mcp.uptimescout.com` |
| Local stdio bridge | Your client launches a command | Install the Python bridge below |
| Shared jsonscraper MCP | You want several independently licensed products in one assistant connection | [Shared connector](https://jsonscraper.com/mcp#connect) |

For the dedicated hosted endpoint, configure the header `Authorization: Bearer YOUR_EVELODE_LICENSE_KEY` in your client's protected credential settings. No Python installation is needed. This endpoint uses Bearer authentication; the shared connector has its own OAuth setup.

**Local stdio installation:**

```sh
python -m pip install "git+https://github.com/jsonscraper/uptimescout-mcp-server.git@0.1.4"
```

Then launch `uptimescout-mcp` from a client that inherits `UPTIMESCOUT_LICENSE_KEY`. Use the absolute executable path if your desktop client cannot find it.

**Example stdio configuration** for clients using an `mcpServers` object:

```json
{
  "mcpServers": {
    "uptimescout": {
      "command": "/absolute/path/to/uptimescout-mcp",
      "env": {
        "UPTIMESCOUT_LICENSE_KEY": "YOUR_EVELODE_LICENSE_KEY"
      }
    }
  }
}
```

The value above is a placeholder. Store your actual configuration privately. This JSON does not imply that all clients support environment-variable interpolation inside HTTP headers.

**3. Ask your assistant:** “Check GitHub and Cloudflare in GB. Report each signal, observation time and freshness. Do not describe another region as affected without checking it.”

[Full setup, client configuration and troubleshooting](docs/mcp.md) · [Example tool calls](examples/README.md)

## Example response

A real public GitHub observation captured on **2026-11-18**, shown as a historical example. It is not a live status claim. License-specific usage fields are omitted.

```json
{
  "status": "ok",
  "region": "GB",
  "service": {
    "id": "github",
    "name": "GitHub",
    "category": "it",
    "status": "operational",
    "stale": false,
    "observed_at": "2026-11-18T03:11:21.650479Z",
    "age_seconds": 60,
    "regions": [
      "GB"
    ],
    "signal": "reported_availability",
    "scope": "regional",
    "logo_url": "https://uptimescout.com/static/brand-assets/github.svg?v=18e8fe76f953a31c",
    "logo_kind": "brand",
    "description": "Platform for Git repositories, code collaboration, issues and software delivery.",
    "description_language": "en"
  },
  "generated_at": "2026-11-18T03:12:21.928449Z",
  "data_type": "availability_observations",
  "stale_after_seconds": 600
}
```

`status` at the top level describes the API request. `service.status` describes the availability signal. Always read `stale`, `observed_at` and `region` together. The region selects observations; `lang` independently selects service-description language.

MCP wraps the API result in `result.structuredContent` and also returns a text content block. Inspect `result.isError` before presenting a tool result as successful. [Full MCP response envelope](docs/responses.md#mcp-envelope).

## Main methods

| Goal | REST endpoint | MCP tool |
| --- | --- | --- |
| Search the service catalog | `GET /v1/services` | `uptimescout_services` |
| Read one regional signal | `GET /v1/status` | `uptimescout_status` |
| Check several services in one call | `GET /v1/statuses` | `uptimescout_statuses` |
| Summarize selected services | `GET /v1/summary` | `uptimescout_summary` |
| Read observation history | `GET /v1/history` | `uptimescout_history` |
| Inspect observation statistics | `GET /v1/stats` | `uptimescout_stats` |
| Find fresh elevated signals | `GET /v1/incidents` | `uptimescout_incidents` |

[Complete parameters and pagination](docs/endpoints.md) · [Response fields and errors](docs/responses.md) · [OpenAPI specification](https://uptimescout.com/openapi.json)

## Ready-to-run examples

- [Search the service catalog](examples/calls/services.json).
- [Read one regional signal](examples/calls/status.json).
- [Check several services in one call](examples/calls/statuses.json).
- [Summarize selected services](examples/calls/summary.json).
- [Read observation history](examples/calls/history.json).
- [Inspect observation statistics](examples/calls/stats.json).
- [Find fresh elevated signals](examples/calls/incidents.json).

Each data example performs **one request**. Pagination is explicit; no example downloads the entire catalog or history automatically. Run `--help` first to see usage without sending a data request. JSON files in the MCP repository are request bodies, not executable scripts.

[Example commands for all seven methods](examples/README.md)

## Regions, languages and logos

Use a two-letter country code such as `GB`, `DE` or `JP`; discover current coverage in `available_regions`. Coverage can differ by service. Without `region`, responses may aggregate observed countries, so specify it when you need a regional answer.

Descriptions support 20 language codes: `en`, `ar`, `cs`, `de`, `es`, `fi`, `fr`, `he`, `it`, `ja`, `ko`, `nl`, `no`, `pl`, `pt`, `ru`, `sv`, `tr`, `uk`, `zh`.

Service metadata includes `description`, `description_language`, `logo_url` and `logo_kind`. Use the versioned HTTPS logo URL with its HTTP cache headers. `logo_kind` distinguishes a brand asset from a monogram fallback.

## Plans and request accounting

| Plan | Requests per minute | Services per batch | History window |
| --- | ---: | ---: | ---: |
| Free | 60 | 5 | 7 days |
| Starter | 300 | 10 | 7 days |
| Builder | 600 | 25 | 30 days |
| Pro | 1,800 | 50 | 90 days |
| Scale | 3,600 | 100 | 90 days |

The rate window is 60 seconds. A successful data call counts as one request, including a batch within your plan's limit. Each additional history page is another call. Failed or rejected calls do not consume the successful-request allowance. Respect HTTP 429 and `Retry-After` when present.

Usage resets on license renewal or a plan change, not on the first day of a calendar month. Annual plans provide twelve monthly allowances as one pool for the full license term, with the same rate limit. History is available only for periods in which observations were collected.

[Current prices and license-period allowances](https://jsonscraper.com/services/uptimescout-api?utm_source=github&utm_medium=sdk&utm_campaign=uptimescout-mcp-server&utm_content=readme#pricing) · [License management](https://evelode.com/checkout/purchase-history/)

## Understanding the data

Observations are updated every minute. A reported disruption signal is not a confirmed global outage or a direct uptime measurement. Regional signals can differ. Missing or stale observations remain unknown; sample statistics must not be labelled as an uptime SLA.

## Configuration and troubleshooting

[Hosted HTTP and local stdio configuration](docs/mcp.md) · [Full integration guide](docs/guide.md)

## Support and license

The client source is [MIT-licensed](LICENSE); hosted API access uses a separate UptimeScout license.

[Service support](https://jsonscraper.com/contacts?utm_source=github&utm_medium=sdk&utm_campaign=uptimescout-mcp-server&utm_content=support) · [Report an SDK issue](https://github.com/jsonscraper/uptimescout-mcp-server/issues) · [Documentation](docs/guide.md)

When reporting a problem, include the client version, method, region and error status. Redact license keys and authorization headers.

The SDK and bridge contain no installation or API-usage telemetry. Documentation links use campaign parameters for website referral analytics. Service names and logos identify monitored services and do not imply endorsement or partnership.

## Remote MCP authorization

Connect to `https://mcp.uptimescout.com` with OAuth. Sign in through your **Evelode account** or enter a **UptimeScout license key** on the authorization screen. Secure Bearer headers and local stdio remain available. [Connection options and revocation](docs/mcp.md) · [Setup guide](https://mcp.uptimescout.com/connect).
