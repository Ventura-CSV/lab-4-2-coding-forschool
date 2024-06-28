def main():

    total = 0 

    for i in range(5):
        number = int(input('Enter an integer value: '))
        total += number

    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
