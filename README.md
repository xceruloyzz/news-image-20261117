# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/xceruloyzz/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/xceruloyzz/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A one-image front page summing up the world news of Tuesday 17 November 2026: Ukraine's strike collapsing a span of the Crimea Bridge, tankers hit in the Strait of Hormuz as Iran tensions spike, Gaza's winter emergency (1.7 million displaced), Trump landing in Manila for the ASEAN summit, and COP31 climate talks entering their decisive days in Antalya — plus a ticker on Japan's jet scramble, oil at $92.76, and the ULA Vulcan failure. The date is named in the image itself, and every story is stated as reported on the day (BBC, Reuters, AP, The Guardian, WFP/IOM).

`main.py` (Python 3.13, standard library only, no network) copies the rendered `entry.png` beside it to the output path, byte for byte, so two runs always write identical bytes. The image is 1024x1024 PNG, well under 1 MiB. `tools/generate_frontpage.py` is the deterministic renderer that produced `entry.png` from the day's headlines hardcoded in it; rerunning it rebuilds the same image.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=ztsmgxnm&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
