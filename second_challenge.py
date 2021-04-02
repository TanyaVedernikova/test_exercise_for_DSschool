import re

list_of_signs = ["A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12", "AA123A12456"]

#первый способ,что пришел в голову,так как длина знака строго фиксирована, просто проверять на каждой позиции что это, число или буква
def parser_for_signs1(list_of_signs):
    list_of_correct_signs = []

    for sign in list_of_signs:
        if len(sign) == 8 or len(sign) == 9:
            if sign[0].isalpha():
                if sign[1 : 4].isdigit():
                    if  sign[4 : 6].isalpha():
                        if sign[6 : 8].isdigit():
                            if len(sign) == 8 or sign[8].isdigit():
                                list_of_correct_signs.append(sign)


#возвращаю список корректных знаков
    return list_of_correct_signs


print(parser_for_signs1(list_of_signs))

#здесь мне захотелось поиграть с библиотекой регулярных выражений, попробовать,  чтобы по формату разбивался знак на составляющие
def parser_for_signs2(list_of_signs):
    list_of_correct_signs = []

    #формат с двумя цифрами в конце
    pattern1 = r'\w{1}\d{3}\w{2}\d{2}\b'
    #формат с тремя цифрами в конце
    pattern2 = r'\w{1}\d{3}\w{2}\d{3}\b'

    #просто потом ищу их
    for sign in list_of_signs:
        if re.fullmatch(pattern1,sign)!= None:
            list_of_correct_signs.append(sign)
        elif re.fullmatch(pattern2,sign)!= None:
            list_of_correct_signs.append(sign)




    return list_of_correct_signs


print(parser_for_signs2(list_of_signs))
