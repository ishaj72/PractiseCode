val = input("Enter the string: ")
def PalindromeString(yourval):
    length = len(yourval)
    flag = length -1
    assignBool = True
    for i  in range(length//2):
        if yourval[i] != yourval[flag]:
            assignBool = False
            break
            flag = flag -1
        
        if assignBool:
            print("String is palindrome")
        else :
            print("String is not palindrome")
    
PalindromeString(val)
        
