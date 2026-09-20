#!/usr/bin/env python3
"""Generate garages_v2.json (published: confirmed repair shops and official unu
dealers) from garages-source.json (the full curated set)."""
import json, os, re, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
src = json.load(open(os.path.join(HERE, "garages-source.json")))["garages"]
pub = [dict(e) for e in src if e.get("r") == 1 or e.get("d") == 1]
out = {
    "$schema": "https://librescoot.org/unu-garages-data/schema.json",
    "garages": pub,
}
json.dump(out, open(os.path.join(HERE, "garages_v2.json"), "w"), separators=(",", ":"), ensure_ascii=False)

# Redirect stubs: the rendered list now lives on the homepage.
REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved</title>
<link rel="canonical" href="__TARGET__">
<meta http-equiv="refresh" content="0; url=__TARGET__">
</head>
<body>
<p>The garage list has moved to <a href="__TARGET__">__TARGET__</a>.</p>
</body>
</html>
"""
for name, target in (("index.html", "https://librescoot.org/garages/"),
                     ("garages.html", "https://librescoot.org/en/garages/"),
                     ("garages-de.html", "https://librescoot.org/garages/")):
    open(os.path.join(HERE, name), "w").write(REDIRECT.replace("__TARGET__", target))
print(f"{len(src)} entries -> garages_v2.json + schema.json + redirects")
