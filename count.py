

def count_char(text):
    # TODO count the number of times each character occurs in the text
    # and print out each character along with its count
    noDup = []
    for i in list(text):
        if i not in noDup:
            noDup.append(i)
    for i in noDup:
        print (i, text.count(i))
    pass

def count_char_insensitive(text):
    # TODO do the same as `count_char` but in a case-insensitive manner
    noDup = []
    for x in list(text.lower()):
        if x not in noDup:
            noDup.append(x)
    for i in noDup:
        print (i, text.lower().count(i))
    pass


def count_char_ordered(text):
    # TODO print the characters in the descending order of the count
    # HINT: lookup `sorted()` in the Python documentation
    
    # This task is quite difficult, so please feel free to make use of
    # noDupources online (Python docs, Stack Overflow, etc.)
    pass