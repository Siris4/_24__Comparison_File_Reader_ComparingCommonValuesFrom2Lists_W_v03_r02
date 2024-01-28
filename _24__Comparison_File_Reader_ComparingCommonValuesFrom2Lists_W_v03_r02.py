
import pandas

# Reading and processing the files
with open("file1.txt", mode="r") as file1:

    # short_names = [name for name in names if len(name) <= 4]
    file1_read = [line.strip() for line in file1.readlines()]

    # print(file1_read)             #prints out complete list for file1

with open("file2.txt", mode="r") as file2:
        # short_names = [name for name in names if len(name) <= 4]
    file2_read = [line.strip() for line in file2.readlines()]

    # print(file2_read)              #prints out complete list for file2

result = [int(num) for num in file1_read if num in file2_read]     # num gets converted to int in the very beginning of the variable definition part of the line block.
    # new_list = [new_item for item in list if testpasses]
print(result)
# [3, 6, 5, 33, 12, 7, 42, 13]

    #solution is all the way to the right, if you want it:                                                                                                                          # file1_read = [line.strip() for line in file1.readlines()]
    # with open("C:/Users/guber/Desktop/CoDex - Code Index - GitHub for HDD/Python/100 Days of Code - Projects Code - in PyCharm/__Learning Only Files - Only Mini-Projects here__/Day 26 Start - List and Dictionary Comprehension NATO Alphabet/file2.txt", mode="r") as file2:

'''
# Convert lists to pandas Series
series1 = pd.Series(file1_read)
series2 = pd.Series(file2_read)


# Convert lists to sets and find the intersection of values:
values_in_common = set(series1) & set(series2)

print(values_in_common)

'''