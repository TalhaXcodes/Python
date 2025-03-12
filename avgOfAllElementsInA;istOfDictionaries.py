values = [{'a':1,'b':5},{'a':2,'b':50},{'a':32,'b':50},{'a':42,'b':50},{'a':92,'b':50},{'a':12,'b':50},{'a':20,'b':50},{'a':28,'b':50},{'a':27,'b':50},{'a':200,'b':50},{'a':202,'b':50}]

sum_1 = 0
sum_2 = 0

for i in values:
    sum_1 = sum_1 + i['a']
    sum_2 = sum_2 + i['b']

total = sum_1 + sum_2
avg = total/len(values)

print(f"The average value of all the elements is: {avg}")