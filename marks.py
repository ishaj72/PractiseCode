if __name__ == '__main__':
    lis1= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis1.append([name,score])
        
    mark = float("inf")
    grades = []
    for x in lis1:
        grades.append(x[1])
        
    for y in grades:
        if y!= min(grades) and y < mark:
            mark = y
    lis1.sort()
    
    for x in lis1:
        if x[1] == mark:
            print(x[0])
