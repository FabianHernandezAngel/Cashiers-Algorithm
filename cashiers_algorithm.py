def coin_change(change, denominations):
    total = 0
    coins = []
            
    for coin in reversed(denominations):
        while change >= coin:
            total += 1
            change -= coin
            coins.append(coin)
    return coins


if __name__ == "__main__":
    result = coin_change(48, [1,5,10,25,100])
    print(result)