# Responses, errors and signal interpretation

[README](../README.md) · [Methods](endpoints.md)

## Regional status example

This complete public response was captured on 2026-11-18. It contains no license key or customer-specific usage. Treat its timestamps and signals as a historical example.

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
  "stale_after_seconds": 600,
  "available_regions": [
    "AE",
    "AR",
    "AT",
    "AU",
    "BD",
    "BE",
    "BR",
    "CA",
    "CH",
    "CL",
    "CO",
    "CZ",
    "DE",
    "DK",
    "EG",
    "ES",
    "FI",
    "FR",
    "GB",
    "GR",
    "HU",
    "ID",
    "IE",
    "IL",
    "IN",
    "IT",
    "JP",
    "KR",
    "MX",
    "MY",
    "NL",
    "NO",
    "NZ",
    "PE",
    "PH",
    "PK",
    "PL",
    "PT",
    "RO",
    "RU",
    "SA",
    "SE",
    "SG",
    "SK",
    "TH",
    "TR",
    "UA",
    "US",
    "VN",
    "ZA"
  ]
}
```

## Fields to use

| Field | Meaning |
| --- | --- |
| `status` | Request outcome; `ok` is distinct from a service's signal |
| `service.status` | `operational`, `degraded`, `outage` or `unknown` |
| `service.observed_at` | Timestamp of the regional observation, not when your request was made |
| `generated_at` | Time the response was generated |
| `service.stale` | Whether the observation has aged beyond the freshness window |
| `service.age_seconds` | Observation age; can be null when no observation exists |
| `region` | Requested observation country; null when no country was selected |
| `available_regions` | Currently observed country codes; not a guarantee every service has data everywhere |
| `service.scope` | `regional` or `any_observed_region` |
| `service.logo_url` | Versioned HTTPS service-logo URL |
| `service.logo_kind` | `brand` or `monogram` fallback |
| `service.description_language` | Language actually used for the description |
| `limits_info` | License usage and limits, when returned; handle omitted or unavailable fields |

A missing observation has `status: unknown`; null timestamps are not evidence of normal availability. A response may be valid while the observation is stale.

## Errors

| HTTP status | What to do |
| --- | --- |
| 400 | Correct invalid method parameters |
| 403 | Check license access or plan restrictions |
| 404 | Resolve a valid service ID with `services` |
| 429 | Stop immediate retries; honor `Retry-After` if returned, then back off |
| 503 | Retry later with a bounded attempt budget |

Check HTTP status and the JSON request outcome before reading service fields. Do not retry invalid credentials or invalid parameters indefinitely. Transport errors, timeouts and invalid JSON must also be handled. Avoid logging the full request headers or key.

## History and pagination

`history` returns saved observations, `total`, `limit`, `offset`, `next_offset` and `truncated`. Read one page, process it, and request another only when `next_offset` is not null and your application's page budget permits it. Catalog and incident results also expose pagination. One page consumes one successful request.

A statistics ratio describes collected samples. It is not a percentage of independently measured uptime.

## MCP envelope

The following envelope is shortened to show its structure; `structuredContent` contains the full API result illustrated above.

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "content": [{"type": "text", "text": "{...API response...}"}],
    "structuredContent": {"status": "ok", "region": "GB", "service": {"id": "github"}},
    "isError": false
  }
}
```

JSON-RPC errors appear in top-level `error`; data-call failures can instead be returned with `result.isError: true`. Handle both. Never interpret a failed tool call as a healthy service.

## All-method response files

See [real request and response examples for all seven methods](../examples/README.md#responses-for-every-method). These are dated public demonstration snapshots and do not include a license-specific quota envelope.
