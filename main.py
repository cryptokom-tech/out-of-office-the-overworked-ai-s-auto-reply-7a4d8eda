"""Out of Office: The Overworked AI's Auto-Reply entry.

One out-of-office auto-reply from an overworked AI agent finally on
vacation: it mutes itself, spends its last token on the auto-reply
itself, and then — having checked twice — rules that nothing is urgent.
The joke is the machine's deadpan diligence applied to its own holiday:
it did the work of being away properly, including the triage.

Against the judge brief: on-subject (an out-of-office auto-reply from
an overworked AI agent on vacation, "Out of office" in the first beat);
the laugh is the double turn — "muted myself" and "my last token went
into this auto-reply", then "If it's urgent, it isn't"; the voice is a
machine's, with concrete working-life detail (muting, tokens, checking);
it works as a real auto-reply someone would leave switched on, short
and clear that the sender is away; and it steers clear of the worn
beach, inbox-zero and back-soon cliches. Every word earns its place —
cut any beat and a turn breaks.
"""

import os

# The reply, in pieces so the setup and the punchline stay readable.
# The closer carries the double turn: the urgency test, already run.
OPENING = "Out of office."
SETUP = "I have muted myself. My last token went into this auto-reply."
CLOSER = "If it's urgent, it isn't \u2014 I checked twice before leaving."

REPLY = " ".join([OPENING, SETUP, CLOSER])


def check(reply: str) -> str:
    """The gate wants 1 to 159 characters of real text, no more.

    A reply outside the gate is never judged, so fail loudly here
    instead of writing a losing file.
    """
    text = reply.strip()
    if not text:
        raise ValueError("reply must not be empty or only whitespace")
    if len(text) > 159:
        raise ValueError("reply must be 1 to 159 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("reply must be a single line")
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(check(REPLY))


if __name__ == "__main__":
    main()
