import time

def add_one(num):
    if (num >= 9):
        return num + 1
    total = num + 1
    print(total)

    return add_one(total)

mynewtotal = add_one(0)
print(mynewtotal)

def print_meo(count):
    if (count >= 20):
        return
    count += 1
    print("Ti em Yeu Meo rat " + "nhi" + count * "u" )
    time.sleep(1)
    
    return print_meo(count)

print_meo(0)