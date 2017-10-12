from ryotest import *

coins = [100, 50, 20, 10, 5, 2, 1]
usd_coins = [100, 50, 25, 10, 5, 1]

coins_avaliable=[
    [100, 20],
    [50, 20],
    [20, 20],
    [10, 20],
    [5, 20],
    [2, 20],
    [1, 20]
    ]
    

def get_change(amount, coins=usd_coins):

    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)    
    return change
    

    
# test_are_equal([], get_change(0))
# test_are_equal([1], get_change(1))
# test_are_equal([2], get_change(2))
# test_are_equal([5], get_change(5))
# test_are_equal([10], get_change(10))
# test_are_equal([20], get_change(20))
# test_are_equal([50], get_change(50))
# test_are_equal([100], get_change(100))
# test_are_equal([2, 1], get_change(3))
# test_are_equal([5, 2], get_change(7))

test_are_equal([25, 10], get_change(35)) 



print("all passed")