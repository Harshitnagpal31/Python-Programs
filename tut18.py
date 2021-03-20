# i = 0

# while (True):
#     if i + 1 < 5:
#         i = i + 1
#         continue
#     print(i)
#     if i == 44:
#         break # stop the loop
#     i = i + 1

# Quiz
while (True):
    print("Enter the number :", end=" ")
    inp = int(input())
    if inp>100:
        print("Congratulations! You have entered a number greater than 100")
        break
    else:
        continue


