#print("rafsan\n".title()* 7)

count = 1
def printer(name):
    global count
    if count <=7:
        print(name)
        count +=1
        printer(name)

printer("Rafsan")