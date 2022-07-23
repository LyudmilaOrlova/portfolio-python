"""
Read in the contents of the file SP500.txt which has monthly data for 2016 and 2017
about the S&P 500 closing prices as well as some other financial indicators, including the “Long Term
Interest Rate”, which is the interest rate paid on 10-year U.S. government bonds. Write a
program that computes the average closing price (the second column, labeled SP500)
and the highest long-term interest rate. Both should be computed only for the period from June 2016
through May 2017
"""


with open("SP500.txt", "r") as file:
    print(file.read())
    closing_price = []
    interest_rate = []

    for line in file.readlines()[6:18]:
        new_line = line.split(',')
        closing_price.append(float(new_line[1]))
        interest_rate.append(float(new_line[5]))

    mean_SP = sum(closing_price) / len(closing_price)
    max_interest = max(interest_rate)

    
"""
addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers 
and assigns it to sum_val.
"""


addition_str = "2+5+10+20"
sum_val = sum([int(x) for x in addition_str.split('+')])


"""
Define a function which generates a list that contains complete email addresses (e.g.diana.prince @ gmail.com).The function receives a dictionary, which contains
domain names as keys, and a list of users as values.
"""


def email_list(domains):
    """generates a list that contains complete email addresses"""
    emails = []
    for domain, users in domains.items():
        for user in users:
            full_email = '{}@{}'.format(user, domain)
            emails.append(full_email)
    return emails


"""
Create a dictionary that keeps track of all the characters in the string and notes how many times
each character was seen.Then, find the key with the lowest value in this dictionary.
"""


str1 = "git add -p: allows a user to interactively review patches to add to the current commit"
d = {}
for char in str1:
    d[char] = d.get(char, 0) + 1
keys = list(d.keys())
min_value = keys[0]
for key in keys:
    if d[key] < d[min_value]:
        min_value = key

        
"""
If a filesystem has a block size of 4096 bytes, this means that a file consisting of only one byte
will still use 4096 bytes of storage.A file made up of 4097 bytes will use 4096 * 2 = 8192 bytes
of storage. Knowing this, define a function that calculates the total number of bytes needed to
store a file of a given size.
"""


def calculate_storage(filesize):
    """calculates the total amount of bytes needed to store a file of a given size"""
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = filesize % block_size
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return block_size * full_blocks


"""
The permissions of a file in a Linux system are split into three sets of three permissions: 
read, write, and execute for the owner, group, and others.Each of the three values can be expressed 
as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute.
Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
For example: 640 is read / write for the owner, read for the group, and no permissions for the others; 
converted to a string, it would be: "rw-r-----".Define a function that makes the code convert a 
permission in octal format into a string format.
"""


def octal_to_string(octal):
    """ makes the code convert a permission in octal format into a string format"""
    result = ''
    value_letters = [(4, 'r'), (2, 'w'), (1, 'x')]
    for num in [int(n) for n in str(octal)]:
        for value, letter in value_letters:
            if num >= value:
                result += letter
                num -= value
            else:
                result += '-'
    return result


"""
Define a function which prints all the prime factors of a number. 
A prime factor is a number that is prime and divides another without a remainder/
"""


def print_prime_factors(num):
    """prints all the prime factors of a number"""
    factor = 2
    while factor <= num:
        if num % factor == 0:
            print(factor)
            num = num/factor
        else:
            factor += 1
    return 'Done'


"""
Define a function so that it returns the sum of all the divisors of a number,
without including it. A divisor is a number that divides into another without a
remainder.
"""


def sum_divisors(n):
    """returns the sum of all the divisors of a number, without including it"""
    total_sum = 0
    d = 1
    while d < n:
        if n % d == 0:
            total_sum += d
            d += 1
        else:
            d += 1
    return total_sum


"""
Define a function which returns whether the number is a power of the given base. 
Base is assumed to be a positive number.
"""


def is_power_of(num, base):
    if num < base:
        return num == 1
    return is_power_of(num//base, base)
