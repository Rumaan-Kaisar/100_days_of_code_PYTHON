# ----------------------  DEBUGGING ------------------------

# Print is Your Friend
# Print every result to Narrow down the bug

"""
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

"""
# Notice the "word_per_page"  is using a logical equal sign "==". This is the bug
# Evaluated as True or False
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# print(word_per_page == int(input("Number of words per page: ")))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# python use_of_print.py