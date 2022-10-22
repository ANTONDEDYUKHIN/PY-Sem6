# для натурального Н создать словарь
# индекс-значение, состоящий из элементов
# посл-ти 3н+1
# пример для н=6 :{1:4, 2:7, 3:10, 4:13, 5:16, 6:19}

number = int(input('input integer N = '))
li1 = [x for x in range(1, number)]
li2 = list(map(lambda x: 3*x+1, li1))
data=list(zip (li1, li2))
print(data)