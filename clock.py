# -*- coding: utf-8 -*-
import sched, datetime, time, os
 
 
s = sched.scheduler(time.time, time.sleep)
tick = 1
 
 
def pari():
    time = datetime.datetime.now().replace(year=1,month=1,day=1)
    pari = [datetime.datetime(1,1,1,8,20), datetime.datetime(1,1,1,10,05), datetime.datetime(1,1,1,12,05),datetime.datetime(1,1,1,13,50),datetime.datetime(1,1,1,15,30)]
   
    end_para = []
    for i in pari:
        end_para.append(i + datetime.timedelta(hours = 1, minutes = 30))
       
    if time > pari[0] and time < end_para[0]:
        return  "1 para", "Do konca pari " + str(end_para[0] - time )[:-7]
    elif time > pari[1] and time < end_para[1]:
        return "2 para", "Do Koch pari"  + str(end_para[1] - time )[:-7]
    elif time > pari[2] and time < end_para[2]:
        return "3 para", "Do konca pari " + str(end_para[2] - time )[:-7]
    elif time > pari[3] and time < end_para[3]:
        return "4 para", "Do konca pari " + str(end_para[3] - time )[:-7]
    elif time > pari[4] and time < end_para[4]:
        return "5 para", "Do konca pari " + str(end_para[4] - time )[:-7]
     
    else:
        return "Net pari", ""     
 
 
def plusminus (b):
    if b:
        return "+"
    return "-"
   
 
def advance_length(string, max_len):
    if len(string) == max_len:
        return string
    else:
        return  string + " " * (max_len - len(string))
       
 
def frame(strings, tick):
    """ Генерирует рамочку вокруг strings используя функции plusminus и advance_length.
    tick - boolean.
    """
    max_len = 0
    for string in strings:
        max_len = max(len(string), max_len)  # находим максимальную длину строки
    output = []  # выходной массив строк
    length_string = (max_len/2+2)
    if tick == 1:
        s1 = "+-" * length_string
    else :
        s1 = "-+" * length_string  # генерируем верхнюю строку рамочки
    if max_len % 2 != 0:  # если в строке нечетное количество символов, то в верхнюю строку рамочки нужно добавить еще один символ
        s1 += plusminus(tick) # рамочка может быть либо +-+-+- при четном количестве, либо +-+-+-+ при нечетном
        right_symbol = tick   #                         -....+ < тогда символы по обе стороны строк будут разные
    else:                     #                         для отслеживания левого символа используется tick, для правого right_symbol
        right_symbol = not tick  #                      если четная длина рамочки, то tick не совпадает с right_symbol
    output.append(s1)
    for string in strings:  # для каждой строки
        tick = not tick  # меняем tick на противоположное значение
        right_symbol = not right_symbol  # right_symbol тоже
        output.append(plusminus(tick)  + " " + advance_length(string, max_len) + " " + plusminus(right_symbol))
        # ^^^ выводим каждую строку, слева символ соответствующий tick, справа right_symbol
    tick = not tick  # снова меняем tick, чтобы нижняя закрывающая рамочка начиналась с другого символа нежели последняя строка
    if tick == 1:
        s1 = "+-" * length_string
    else :
        s1 = "-+" * length_string
    if max_len % 2 != 0:
        s1 += plusminus(tick)  # последние шесть строчек копипаст из верхней части
    output.append(s1)  # добавляем нижнюю рамочку в output
    return output
   
 
def print_time():
    global tick
    nomer, left = pari()
    time = datetime.datetime.now().strftime("%H:%M:%S")
    strings = ["CockClock", time, nomer, left]
   
    if tick == 1 :
        strings[0] = "CockClock"
        tick = 0
    else:
        strings[0] ="ClockCock"
        tick = 1
    output = frame(strings, tick)    
    os.system('cls' if os.name=='nt' else 'clear')
    pari()
    for string in output:
        print string
 
 
def clock():
    while True :
        s.enter(0.5, 1, print_time, ())
        s.run()
 
 
clock()