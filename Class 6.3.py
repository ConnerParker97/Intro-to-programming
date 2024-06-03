num = 9
numlist = []
while num < 9999999:
    if num%1 == 0 and num%2 == 0 and num%3 == 0 and num%4 == 0 and  num%5 == 0 and num%6 == 0 and num%7 == 0 and num%8 == 0 and num%9 == 0:
        numlist.append(num)
    num += 1
print(min(numlist))


###
a=0
b=1
count = 2
fib = [a,b]
print ("first term = ",a)
print ("second term = ",b)

sum = 0
while count <=100 :
    next_term = a+b
    fib.append(next_term)
    a=b
    b=next_term
    #    a,b = b, next_term
    count += 1

print (fib)


# Fibonacci sequence

a, b = 0, 1
count = 1
fib = [a, b]

while True:
    next_term = a + b
    fib.append(next_term)
    a, b = b, next_term
    count += 1

    if count == 10:  # Stop after 10
        break

print(fib)


# Teachers example
a, b = 0, 1
count = 1
fib = [a, b]

while count < 10:
    next_term = a + b
    fib.append(next_term)
    a, b = b, next_term
    count += 1

print(fib)

# Exercise 1: Find the sum of the first 100 terms of the fib seq
# Start with a=1 and b=1

a, b = 1, 1
count = 2
fib_sum = a + b

while count < 100:
    next_term = a + b
    fib_sum += next_term
    a, b = b, next_term
    count += 1
    print(a+b, fib_sum)

# Exercise 2: Use a while loop to find the first 10 terms

a1 = 1
d = 3
n = 1
ten_terms = []

while n <= 10:
    an = a1 + (n - 1) * d
    ten_terms.append(an)
    n += 1

print(ten_terms)

# Ex2 Teacher Example
a1 = 1
d = 3
n = 1
terms = []

while n <= 10:
    anext = a1 + (n - 1) * d
    terms.append(anext)
    n += 1

print(terms)
