from quotes import quote_collection
import random

# TODO : Generating the program to update the list day by day


length_of_list = len(quote_collection)
index_value = random.randint(0,length_of_list)
# print(quote_collection[index_value])
print(quote_collection[index_value]["quote"])
print(quote_collection[index_value]["author"])


# TODO: updating the value in database


# TODO: Day count updation with the quotes

# TODO: money saved counts




"""
Skills required:

postgres
sql

"""