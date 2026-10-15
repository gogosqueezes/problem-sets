def main():
    blue()
    blastoff()
    print(candy_shop())

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
main()