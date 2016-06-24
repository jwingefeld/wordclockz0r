def combine_words(words,max_len=100):
    #print("\n")
    #for w in words:
    #    print(w)

    max_aval = 0
    max_a = [0,1]
    for a in range(len(words)-1):
        max_bval = 0
        max_b = a+1
        for b in range(a+1,len(words)):
            i=0
            max_i = 0
            while (i < len(words[a]) and i < len(words[b])):
                i=i+1
                if words[a][:i] == words[b][-i:] or words[a][-i:] == words[b][:i]:
                    #skip the match detection if the combination is too large
                    if (len(words[a]) + len(words[b]) - i) <= max_len:
                        max_i = i
                    #else:
                        #print("Max size reached, ignoring match.")
            if max_i > max_bval:
                max_bval = max_i
                max_b = b

            #print(words[a] + " vs " + words[b] + " score: " + str(max_i))
        #print("\nhigh score: " + str(max_bval) + " index: " + str(max_b) + "\n")
        if max_bval > max_aval:
            max_a = [a,max_b]
            max_aval = max_bval

    word_a = words[max_a[0]]
    word_b = words[max_a[1]]
    if word_a[:max_aval] == word_b[-max_aval:]:
        combined = word_b + word_a[max_aval:]
    elif word_b[:max_aval] == word_a[-max_aval:]:
        combined = word_a + word_b[max_aval:]
    else:
        #print("\n")
        #for w in words:
            #print(w)
        #print("returning a list")
        return words

    words.append(combined)
    del words[max_a[1]]
    del words[max_a[0]]
    if len(words) == 1:
        #print(words[0])
        return words[0]
    else:
        return combine_words(words,max_len)
if __name__ == '__main__':
    import sys
    combine_words(sys.argv[1:])
