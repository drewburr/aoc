input_file = "input.txt"

part = 2
data = []

for l in open(input_file):
    l = l.strip()
    data.append(l)


def count_vowels(word):
    vowels = list("aeiou")
    return sum(map(word.count, vowels))


def has_double(word):
    last = None
    for i, c in enumerate(word):
        if c == last:
            return i
        last = c
    return False

def has_double_double(word):
    for i, _ in enumerate(word):
        if i == 0: continue
        if contains_substring(word[i+1:], [word[i-1:i+1]]):
            # print(word[i+1:], '--',  word[i-1:i+1])
            return True

    return False


def contains_substring(word, substrings):
    def is_in(sub): return sub in word
    return 0 != sum(map(is_in, substrings))

def contains_palindrome(word):
    before = None
    last = None
    for i, c in enumerate(word):
        if c == before:
            return i
        before = last
        last = c
    return False

bad_substrings = ["ab", "cd", "pq", "xy"]
total = 0
for word in data:
    if part == 1:
        if (count_vowels(word) >= 3
            and has_double(word)
            and not contains_substring(word, bad_substrings)):
            total += 1
    else:
        if (contains_palindrome(word)
            and has_double_double(word)):
            # print(word)
            total += 1

print(total)
