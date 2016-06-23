from wordcombine import combine_words
import random
letters = "abcdefghijklmnopqrstuvwxyz"

def generate(array_in, min_size):
    i = 0
    array = array_in
    a = 0
    while a < len(array):
        if array[a] == '[':
            b = a+1
            while array[b] != ']':
                b = b+1
            for c in array[a+1:b]:
                print(c)
            print("combining")
            combined = combine_words(array[a+1:b])
            for c in combined:
                print c
            del array[a+1:b-2]
            if type(combined) is list:
                array = array[:a+1] + combined + array[a+2:]
            else:
                array.insert(a+1,combined)
        a = a + 1



    biggest_word = max(array, key=len)
    print("Biggest Word: " + biggest_word)

    letter_sum = 0
    for a in array:
        letter_sum = letter_sum + len(a)
        print("letter_sum = " + str(letter_sum))
    if len(biggest_word)**2 < letter_sum:
        n = len(biggest_word)
        while n**2 < letter_sum:
            n = n+1
            print("n = " + str(n))
        side_len = n
        print("side_len: " + str(side_len))
    else:
        side_len = len(biggest_word)

    if side_len < min_size:
        side_len = int(min_size)

    success = False
    while not success:
        row = 0
        col = 0

        string = ""
        spaces = True

        for a in array:
            if(a == "["):
                spaces = False
            elif(a == "]"):
                spaces = True
            else:
                if col+len(a) >  side_len:
                    row = row+1
                    for i in range(col,side_len):
                        string = string + random.choice(letters)
                    string = string + "\n" #remove this later
                    col = 0
                string = string + a
                col = col + len(a)
                if spaces:
                    if col < side_len:
                        string = string + random.choice(letters)
                        col = col+1
        #if adding spaces to our words pushed us above our limit, increase the size and try again
        if row < side_len:
            success = True
            #fill up the rest of the space with garbage
            print(side_len)
            for i in range(row, side_len):
                for j in range(col, side_len):
                    string = string + random.choice(letters)
                col = 0
                string = string + "\n" #remove this too
        else:
            print("failed side_len = "+ str(side_len))
            side_len = side_len+1

    print("\n Done. Size is: " + str(side_len) + "\n")
    print(string)

if __name__ == '__main__':
    import sys
    generate(sys.argv[2:],int(sys.argv[1]))
