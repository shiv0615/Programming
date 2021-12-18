from collections import OrderedDict

def reverse_data(a, j= 4):
    return [a[j - len(a) + i] for i in range(len(a))]

def reverse_string(s):
    new_string = [s.split(' ')[i-1] for i in range(len(s.split(' ')),0,-1)]
    reverse = ''
    for i in range(len(new_string)):
        reverse += new_string[i] + ' '
    return reverse

def isomorphic_string(s,t):
    dict_s = OrderedDict()
    iso_string = ''
    if len(s) != len(t):
        print('Strings %s and %s are not ismorphic'%(s,t))
    else:
        i = 0
        consec_char = True
        for char_s, char_t in zip(s,t):
            dict_s[char_s] = char_t
            if i < len(s)-1:
                if s[i] == s[i+1]:
                    if t[i] != t[i+1]:
                        consec_char = False
                        print('Strings %s and %s are not ismorphic' % (s, t))
                        break
            i += 1
        if consec_char:
            for char_s in s:
                iso_string = iso_string + dict_s[char_s]
    return iso_string
if __name__ =='__main__':
    # a = [1,2,3,4,5,6]
    # print(a)
    # print(reverse_data(a, j=4))
    # print(reverse_string('the sky is blue'))
    print(isomorphic_string('foo', 'bar'))