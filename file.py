with open("pratice.txt","w") as f:
    #  f.write("Hii everyone\nwe are learning File I/O\n")
    #  f.write("using java.\nI like programming in java.")

    data = f.read()
    new_data = data.replace("java","python")
    print(new_data)
    f.write(new_data)


word = "learning"
with open("pratice.txt","r") as f:
    data = f.read()
    if(data.find(word)!= -1):
        print("found")
    else:
        print("not found")


def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("pratice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data)
            print(line_no)
            return
            line_no +=1
    return -1
 check_for_line() 