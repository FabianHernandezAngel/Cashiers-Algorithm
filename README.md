# Cashier's Algorithm
This project demonstrates a Greedy implementation of the register's algorithm. Given an array of currency denominations, the algorithm first sorts the denominations and then repeatedly selects the largest coin that does not exceed the remaining amount until the change is fully returned.

# Example
Given the coin denominations: 1, 5, 10, 25, 100, and the change due: 48¢, the algorithm will print:
[25, 10, 10, 1, 1, 1]

# Limitations
This Greedy approach is not optimal for denominations that aren't factors of 5 or that fall between 50 and 100. For example, given the denominations 1, 3, 60, 100, and the change due of 120¢, the optimal solution would be [60, 60]. This algorithm would instead output: [100, 3, 3, 3, 3, 3, 3, 1, 1]. The algorithm also assumes that the array of coin denominations is sorted.

# Algorithm
```
def coin_change(change, denominations):
    total = 0
    coins = []
            
    for coin in reversed(denominations):
        while change >= coin:
            total += 1
            change -= coin
            coins.append(coin)
    return coins
```

# Time complexity
* ``for coin in reversed(denominations)`` iterates through all denominations once O(D)
* ``while change >= coin`` iterates for every coin added O(C)
* All other operations run in O(1)
* Run time is O(D + C)
