def count_words(words):
    import re
    t = str(type(words))
    if "\'str\'" not in t:
        print("This function only accepts strings")
        return None
    words = re.sub('[^0-9a-zA-Z -\']+', '', words)
    # words = re.sub('[^0-9a-öA-Ö -\']+', '', words)
    # above doesn't work with åöä or ÅÖÄ, messes the removal of special signs (¿ is not purged for example)
    wordList = words.split(" ")
    wordList.sort()
    wordDict = dict()
    for w in wordList:
        count = 0
        for word in wordList:
            w, word = w.lower(), word.lower()
            if word == w:
                count += 1
        wordDict[w] = count
    # print(wordDict)
    return wordDict


if __name__ == "__main__":

    string = "Å world is a world, ¿were it in any way it is, don't ä ö Ä Ö"
    counted = count_words(string)
    print(counted)
