def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)


def fact(n):
    if(n == 0 or n == 1):
        return 1
        else:
            return n * fact(n-1)

            print(fact(6))



#natural no
def cal_sum(n):
    if(n==0):
        return 0
    print(n)
   return cal_sum(n-1) + n
  sum =  cal_sum(5)
  print(sum)



#element in a list
def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango","apple","kiwi"]
print_list(fruits)