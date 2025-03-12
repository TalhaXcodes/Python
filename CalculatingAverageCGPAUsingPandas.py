import pandas as pd

x = pd.read_csv(r"C:\Users\HP\Desktop\python programs\students.csv")

# print(len(x))
s = 0
for i in range(len(x)):
    s = s + x['Cgpa'][i]

avg = s/len(x)

# print(f"The average Cgpa of the students is: {avg}")

s = x['Cgpa'].sum()
avg_2 = s/len(x)
print(f"The average Cgpa of the students is: {avg_2}")