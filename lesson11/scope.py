name = "Dave"
count = 1

def another():
    color = "blue"
    global count # Declare we'll be using global variable
    count += 1

    print(count)
    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Meo")

another()
