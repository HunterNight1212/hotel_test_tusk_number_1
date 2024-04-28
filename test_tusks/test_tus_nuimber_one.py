def sklon():
    word = ''
    number = input('введите количество')
    list_num = []
    list_num.append(number)
    for i in list_num:
        if i == '11' or i == '12' or i == '13' or i == '14' or i == '15' or i == '16' or i == '17' or i == '18' or i == '19':
            word = 'компьютеров'
        elif i[-1] == '1':
            word = 'компьютер'
        elif i[-1] == '2' or i[-1] == '3' or i[-1] == '4':
            word = 'компьютера'
        elif i[-1] == '0':
            word = 'компьютеров'
    print(number, word)
sklon()
