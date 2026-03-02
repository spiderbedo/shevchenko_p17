def translate_word() -> None:

    '''
    Reads a dictionary of N Russian-English word pairs, then translates the phrase.
    If a word is not in the dictionary, it remains unchanged.
    Return: None
    '''

    number = int(input())
    ru_eng_dict = {}
    for i in range(number):
        words = input().split()
        ru, eng = words
        ru_eng_dict[ru] = eng
    stroka = input().split()
    trans_stroka = [ru_eng_dict.get(slovo, slovo) for slovo in stroka]
    print(' '.join(trans_stroka))

if __name__ == "__main__":
    translate_word()
