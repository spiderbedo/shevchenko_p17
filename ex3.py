def find_antonym() -> None:
    
    """
    Reads the dictionary and finds the needed antonym for the word.
    If the word is not in the dictionary, the word stays the same
    Args:
        None
    Returns: 
        None
    """
    
    n = int(input())
    antonyms = {}
    for i in range(n):
        line = input().strip()
        word1, word2 = line.split()
        antonyms[word1] = word2
        antonyms[word2] = word1
    target = input()
    result = antonyms.get(target, target)
    print(result)


if __name__ == "__main__":
    find_antonym()
