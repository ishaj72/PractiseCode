def count_substring(string, sub_string):
    a = string.count(sub_string)
    return a
## this will not work for every case. For ex - DFGHYHYH

def count_substring(string, sub_string):
    ans = 0
    l = len(sub_string)
    for i in range(0, len(string)):
        if string[i : i+l] == sub_string:
            ans = ans+1
    return ans
## The above code works for every case
