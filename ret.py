def create_phone_number(n):
    number = "(012) 345-6789"
    print(number)
    i = 0
    for count in n:
        #print(f"Count: {count}")
        number = number.replace(str(i),str(count))
        print(f"Contador: {i} --- {number.replace(str(i),str(count))}")
        print(f"Count: {count}")
        i += 1
    return number

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

