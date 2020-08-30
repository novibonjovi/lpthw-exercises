# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i += 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")


# print("The numbers: ")

# for num in numbers:
#     print(num)


i = 0
numbers = []


def count_list(num):
    i = 0

    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)
