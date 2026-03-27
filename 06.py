from collections import deque

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    queue = deque([(beginWord, 1)])

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i+1:]
                if new_word in wordSet:
                    queue.append((new_word, steps + 1))
                    wordSet.remove(new_word)

    return 1