__author__ = 'Ayla'
#1. Write a program that asks for a users email address.
#2. Pass this email address, as a string, to a function that uses a tuple to split the email address into username, domain, and generic
#top level domain (gTLD - .com, .gov, .edu, .org, .mil, .net).
#3. Make sure your functions tests that they have provided a proper email address format: it must have an @ symbol and a
#. followed by a proper gTLD. For this assignment a proper gTLD is .com, .gov, .edu, .org, .mil, or .net, the actual list
#of proper gTLD's is much longer.
#4. Your function should return the username, domain, and gTLD as a tuple

emailaddress=input('Input an email address')
gTLD=['gov','mil','org','com','net','edu']
try:
    username,domain =emailaddress.split('@')
    domain,generictoplevel=domain.split('.')
    print(username)
    print(domain)

    if generictoplevel in gTLD:
        print(generictoplevel)
    else:
        print('wrong email address')
except ValueError:
    print('not a valid email address')
















# tuples are immutable and organized (,), non-negative integers
#lists are mutable are organized [], non-negative integers
#dictionaries are mutable not organized {}, keys (general)