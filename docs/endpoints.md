# UptimeScout method reference

[README](../README.md) · [Responses](responses.md) · [Examples](../examples/README.md)

Base URL: `https://api.uptimescout.com/v1/`
Authentication: `Authorization: Bearer YOUR_EVELODE_LICENSE_KEY`

| Method | Required | Common optional parameters | Result |
| --- | --- | --- | --- |
| `services` | — | `q`, `category`, `region`, `lang`, `limit`, `offset` | Catalog and matching service signals |
| `status` | `service` | `region`, `lang` | One service and its observation metadata |
| `statuses` | `services` | `region`, `lang` | Several services in one data call |
| `summary` | — | `services`, `category`, `region`, `lang` | Signal counts across matching services |
| `history` | `service` | `hours`, `region`, `lang`, `limit`, `offset` | Saved observations and pagination |
| `stats` | `service` | `hours`, `region`, `lang` | Statistics over collected samples |
| `incidents` | — | `region`, `lang`, `limit`, `offset` | Services with fresh elevated signals |

`service` is a catalog ID, not an arbitrary URL. `services` is a comma-separated ID list over HTTP and MCP. Python, Node.js and PHP batch helpers also accept arrays and serialize them for you. Batch size is limited by your plan (5–100).

`limit` is 1–200. `offset` is zero-based. `hours` is 1–2160, additionally restricted by your plan's history depth. Use `next_offset`, not a guessed page count. Each page is a separate data call.

## Regional observations and localized metadata

Pass an ISO two-letter country code such as `GB`, `DE` or `JP`. The current set is returned in `available_regions`; do not hard-code a permanent list. Omit `region` only when a cross-region view is intended.

`lang` independently selects descriptions: `en`, `ar`, `cs`, `de`, `es`, `fi`, `fr`, `he`, `it`, `ja`, `ko`, `nl`, `no`, `pl`, `pt`, `ru`, `sv`, `tr`, `uk`, `zh`.

Service metadata includes localized `description`, actual `description_language`, versioned `logo_url` and `logo_kind` (`brand` or `monogram`). Logo URLs can be reused according to their HTTP response headers.

Read `observed_at`, `age_seconds` and `stale`. A country without a recent observation remains unknown. The same service can have different signals across regions.

## cURL example

```sh
curl --get 'https://api.uptimescout.com/v1/status' \
  --data-urlencode 'service=github' \
  --data-urlencode 'region=GB' \
  --data-urlencode 'lang=en' \
  --header "Authorization: Bearer $UPTIMESCOUT_LICENSE_KEY"
```

[Authoritative OpenAPI specification](https://uptimescout.com/openapi.json)
