#!/usr/bin/env python3
"""Generate sentry-instrument semantics lookup files from published conventions.

Source: https://getsentry.github.io/sentry-conventions/api/attributes.json
Re-run when conventions bump. Commits the markdown artifacts on purpose (v0).
"""

from __future__ import annotations

import json
import urllib.request
from collections import defaultdict
from pathlib import Path

SOURCE_URL = "https://getsentry.github.io/sentry-conventions/api/attributes.json"
SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCES = SKILL_ROOT / "references"
OUT_DIR = REFERENCES / "semantics"
INDEX_PATH = REFERENCES / "semantics.md"

# Short "use when" hints for common domains; everything else falls back.
USE_WHEN = {
    "http": "HTTP client/server spans",
    "db": "database query spans",
    "gen_ai": "LLM / agent spans (manual or custom)",
    "mcp": "Model Context Protocol spans",
    "cache": "cache get/set spans",
    "messaging": "queue / pubsub spans",
    "browser": "browser / web-vital attributes",
    "app": "mobile/desktop app lifecycle",
    "device": "device hardware/OS facts",
    "user": "end-user identity attributes",
    "url": "URL components on spans",
    "server": "server address/port",
    "network": "network transport details",
    "cloudflare": "Cloudflare worker/bindings",
    "vercel": "Vercel platform attributes",
    "aws": "AWS service attributes",
    "gcp": "GCP service attributes",
    "faas": "serverless / function spans",
    "grpc": "gRPC spans",
    "graphql": "GraphQL spans",
    "sentry": "Sentry SDK / product attributes",
    "ui": "UI / rendering spans",
    "error": "error classification",
    "exception": "exception details",
    "code": "code unit / function location",
    "process": "process runtime facts",
    "os": "operating system facts",
    "service": "service name/version",
    "thread": "thread identity",
    "file": "file path operations",
    "flag": "feature flags",
    "logger": "logger name/context",
    "otel": "OpenTelemetry bridge attributes",
    "rpc": "generic RPC spans",
    "client": "client address attributes",
    "navigation": "client navigation spans",
}


def fetch_attributes() -> list[dict]:
    with urllib.request.urlopen(SOURCE_URL, timeout=60) as resp:
        return json.load(resp)


def main() -> None:
    attrs = fetch_attributes()
    stable = [a for a in attrs if not a.get("deprecated")]
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for a in stable:
        cat = a.get("category") or "general"
        by_cat[cat].append(a)

    for cat in by_cat:
        by_cat[cat].sort(key=lambda a: a["key"])

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # wipe previous domain files so renames/removals don't leave orphans
    for old in OUT_DIR.glob("*.md"):
        old.unlink()

    # domain files
    for cat, items in sorted(by_cat.items()):
        lines = [
            f"# {cat} attributes",
            "",
            f"Stable Sentry semantic convention attributes for `{cat}`.",
            "Generated — do not edit by hand. Re-run `scripts/gen-semantics.py`.",
            "",
            "| Key | Type | Brief |",
            "| --- | --- | --- |",
        ]
        for a in items:
            key = a["key"].replace("|", "\\|")
            typ = str(a.get("type", "")).replace("|", "\\|")
            brief = str(a.get("brief", "")).replace("|", "\\|").replace("\n", " ")
            lines.append(f"| `{key}` | `{typ}` | {brief} |")
        lines.append("")
        (OUT_DIR / f"{cat}.md").write_text("\n".join(lines), encoding="utf-8")

    # index / map
    index = [
        "# Semantic conventions map",
        "",
        "Lookup tables for Sentry span/log attribute keys, split by domain.",
        "",
        "**Rules**",
        "",
        "1. Prefer these stable keys. Do not invent attribute names when a convention exists.",
        "2. Open **only** the domain file you need — never load every domain.",
        "3. Deprecated attributes are omitted from this tree on purpose.",
        "4. Re-run `scripts/gen-semantics.py` when conventions change.",
        "",
        f"Source: [{SOURCE_URL}]({SOURCE_URL})  ",
        f"Stable attributes in this tree: **{len(stable)}** (of {len(attrs)} total upstream).",
        "",
        "| Domain | File | Count | Use when |",
        "| --- | --- | ---: | --- |",
    ]
    for cat, items in sorted(by_cat.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        use = USE_WHEN.get(cat, f"`{cat}.*` attributes")
        index.append(f"| `{cat}` | [`semantics/{cat}.md`](semantics/{cat}.md) | {len(items)} | {use} |")
    index.extend(
        [
            "",
            "Full browsable docs (escape hatch only):",
            "https://getsentry.github.io/sentry-conventions/attributes/",
            "",
        ]
    )
    INDEX_PATH.write_text("\n".join(index), encoding="utf-8")

    print(f"wrote {INDEX_PATH.relative_to(SKILL_ROOT)} and {len(by_cat)} domain files ({len(stable)} attrs)")


if __name__ == "__main__":
    main()
