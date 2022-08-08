def main():

    im = float(input('Initial miles:\n '))
    if im <= 0:
        print('Bye.')
        exit()
    if im > 0:
        fm = int(input('Final miles:\n '))
        g = int(input('Gallon: \n '))
        mpg = ((fm - im) + 0.0)/g
        print("Miles Per Gallon: ", mpg)
        main()

    else: main()
main()
