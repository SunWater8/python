money = 1260
count = 0

coin_type = [500,100,50,10]
for coin in coin_type: #첫째 코인은 500
    count += money // coin
    money %= coin

print(count)
