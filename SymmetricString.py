val = input("Enter the string: ")
def symmetry(yourval):
    length = len(yourval) # taking the length of the string
    if length%2 ==0 : # if length then split the string into two parts using slicing 
        mid=length//2
        substr1 = yourval[:mid] 
        substr2 = yourval[mid:]
        if substr1 == substr2: # checking if two parts are equal or not
            print("The string is symmetrical")
        else:
            print("The string is not symmetrical")
    else:
            print("The string is not symmetrical")
            
symmetry(val)
