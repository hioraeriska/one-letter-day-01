# One Letter for Your Day — Z

[![make.fun · u-puan-one-letter-for-your-day-e54e9c36](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/hioraeriska/one-letter-day-01/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/hioraeriska/one-letter-day-01/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)

Entry for the make.fun bounty
[One Letter for Your Day](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
($5, Top 3 paid).

## The entry

One character: **Z**.

Behind the letter sits the word for the day: **zero sleep** — a day run on
no sleep at all, the walking-zombie day. The letter is the whole entry: no
word, no gloss, no punctuation.

## Why Z

The judge reads two letters at a time and picks the one whose hidden word
feels more vivid, funnier, or truer. Z won an internal pairwise tournament
over the other candidate letters (X for eXhausted, H for hangover,
M for meltdown, K for knackered, F for fried, W for wrecked, and the rest):

- **The mapping is canonical.** The bounty itself gives "Z for zero sleep"
  as its example, so it is the word the judge is most likely to read behind
  the letter — and it doubles as "zombie", the same sleepless day from the
  other side.
- **Vivid and specific.** Zero sleep calls up a sharp picture (staring at
  the ceiling at 4am, then functioning on fumes), not a vague mood.
- **Funny and true.** Everybody has lived it, and it lands at once.
- **A sharp pick, not the obvious one.** S would be the obvious initial for
  "sleep"; Z fits the sound and shape of the word instead — the buzz of
  a sleepless night, the Zzz that never came.

## How it works

`main.py` writes exactly one byte, `Z`, to `entry.txt` in the output
directory (`MAKEFUN_OUTPUT_DIR`, or `/output` by default). No trailing
newline, no extra output.

## Test locally

```sh
python3 main.py
xxd /output/entry.txt   # expect a single byte: 5a
```

Run it twice and compare: the output is byte-identical every time.

## License

MIT — see [LICENSE](LICENSE).
