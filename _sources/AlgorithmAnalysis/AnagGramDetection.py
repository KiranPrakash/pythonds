def checkoff_anagram(string1, string2):
    flag1 = True
    if len(string1) != len(string2):
        flag1 = False

    s2 = list(string2)

    i = 0

    while i<len(string1) and flag1:
        j= 0
        flag2=False
        while j<len(s2) and not flag2:
            if string1[i] == s2[j]:
                flag2 = True
            else:
                j = j+1
        if flag2:
            s2[j] = None

        else:
            flag1 = False

        i = i +1

    return flag1

def sort_compare_anagram(string1, string2):
    s1 = list(string1)
    s2 = list(string2)

    s1.sort()
    s2.sort()
    print(s1)

    if s1 == s2 :
        flag = True

    else :
        flag = False
    return flag

def count_and_compare_anagram(string1, string2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(string1)):
        pos = ord(string1[i])-ord('a')
        c1[pos] = c1[pos]+1

    for i in range(len(string2)):
        pos = ord(string2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    flag = True

    j = 0
    while j<26 and flag:
        if c1[j] == c2[j]:
            j = j +1
        else:
            flag = False

    return flag

#istrue=checkoff_anagram('python','atyphon')
#istrue=sort_compare_anagram('python','typhon')
istrue = count_and_compare_anagram('python', 'tayphoa')
print(istrue)