heroes = ["thor","batman","spiderman","ironman"]
def print_len(list):
    print(len(list))
    def print_list(list):
        for item in list:
            print(item, end =" ")

            print_list(heroes)



#fact
n=5
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
        print(fact)
        cal_fact(5)



#covert usd to inr
def convertor(usd_val):
    inr_val = usd_val *83
    print(usd_val, "USD=", inr_val, "INR")

    convertor(1)


