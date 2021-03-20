# list1 = [["Harry", 1], ["Larry", 2], ["Carry", 6], ["Sarry", 8]]
# dict1 = dict(list1)

# for item in list1:
#     print(item)
# for item, lollypop in dict1.items():
#     print(item,"and the lolly is", lollypop)

# Quiz
list2 = ["Harshit","Harry","Piyush","Rohan","Rohit", 6, 2, 4, 7, 9, 1, 8]

for item in list2:
    if str(item).isnumeric() and item>=6:
        print("The number is",item)

