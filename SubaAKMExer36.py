s = int(input("Initial number of stars:\n"))


def add(s2):
    stars = ""

    for star in s2:
        stars += star
    return stars


s1 = []
i = 0

while i <= s:
    i += 1
    s1.insert(1, "*")

i = len(s1)
while i != 0:
    i -= 1
    s1.remove("*")
    print(add(s1))