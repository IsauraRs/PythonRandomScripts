## This code returns the amount of coins and the denomination of each coin in order to get to the target amount

def make_change(target_amount):
    #Pence        Pounds
    #1,2,5,10,20, 1e, 2e
    denominations = [200,100,50,20,10,5,2,1]
    coin_count = 0
    values = []

    for coin in denominations:
        while target_amount >= coin:
            target_amount -= coin
            values.append(coin)
            coin_count += 1

    return coin_count , values


print(make_change(24))

print(make_change(163))