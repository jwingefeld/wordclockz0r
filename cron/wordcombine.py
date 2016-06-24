def combine_words(words,max_len=100,pref_len=-1):
    #print("attempting to create words with max_size " + str(max_len))
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
                        #bonus points if you exactly meet the preferred length
                        if len(words[a]) + len(words[b]) - i == pref_len:
                            max_i = 100
                        else:
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
    if len(words) <= 1:
        return []
    word_a = words[max_a[0]]
    word_b = words[max_a[1]]
    #print("combining " + word_a + " and " + word_b)
    i=0
    matching = False
    while i < len(word_a) and i < len(word_b):
        if word_a[:i] == word_b[-i:]:
            combined = word_b + word_a[i:]
            matching = True
        elif word_b[:i] == word_a[-i:]:
            combined = word_a + word_b[i:]
            matching = True
        i = i+1

    if not matching:
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
