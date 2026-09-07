def counts(text: str) -> dict[str, int]:
    """How often each character appears, in first-seen order."""
    found: dict[str, int] = {}
    for one in text:
        found[one] = found.get(one, 0) + 1
    return found


if __name__ == "__main__":
    print(counts("abracadabra"))
