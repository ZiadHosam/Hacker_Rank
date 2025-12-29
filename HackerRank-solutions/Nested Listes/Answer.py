if __name__ == '__main__':
    n=int(input())
    students=[]
    if 2<=n<=5:
        for i in range (n):
            name = input()
            score = float(input())
            students.append([name,score])
    students2=[]
    z = min(x[1] for x in students) 
    f=999
    for x in students:
        if f>=x[1]>z: f=x[1]
    for x in students:
        if x[1] == f:
            students2.append(x[0])

for student in sorted(students2):
    print(student)
