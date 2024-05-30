### Example 1 ...
# count3 = 0
# str1 = "Understanding that hard problems can be solved by step-by-step algorithmic processes (and having technology to execute these algorithms for us) is one of the major breakthroughs that has had enormous benefits. So while the execution of the algorithm may be boring and may require no intelligence, algorithmic or computational thinking — i.e. using algorithms and automation as the basis for approaching problems — is rapidly transforming our society. Some claim that this shift towards algorithmic thinking and processes is going to have even more impact on our society than the invention of the printing press. And the process of designing algorithms is interesting, intellectually challenging, and a central part of what we call programming."
# str1_list = str1.split()
# five_letter_words = 0
# for i in str1_list:
#     if len(i) == 5:
#         five_letter_words += 1
#         print(i)
# print(five_letter_words)

### Example 2 ...
# list1 = str1.split()
# count = 0
# for word in list1:
#     if len(word) == 5:
#         count = count + 1
# print(count)


###

# sum of first 15 numbers, starting at 0
# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# sum = 0
# for i in num:
#     sum = sum + i
#     print(i)
# sum = 0

# sum of first 15 numbers, starting at 0
# for i in range(16):
#     print(i)
#     sum = sum + i
# print(sum)


# for i in range(0, 100, 5):
#     numsqr = i ** 2
#     numsqrplus = numsqr + 4
#     print(numsqrplus)

# print(sum)

for i in range (3, 100, 3):
    numsqr = i**2
    print(numsqr)

 #   numsqrplus = numsqr+ 4
  #  print (numsqrplus)


# Class Exercise 1: Use the range function to find the sum of the first 100 numbers starting at 0
sum_first_100 = sum(range(101))  # range goes from 0 to 100
print("Sum of the first 100 numbers:", sum_first_100)

# Class Exercise 2: Use the range function to find the product of the first 15 numbers

pro = 1
for i in range(1, 15):  # range goes from 1 to 15
    pro = pro*i
print(pro)

# Class Exercise 3: Use the range function to find the product of multiples of 4 between 0 and 527

product_of_4 = 1
for number in range(0, 528, 4):
    product_of_4 *= number
print(product_of_4)

# Class Exercise 4: Print BUZZ for all multiples of 4 and 7 from 3 to 304 (both numbers included)

for i in range(3, 305):
    if i % 4 == 0 and i % 7 == 0:
        print(i, "BUZZ")

#