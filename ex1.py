def frequency() -> None:
    """
    Reads the line and finds the frequency of the words.
    If the frequency is equal, the program chooses the first in order.
    Args:
        None
    Returns:
        None
    """
    text = input().strip()
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    unique_words = []
    seen = set()
    for word in words:
        if word not in seen:
            seen.add(word)
            unique_words.append(word)
    sorted_words = sorted(unique_words, key=freq.get, reverse=True)
    for word in sorted_words:
        print(word)


if __name__ == "__main__":
    frequency()
