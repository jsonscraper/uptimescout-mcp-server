# Connect to UptimeScout MCP

The dedicated Streamable HTTP endpoint is **https://mcp.uptimescout.com**. Open the [connection guide](https://mcp.uptimescout.com/connect) for the server URL and authorization options.

## OAuth: Evelode account or license key

1. Add the server URL in a remote MCP client and select OAuth.
2. Allow the client to register automatically. No client secret is required.
3. On the UptimeScout connection screen, choose **Sign in with Evelode** or enter your **UptimeScout API license key**.
4. Review the requesting application and confirm read access.

With Evelode, you sign in on evelode.com using the account's available sign-in methods. UptimeScout never receives your account password. The grant is limited to `uptimescout:read`; it does not connect TikTok or Instagram licenses.

OAuth uses authorization code flow with PKCE S256, short-lived access tokens and rotating refresh tokens. Clients discover authorization endpoints from the protected-resource metadata and HTTP 401 challenge. Tokens issued here are bound to this dedicated MCP server; they are not REST API credentials.

Account-linked connections refresh current license entitlements automatically. Renew or change your plan in [Evelode licenses](https://evelode.com/licenses/). Manage or revoke the account grant in [Evelode authorized apps](https://evelode.com/dashboard/#authorized-apps). A revoked connection needs authorization again. License expiration and normal plan limits still apply.

## Bearer header and local stdio

For an HTTP client with secure header configuration, set `Authorization: Bearer YOUR_EVELODE_LICENSE_KEY`. Local stdio uses `UPTIMESCOUT_LICENSE_KEY` in the process environment. Never paste keys into an assistant conversation or commit them to a repository.

REST SDKs continue to use the Evelode license key. Every successful MCP data call uses the same UptimeScout plan quota as REST; authentication itself does not run a service-data method.

## Shared jsonscraper connector

The shared server **https://mcp.jsonscraper.com** remains available if you want to combine UptimeScout with other licensed products. It has its own OAuth audience and independent consent. Do not reuse tokens across the two servers.
