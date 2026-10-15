#!/usr/bin/env python3
"""Update public Google Scholar statistics using the SerpApi author endpoint."""
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

key = os.environ.get("SERPAPI_API_KEY")
if not key:
    raise SystemExit("SERPAPI_API_KEY is not configured")
url = "https://serpapi.com/search.json?" + urlencode({
    "engine": "google_scholar_author",
    "author_id": "8_mITz8AAAAJ",
    "hl": "en",
    "api_key": key,
})
with urlopen(url, timeout=60) as response:
    result = json.load(response)
if result.get("error"):
    raise SystemExit("SerpApi error: " + str(result["error"]))
cited = result.get("cited_by") or {}
rows = cited.get("table") or []
graph = cited.get("graph") or []
def stat(key):
    for row in rows:
        if key in row:
            return int(row[key]["all"])
    raise ValueError("Missing metric: " + key)
years = [{"year": int(x["year"]), "citations": int(x["citations"])} for x in graph]
if not years:
    raise ValueError("No annual citation data returned")
data = {
    "citations": stat("citations"),
    "h_index": stat("h_index"),
    "i10_index": stat("i10_index"),
    "yearly": years,
    "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "source": "Google Scholar via SerpApi"
}
target = Path("assets/json/scholar_metrics.json")
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
print("Scholar citation metrics refreshed; no API credentials stored.")
