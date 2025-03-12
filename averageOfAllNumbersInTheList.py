def calculateAvg(numbers:list)->float:

    try:
        sum = 0

        for i in numbers:    
            sum += i

        avg = sum/len(numbers)
        return avg
    
    except ZeroDivisionError as Z:
        return(f"cannot compute average of an empty list!, {Z}")

    except TypeError as T:
        return (f"All elements of the list must be numbers!, {T}")
    
    except Exception as E:
        return (f"An unexpected exception has occured!, {E}")
    




lst = []

print(calculateAvg(lst))

lst2 = [1,2,3,4,5]

print(calculateAvg(lst2))

lst3 = [1,2,'talha',4,5]

print(calculateAvg(lst3))