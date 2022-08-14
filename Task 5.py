list = [57.8, 46.51, 97, 100, 13.5, 64, 75.44, 98.66, 7.77, 14]

store_id = id(list)
print(f"{'a':}")
end_word: str = ", "

for i, num in enumerate(list):

    price = str(f"{float(num):.2f}").split(".")

    if i == len(list) - 1:
        end_word = "\n"

    print(f"{price[0]} руб {price[1]} коп", end=end_word)

print(f"{'-':-^79}")

print(f"id перед сортировкой {store_id}")
list.sort()
print(list)
print(f"id после сортировки {id(list)}")

print(f"{'-':-^79}")

copy_of_list = list.copy()
copy_of_list.sort(reverse=True)

print(copy_of_list)
print(store_id)
print(id(copy_of_list))

print(f"{'-':-^79}")

print("Цены пяти самых дорогих товаров", list[-6:-1])