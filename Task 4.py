Hi = 'Привет, {}!'

wrong = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА','токарь высшего разряда нИКОЛАй', 'директор аэлита']

for correct in wrong:
    print(Hi.format(correct.split()[-1].title()))