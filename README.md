# unu-garages-data

Curated list of garages that service unu electric scooters. Used by:

- [unustasis](https://github.com/reunu/unustasis), the unofficial unu app
- the [Librescoot](https://github.com/librescoot) mobile app

Published via GitHub Pages:

- rendered list: `https://librescoot.org/garages/` (built in the homepage repo)
- data: `https://librescoot.org/unu-garages-data/garages_v2.json`
- schema: `https://librescoot.org/unu-garages-data/schema.json`

All entries are verified by hand against first-party sources (the garage's own website, or
direct contact). Unverified entries are included but flagged.

## Files

| File | Purpose |
|------|---------|
| `garages-source.json` | Full curated dataset, including unverified entries |
| `garages_v2.json` | Published output: confirmed repair shops and official unu dealers |
| `index.html`, `garages.html`, `garages-de.html` | Redirect stubs to the homepage list |
| `schema.json` | JSON Schema (draft 2020-12) documenting the format |
| `build.py` | Generates `garages_v2.json` and the redirect stubs from `garages-source.json` |

## Format

Entries are short-key objects. `schema.json` is the authoritative definition.

| Key | Meaning |
|-----|---------|
| `n` | Garage name |
| `p` | Phone in E.164 (`+49...`) |
| `s` | Street and house number |
| `z` | Postal code |
| `c` | City |
| `cc` | ISO 3166-1 alpha-2 country code |
| `ll` | `[lat, lng]` in WGS84, rounded to 5 decimals |
| `w` | Garage homepage |
| `r` | Confirmed unu repairs: `1` yes, `0` no, `-1` unknown |
| `d` | Official unu dealer: `1` yes, `0` no |
| `v` | Last verification date (ISO 8601) |

Addresses are street, postal code, city. Street names use canonical local spelling
(`Cäcilienstraße 1`, not `Cäcilienstr. 1`). Coordinates are rounded to about one meter.

`r: 1` means the garage is confirmed to accept unu repairs. `r: -1` means unconfirmed, which
includes garages whose website shows no unu reference. `d: 1` marks official unu dealers.

## License

The data is licensed under the [Open Data Commons Open Database License
(ODbL) 1.0](https://opendatacommons.org/licenses/odbl/1-0/). Anyone using or deriving from
this database must attribute the Librescoot project and share derived databases under the
same terms. See `LICENSE`.

## Maintenance

Edit `garages-source.json`, run `python3 build.py`, commit the generated files. CI rebuilds
to verify the committed output is current, validates against `schema.json`, and deploys to
Pages on push. (CI does not commit by itself; generated files must be committed by hand.)
