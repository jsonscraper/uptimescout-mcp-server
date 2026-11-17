# Methods

Base: `https://api.uptimescout.com/v1/`
Authentication: `Authorization: Bearer YOUR_EVELODE_LICENSE_KEY`

| Method | Parameters | Behavior |
|---|---|---|
| services | q, region, category, limit, offset | Search catalog |
| status | service, region | Current service status |
| statuses | services (comma-separated), region | Batch statuses |
| summary | services, region, category | Counts and freshness |
| history | service, hours, region | Observed history, maximum 90 days depending on plan |
| stats | service, hours, region | Sample ratios, not uptime |
| incidents | region, limit, offset | Fresh elevated signals |

Limit is 1–200, offset is zero-based. HTTP 400: invalid input; 403: license or plan restriction; 404: unknown service; 429: quota/rate limit; 503: temporarily unavailable. Never log license keys.

History supports `limit` (1–200) and `offset`. Follow `next_offset` until null to retrieve the whole requested window. `total` counts saved samples; gaps are unknown. Quotas count each page as one successful request.


### Regional observations and localized metadata

Pass `region` as an ISO country code, for example `GB`, `DE` or `JP`. Responses expose `available_regions`; the selected country is independent of `lang`. Omit `region` only when an aggregate view across observed countries is intended. Unknown or stale observations must remain unknown.

Pass `lang` to select one of 20 description languages: `en`, `ar`, `cs`, `de`, `es`, `fi`, `fr`, `he`, `it`, `ja`, `ko`, `nl`, `no`, `pl`, `pt`, `ru`, `sv`, `tr`, `uk`, `zh`. Service objects include `logo_url`, `logo_kind` (`brand` or `monogram`), `description`, and `description_language`. Logo URLs are versioned HTTPS URLs on uptimescout.com and can be cached using their response headers.

Read `observed_at`, `age_seconds` and `stale` for the actual freshness of each regional observation. A region without observations is not a worldwide outage. Data collection runs independently of API or MCP requests.
