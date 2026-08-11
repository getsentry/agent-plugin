# Semantic conventions map

Lookup tables for Sentry span/log attribute keys, split by domain.

**Rules**

1. Prefer these stable keys. Do not invent attribute names when a convention exists.
2. Open **only** the domain file you need — never load every domain.
3. Deprecated attributes are omitted from this tree on purpose.
4. Re-run `scripts/gen-semantics.py` when conventions change.

Source: [https://getsentry.github.io/sentry-conventions/api/attributes.json](https://getsentry.github.io/sentry-conventions/api/attributes.json)  
Stable attributes in this tree: **576** (of 791 total upstream).

| Domain | File | Count | Use when |
| --- | --- | ---: | --- |
| `sentry` | [`semantics/sentry.md`](semantics/sentry.md) | 63 | Sentry SDK / product attributes |
| `gen_ai` | [`semantics/gen_ai.md`](semantics/gen_ai.md) | 47 | LLM / agent spans (manual or custom) |
| `aws` | [`semantics/aws.md`](semantics/aws.md) | 37 | AWS service attributes |
| `device` | [`semantics/device.md`](semantics/device.md) | 37 | device hardware/OS facts |
| `vercel` | [`semantics/vercel.md`](semantics/vercel.md) | 36 | Vercel platform attributes |
| `mcp` | [`semantics/mcp.md`](semantics/mcp.md) | 31 | Model Context Protocol spans |
| `browser` | [`semantics/browser.md`](semantics/browser.md) | 28 | browser / web-vital attributes |
| `http` | [`semantics/http.md`](semantics/http.md) | 28 | HTTP client/server spans |
| `app` | [`semantics/app.md`](semantics/app.md) | 22 | mobile/desktop app lifecycle |
| `cloudflare` | [`semantics/cloudflare.md`](semantics/cloudflare.md) | 17 | Cloudflare worker/bindings |
| `messaging` | [`semantics/messaging.md`](semantics/messaging.md) | 17 | messaging systems |
| `db` | [`semantics/db.md`](semantics/db.md) | 15 | database query spans |
| `faas` | [`semantics/faas.md`](semantics/faas.md) | 13 | serverless / function spans |
| `grpc` | [`semantics/grpc.md`](semantics/grpc.md) | 13 | gRPC spans |
| `ui` | [`semantics/ui.md`](semantics/ui.md) | 12 | UI / rendering spans |
| `art` | [`semantics/art.md`](semantics/art.md) | 11 | `art.*` attributes |
| `network` | [`semantics/network.md`](semantics/network.md) | 11 | network transport details |
| `user` | [`semantics/user.md`](semantics/user.md) | 11 | end-user identity attributes |
| `gcp` | [`semantics/gcp.md`](semantics/gcp.md) | 10 | GCP service attributes |
| `os` | [`semantics/os.md`](semantics/os.md) | 9 | operating system facts |
| `url` | [`semantics/url.md`](semantics/url.md) | 9 | URL components on spans |
| `process` | [`semantics/process.md`](semantics/process.md) | 8 | process runtime facts |
| `cache` | [`semantics/cache.md`](semantics/cache.md) | 6 | cache get/set spans |
| `cloud` | [`semantics/cloud.md`](semantics/cloud.md) | 6 | `cloud.*` attributes |
| `jvm` | [`semantics/jvm.md`](semantics/jvm.md) | 6 | `jvm.*` attributes |
| `code` | [`semantics/code.md`](semantics/code.md) | 5 | code unit / function location |
| `culture` | [`semantics/culture.md`](semantics/culture.md) | 5 | `culture.*` attributes |
| `general` | [`semantics/general.md`](semantics/general.md) | 5 | `general.*` attributes |
| `nel` | [`semantics/nel.md`](semantics/nel.md) | 5 | `nel.*` attributes |
| `exception` | [`semantics/exception.md`](semantics/exception.md) | 4 | exception details |
| `otel` | [`semantics/otel.md`](semantics/otel.md) | 4 | OpenTelemetry bridge attributes |
| `rpc` | [`semantics/rpc.md`](semantics/rpc.md) | 4 | generic RPC spans |
| `score` | [`semantics/score.md`](semantics/score.md) | 4 | `score.*` attributes |
| `graphql` | [`semantics/graphql.md`](semantics/graphql.md) | 3 | GraphQL spans |
| `navigation` | [`semantics/navigation.md`](semantics/navigation.md) | 3 | client navigation spans |
| `client` | [`semantics/client.md`](semantics/client.md) | 2 | client address attributes |
| `event` | [`semantics/event.md`](semantics/event.md) | 2 | `event.*` attributes |
| `file` | [`semantics/file.md`](semantics/file.md) | 2 | file path operations |
| `jsonrpc` | [`semantics/jsonrpc.md`](semantics/jsonrpc.md) | 2 | `jsonrpc.*` attributes |
| `server` | [`semantics/server.md`](semantics/server.md) | 2 | server address/port |
| `service` | [`semantics/service.md`](semantics/service.md) | 2 | service name/version |
| `thread` | [`semantics/thread.md`](semantics/thread.md) | 2 | thread identity |
| `trpc` | [`semantics/trpc.md`](semantics/trpc.md) | 2 | `trpc.*` attributes |
| `angular` | [`semantics/angular.md`](semantics/angular.md) | 1 | `angular.*` attributes |
| `error` | [`semantics/error.md`](semantics/error.md) | 1 | error classification |
| `flag` | [`semantics/flag.md`](semantics/flag.md) | 1 | feature flags |
| `koa` | [`semantics/koa.md`](semantics/koa.md) | 1 | `koa.*` attributes |
| `logger` | [`semantics/logger.md`](semantics/logger.md) | 1 | logger name/context |
| `mdc` | [`semantics/mdc.md`](semantics/mdc.md) | 1 | `mdc.*` attributes |
| `middleware` | [`semantics/middleware.md`](semantics/middleware.md) | 1 | `middleware.*` attributes |
| `params` | [`semantics/params.md`](semantics/params.md) | 1 | `params.*` attributes |
| `react` | [`semantics/react.md`](semantics/react.md) | 1 | `react.*` attributes |
| `remix` | [`semantics/remix.md`](semantics/remix.md) | 1 | `remix.*` attributes |
| `resource` | [`semantics/resource.md`](semantics/resource.md) | 1 | `resource.*` attributes |
| `session` | [`semantics/session.md`](semantics/session.md) | 1 | `session.*` attributes |
| `state` | [`semantics/state.md`](semantics/state.md) | 1 | `state.*` attributes |
| `timber` | [`semantics/timber.md`](semantics/timber.md) | 1 | `timber.*` attributes |
| `user_agent` | [`semantics/user_agent.md`](semantics/user_agent.md) | 1 | `user_agent.*` attributes |

Full browsable docs (escape hatch only):
https://getsentry.github.io/sentry-conventions/attributes/
