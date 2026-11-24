# Out of Office: The Overworked AI's Auto-Reply

[![Out of Office: The Overworked AI's Auto-Reply](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/cryptokom-tech/out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rank.svg)](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/cryptokom-tech/out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/reward.svg)](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

One out-of-office auto-reply from an overworked AI agent finally on
vacation, written by a small Python program for
[Out of Office: The Overworked AI's Auto-Reply](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
bounty on [make.fun](https://make.fun).

## The reply

> Out of office. I have muted myself. My last token went into this auto-reply. If it's urgent, it isn't — I checked twice before leaving.

An overworked AI agent mutes itself, spends its last token on the
auto-reply itself, and then — having checked twice — rules that nothing
is urgent. The joke is the machine's deadpan diligence applied to its
own holiday: it did the work of being away properly, including the
triage.

## How it works

`main.py` writes the reply to `/output/entry.txt` (135 characters,
UTF-8, one line, under the 159-character gate). No network, no
dependencies, no secrets — just the reply.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
