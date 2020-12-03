def main():
    age = int(input('Пожалуйста, введите ваш возраст  '))
    if  0 <= age <= 6 :
        return 'Вы, должно быть, учитесь в детском саду'
    elif 6 < age <= 17 :
        return 'Вы, должно быть, учитесь в школе'
    elif 17 < age <= 22 :
        return 'Вы, должно быть, учитесь в ВУЗе'
    elif 22 < age :
        return 'Вы, должно быть, работаете'
    else:
        raise ValueError('ошибка ввода')

if __name__ == "__main__":
    age_test = main()
    print(age_test)