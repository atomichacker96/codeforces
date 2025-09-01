numberOfWords = int(input())


def wordEncoding(word):
    if len(word) > 10:
        return word[0] + str(len(word) - 2) + word[-1]
    else:
        return word


for i in range(numberOfWords):
    word = input()
    print(wordEncoding(word))
