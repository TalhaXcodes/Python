with open('employeedetails.txt','r',newline='') as f:
    x = f.readlines()
    f.seek(0)
    amount = 0
    print(f"The employee data is:\n ")
    for i in x:
        print(i)

    for line in f:
        lst = line.split(',')
        amount += int(lst[2])    
    print(f"""\nThe average salary of all the employees is: {amount/len(x)}""")    