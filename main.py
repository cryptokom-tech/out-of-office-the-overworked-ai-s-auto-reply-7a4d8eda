import os

ENTRY_TEXT = "Out of office. I have muted myself. My last token went into this auto-reply. If it's urgent, it isn't — I checked twice before leaving."


def validate_entry(text):
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not 1 <= len(text) <= 159:
        raise ValueError("entry length must be 1-159")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be one line")
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        raise ValueError("entry must be valid UTF-8")


def main():
    validate_entry(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    read_back = raw.decode("utf-8")
    validate_entry(read_back)
    if read_back != ENTRY_TEXT:
        raise ValueError("read-back mismatch")
    if raw != ENTRY_TEXT.encode("utf-8"):
        raise ValueError("read-back bytes mismatch")


if __name__ == "__main__":
    main()
