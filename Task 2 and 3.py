list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

lenght: int = len(list1)
store_id = id(list1)
for i in range(lenght):
    subject = list1.pop(0)
    if subject.isdigit():
        list1.append(f'"{int(subject):01}"')
    elif subject[0] == "+" and subject[1].isdigit():
        list1.append(f'"+{int(subject):01}"')
    else:
        list1.append(subject)
print(' '.join(list1))