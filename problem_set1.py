def main():
    blue()
    blastoff()
    print(candy_shop())
    fruit_pricing()

def blue(): 
    red = 3
    purple = red * 3
    print(purple)

def blastoff():
    count = int(input("Please put in a countdown number!: "))
    for i in range (count, 0, -1):
        print (i)
    print ("blastoff!")

def candy_shop():
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
    for candy in all_candies:
        print(candy)
    return (len(all_candies) * 1.25)

def fruit_pricing():
    fruits ={
        "apple": 0.75, "banana": 1.25, "orange": 0.8, "peach": 2.25, "coconut": 2.80
    }
    fruits ["pear"] = 1.25
    fruits.get("peach")
    for i in fruits:
        if fruits.get(i)>= 1.25:
            print(i)
    shoppingtrip = 3*fruits["apple"] + 2*fruits["banana"] + 1*fruits["coconut"]
    print(shoppingtrip)

main()