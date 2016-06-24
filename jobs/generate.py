#i am a machine that converts club mate into spaghetti code


from wordcombine import combine_words
from BinPacking import pack

import random
human_readable = False
letters = "abcdefghijklmnopqrstuvwxyz"

def generate(array_in, min_size, oversize):
    i = 0
    array = array_in
    biggest_word = max(array, key=len)
    #print("Biggest Word: " + biggest_word)

    a = 0
    while a < len(array):
        if array[a] == '[':
            b = a+1
            while array[b] != ']':
                b = b+1
            #for c in array[a+1:b]:
                #print(c)
            #print("combining")
            combined = combine_words(array[a+1:b],len(biggest_word)+oversize,len(biggest_word))
            #for c in combined:
                #print c
            del array[a+1:b-1]
            if type(combined) is list:
                array = array[:a+1] + combined + array[a+2:]
            else:
                array.insert(a+1,combined)
        a = a + 1

    biggest_word = max(array, key=len)
    #print("New Biggest Word: " + biggest_word)
    #print("Len Biggest Word: " + str(len(biggest_word)))
    a = 0
    while a < len(array):
        if array[a] == '[':
            b = a+1
            while array[b] != ']':
                b = b+1
            reordered = reorder(array[a+1:b],len(biggest_word))
            del array[a+1:b-1]
            if type(reordered) is list:
                array = array[:a+1] + reordered + array[a+2:]
            else:
                array.insert(a+1, reordered)
        a = a + 1

    letter_sum = 0
    side_len = 0
    for a in array:
        letter_sum = letter_sum + len(a)
        #print("letter_sum = " + str(letter_sum))
    if len(biggest_word)**2 < letter_sum:
        n = len(biggest_word)
        while n**2 < letter_sum:
            n = n+1
            #print("n = " + str(n))
        side_len = n
        #print("side_len: " + str(side_len))
    if side_len < len(biggest_word):
        side_len = len(biggest_word)
        #print("side len set to biggest word: " + str(side_len))

    if side_len < int(min_size):
        side_len = int(min_size)
        #print("side len set to min size: " + str(side_len))
    #for a in array:
        #print(a)
    #print("side len: " + str(side_len))
    success = False
    while not success:
        row = 0
        col = 0

        string = ""
        spaces = True

        for a in array:
            #print(a)
            if(a == "["):
                spaces = False
                #print("spaces disabled")
                if col > 0 and col < side_len:
                    #Add a final trailing space before space disabled block
                    string = string + random.choice(letters)
                    col = col+1
            elif(a == "]"):
                spaces = True
                #print("spaces enabled")
            else:
                if spaces:
                    if col > 0 and col < side_len:
                        #print("adding a space!")
                        string = string + random.choice(letters)
                        col = col+1
                if col+len(a) >  side_len:
                    row = row+1
                    for i in range(col,side_len):
                        string = string + random.choice(letters)
                    string = string + "\n" #remove this later
                    col = 0
                string = string + a
                col = col + len(a)
        #if adding spaces to our words pushed us above our limit, increase the size and try again
        if row < side_len:
            success = True
            #fill up the rest of the space with garbage
            #print(side_len)
            for i in range(row, side_len):
                for j in range(col, side_len):
                    string = string + random.choice(letters)
                col = 0
                string = string + "\n" #remove this too
        else:
            #print("failed side_len = "+ str(side_len))
            side_len = side_len+1

    #print("\n Done. Size is: " + str(side_len) + "\n")
    if human_readable:
        for i in range(side_len):
            print(string[side_len*i:side_len*i+side_len])
    #else:
        #print(string)

    return string


def reorder(array, max_size):
    #attempts to reorder an array so that the most words fit on one line
    length_array = []
    for a in array:
        length_array.append(len(a))

    bins = pack(length_array, max_size)
    new_arr = []
    for b in bins:
        new_arr.append("")
        for i in b.items:
            for a in array:
                if len(a) == i:
                    new_arr[-1] = new_arr[-1]+a
                    array.remove(a)
                    break
    #for i in new_arr:
    #    print(i)
    return new_arr


if __name__ == '__main__':
    import sys
    generate(sys.argv[2:],int(sys.argv[1]),1)
