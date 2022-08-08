first_word = input("Please enter the first word:\n")
second_word = input("Please enter the second word:\n")


def add(d1):
    dots = ""

    for dot in d1:
        dots += dot
    return dots


d = [first_word, second_word]
i = len(first_word + second_word)

while i != 30:
    i += 1
    d.insert(1, ".")

print(add(d))
