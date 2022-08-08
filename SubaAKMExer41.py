print("Area of Rectangles")
def main():
    x1 = int(input("First corner X coordinate:\n"))
    y1 = int(input("First corner y coordinate:\n"))
    x2 = int(input("Second corner X coordinate:\n"))
    y2 = int(input("Second corner X coordinate:\n"))

    area = (x2 - x1) * (y2 - y1)

    if area == 0:
        print("")
        (main)
    else:
        print(f"Width: {abs(x2 - x1)}", f"\tHeight: {abs(y2 - y1)}", f"\tArea:", area)
main()

main()
