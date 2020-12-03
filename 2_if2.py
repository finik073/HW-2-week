def main():
    enter1 = input('Введите первую строку  ')
    enter2 = input('Введите вторую строку  ')
    str_test = type(enter1) == str and type(enter2) == str
    if str_test == False:
        return 0
    elif enter1 == enter2:
        return 1
    elif len(enter1) > len(enter2):
        return 2
    elif enter2 == 'learn':
        return 3
    else:
        return "Ничего не произошло"

if __name__ == "__main__":
    print(main())
    print(main())
    print(main())