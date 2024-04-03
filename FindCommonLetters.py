firstStr = input("Enter the first string: ")
secondStr = input("Enter the second string: ")
def CountSimilarValues(string1 , string2):
    l = []
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string1[i] == string2[j] and string1[i] not in l : 
                print(string1[i])
                l.append(string1[i])
CountSimilarValues(firstStr,secondStr)
