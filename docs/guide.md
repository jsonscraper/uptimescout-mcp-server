# Integration guide

[README](../README.md)

1. [Install and make your first request](../README.md#quick-start).
2. [Run examples for all seven methods](../examples/README.md).
3. [Select region, language and method parameters](endpoints.md).
4. [Interpret responses and freshness](responses.md).
5. [Configure your runtime and handle failures](configuration.md).
6. [Connect an AI assistant](mcp.md).
7. [Compare plans and obtain a key](https://jsonscraper.com/services/uptimescout-api?utm_source=github&utm_medium=sdk&utm_campaign=uptimescout-mcp-server&utm_content=readme#pricing).

## Installation

Requires Python 3.10+. The client package identifier is `uptimescout-mcp`. Installation from the GitHub release:

```sh
python -m pip install "git+https://github.com/jsonscraper/uptimescout-mcp-server.git@0.1.3"
```

## First integration checklist

- Use a catalog service ID and an explicit observation region.
- Distinguish API request outcome from `service.status`.
- Display observation time and freshness near the signal.
- Keep unknown and missing observations distinct from normal availability.
- Handle errors before accessing service fields.
- Bound history pages, retries and simultaneous requests.
- Use versioned logo URLs and the returned description language.
- Keep the key on your server or in private MCP credential settings.

[Questions or service support](https://jsonscraper.com/contacts?utm_source=github&utm_medium=sdk&utm_campaign=uptimescout-mcp-server&utm_content=support).
