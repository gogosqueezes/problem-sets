def main(): # main runs each function and then prints the total cost of the candies
    blue()
    blastoff()
    print(candy_shop())
    fruit_pricing()

def blue(): # assigns red a value and then multiplies that by 12, testing basics
    red = 3
    purple = red * 12
    print(purple)

def blastoff(): # uses a python for-loop to count down from the user's number to 1
    count = int(input("Please put in a countdown number!: "))
    for i in range (count, 0, -1):
        print (i)
    print ("blastoff!")

def candy_shop(): # combines an assigned candy list with an inputted candy list and calculates the cost of buying one of each candy.
    candies = ["milk duds", "twix", "m&ms"]
    candies.append("kitkat")
    candies.insert(1,"nerds")
    candies.sort()
    candies.remove("kitkat")
    print(candies)
    user_candies = []
    user_candies.append(input("What is your favorite candy?: "))
    user_candies.append(input("What is your second favorite candy?: "))
    user_candies.append(input("What is your third favorite candy?: "))
    all_candies = candies + user_candies
    print(len(all_candies))
    for candy in all_candies:
        print(candy)
    return (len(all_candies) * 1.25)

def fruit_pricing(): # Uses a python dictionary to store fruit prices and then calculates the cost of a shopping trip
    fruits ={
        "apple": 0.75, "banana": 1.25, "orange": 0.8, "peach": 2.25, "coconut": 2.80
    }
    fruits ["pear"] = 1.15
    print(fruits.get("peach"))
    for i in fruits:
        if fruits.get(i)>= 1.25:
            print(i)
    shoppingtrip = 3*fruits["apple"] + 2*fruits["banana"] + 1*fruits["coconut"]
    print(shoppingtrip)

main()