# Verification — news-image-20261117

Verified 2026-11-18 by a fresh verification/revision session (started after
the competition opened 2026-11-17T23:43Z).

## Image

- File: `entry.png`
- Size: 142,950 bytes
- Dimensions: 1024 × 1024 px, RGB PNG

## 1. Reproducibility (`tools/generate_frontpage.py`)

The committed `entry.png` was copied aside, then the generator was re-run
(`python3 tools/generate_frontpage.py` from the repo root) and the outputs
byte-compared with `sha256sum` / `cmp`:

- Committed:   `51d5b03e3571216bfa03e647dc78525ce0dfbb64efa11c277f891fd7b0e02be8`
- Regenerated: `51d5b03e3571216bfa03e647dc78525ce0dfbb64efa11c277f891fd7b0e02be8`

Result: **identical** — `cmp` reports no difference. The generator is
deterministic (fixed canvas/fonts, no randomness, clock, or network) and
rebuilds the committed image byte-for-byte. No generator change was needed.

## 2. Determinism (`main.py`, two runs)

`main.py` was run twice with `MAKEFUN_OUTPUT_DIR` set to two different
temporary directories:

- Run 1 output: `51d5b03e3571216bfa03e647dc78525ce0dfbb64efa11c277f891fd7b0e02be8` (142,950 bytes)
- Run 2 output: `51d5b03e3571216bfa03e647dc78525ce0dfbb64efa11c277f891fd7b0e02be8` (142,950 bytes)

Result: **identical** — both outputs also match the committed `entry.png`
hash above, as expected for a byte-for-byte copy.

## 3. Legibility at 300 × 300

`entry.png` was downscaled to 300 × 300 with PIL (Lanczos) and inspected
visually:

- Date line — "TUESDAY - 17 NOVEMBER 2026": **readable**, large white
  bold type on the red band.
- Lead headline — "UKRAINE BLOWS OPEN THE CRIMEA BRIDGE": **readable**,
  clearly legible in two lines.
- Panel headlines — all four **readable**:
  - "TANKERS HIT IN THE STRAIT OF HORMUZ"
  - "WINTER EMERGENCY GRIPS GAZA"
  - "TRUMP LANDS IN MANILA"
  - "CLIMATE TALKS ENTER DECISIVE DAYS"

Verdict: **PASS** — the date line, lead headline, and all four panel
headlines remain readable at 300 × 300. No headline-size fix was required,
so the generator and `entry.png` are unchanged.
