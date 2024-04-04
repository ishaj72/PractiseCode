list1 = ["whale",2,"elephant",7]
def ListToDictionaries(list1):
    new_list = []
    ref_list = ["name","id"]
    for i in range( 0 , len(list1) , 2 ):
        new_list.append({ref_list[0] : list1[i] , ref_list[1] : list1[i+1]})
    return new_list
print(ListToDictionaries(list1))
