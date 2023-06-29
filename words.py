# words = ["hello", "world", "python "]
# for word in words:
#     print(word.upper())

# # def print_upper_words(words):
# #     """Print every word in UPPERCASE"""
# #     for word in words:
# #         print(word.upper())

# # def print_upper_words(words):
# #     """Print words that start with 'e' in all uppercase"""
# #     for word in words:
# #         if word.startswith('e') or word.startswith('E'):
# #             print(word.upper())

def print_upper_words(words, must_start_with):
    """Print words that start with specific letters in UPPERCASE"""
    for word in words:
        if word.startswith(tuple(must_start_with)): #tuple is ordered collection 
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})
# Result should = 
# HELLO
# HEY
# YO 
# YES
