from mock_data import catalog

def print_catalog_total (list):
    total=0
    for item in list:
        # print (item["price"]) testing to see if we are grabbing the prices from the dictionary we called catalog
        total+=item["price"]
    # print ("The total of the catalog is: " + str(total))  Alternative option but the f...{} solution seems more user friendly as you can type after with less code.
    print (f"The total of the catalog is: {total}")

print_catalog_total(catalog)















def say_hello():
    print ("Hello!")

def print_the_sum(a,b):
    print (a+b)

def print_the_division(a,b):
    if b == 0:
        print ("Cannot divide by zero")
    else:
        print (a/b)

def print_the_cheaper(a,b):

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("The variable is not a number.")
        return
    elif a<b:
        print (a)
    elif b<a:
        print (b)
    else:
        print ("bro, these are equal")


def print_all_numbers (nums):
    for i in nums:
        print (i)

def print_the_total_sum (nums):
    sum=0
    for i in nums:
        sum=(sum+i)
        # total += i  ***Shortcut***
    print(sum)

def sum_greater_than (nums,greater):
    sum=0
    for i in nums:
        if i >greater:
            sum += i
        # total += i  ***Shortcut***
    print(sum)

def count_less_than (nums,lesser):
    sum=0
    for i in nums:
        if i <=lesser:
            sum += 1
    print(sum)




# say_hello()
# print_the_sum (5,1)
# print_the_division(23,0)
# # print_the_cheaper(5,e)
# # print_all_numbers([47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21])
# print_the_total_sum([47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21])
# sum_greater_than([47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21],40)
# count_less_than([47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21],50)


