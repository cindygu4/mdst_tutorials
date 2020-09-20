"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if x % 2 != 0:
        return True
    else:
        return False

def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    word = word.replace(" ", "")
    return word == word[::-1] 


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    return [num for num in numlist if is_odd(num)]


def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    words = {}
    word_list = text.lower().split()
    for word in word_list:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1
    
    return words

print("is_odd(5):", is_odd(5))
print("is_odd(8):", is_odd(8))
print("is_palindrome('word'):", is_palindrome('word'))
print("is_palindrome('racecar'):", is_palindrome('racecar'))
print("only_odds:", only_odds([1,2,3,4,5,6]))
print(count_words("How much wood would a woodchuck chuck if a woodchuck could chuck wood?"))
