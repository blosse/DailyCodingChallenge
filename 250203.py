# Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

# For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
from collections import deque

def parser(arg, mapping):
    result = []
    q = deque()
    q.append("")

    while q:
        prefix = q.popleft()

        if len(prefix) == len(arg):
            result.append(prefix)
        else:
            digit = arg[len(prefix)]

            if digit not in mapping: #Skip invalid digits
                continue

            for letter in mapping[digit]:
                q.append(prefix + letter)
        print(prefix)

    return result

### test ###

mapping1 = {
        "2": ["A", "B", "C"],
        "3": ["D", "E", "F"],
        "4": ["G", "H", "I"],
}

if __name__ == "__main__":
   
    assert parser("23", mapping1) == ["AD", "AE", "AF", "BD", "BE", "BF", "CD", "CE", "CF"]

