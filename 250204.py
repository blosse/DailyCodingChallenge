# Using a read7() method that returns 7 characters from a file,
# implement readN(n) which reads n characters.

# For example, given a file with the content “Hello world”,
# three read7() returns “Hello w”, “orld” and then “”.

# Comment on solve: Hardest part was figuring out the question
# Not even sure if this answers the question correctly.

nReads = 0
f1 = open("./testFiles/textFile.txt")
f2 = open("./testFiles/textFile.txt")

def read7() -> str:
    return f1.read(7)

def readN(n: int) -> str:
    return f2.read(n)


### test ###

test1 = read7()
test2 = read7()

test3 = readN(7)
test4 = readN(7)

assert test1 == test3, f"Returned {test3}"
assert test2 == test4, f"Returned {test4}"

f1.close() # Best practice
f2.close() # Best practice
