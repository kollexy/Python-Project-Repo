lower = 2000
upper = 2024
x = list(range(lower, upper))

for i in x:
    my_list = []
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        my_list.append(i)
    else:
        print("not a leap year")
print(my_list)
print(my_list.count())
#
# year = 2032
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print("not a leap year")

#
