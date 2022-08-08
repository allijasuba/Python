def elif_main():
    pass


def main():
        w = float(input("Weight of order:\n"))
        if w <= 0:
            print("Bye")
            exit()
        if w <= 10:
            print("Shipping cost: $", 3)
            main()
        if w > 10:
            extra = w - 10
        shipping = extra * .25 + 3
        print("Shipping cost: $", shipping)
        main()
        elif_main()
main()
