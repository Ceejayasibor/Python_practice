
'''
import heapq
heapq.nlargest, heapq.nsmallest- Use for smaller values.
sorted()- Use for larger values.

heapq.nlargest(n, iterable, key=key)
sorted(iterable, key=key, reverse =True/False)[:n]

top_5_stocks = heapq.nlargest(5, stocks.items(), key = lambda x: x[1])
top_5_largest_stocks=  sorted(stocks.tems(), key = lambda x: x[1], reverse = True)[:5]

'''

trades = [
    ("AAPL", +70),
    ("AAPL", -5),
    ("GOOG", +3),
    ("AAPL", -5),
    ("GOOG", -3),
    ("META", 120),
    ("TSLA", -20),
    ("PLNTR", 160)
]
k = 3

import heapq
def get_top_k_positions(trades, k):
    net_trades ={}
    for symbol,value in trades:
        net_trades[symbol] = net_trades.get(symbol, 0) + value
    non_zero_trades = {}
    for symbol, value in net_trades.items():
        if value != 0:
            non_zero_trades[symbol] = value
    top_k_positions = heapq.nlargest(k, non_zero_trades.items(), key = lambda x: x[1])
    return dict(top_k_positions)

print(get_top_k_positions(trades, k))

trades = [
    ("AAPL", +70),
    ("AAPL", -5),
    ("GOOG", +3),
    ("AAPL", -5),
    ("GOOG", -3),
    ("META", 120),
    ("TSLA", -20),
    ("PLNTR", 160)
]
k = 3


from collections import defaultdict
def get_top_k_positions(trades, k):
    net_trades = defaultdict(int)

    for symbol,value in trades:
        net_trades[symbol] += value
    # return dict(net_trades)

    non_zero_trades = {s:v for s, v in net_trades.items() if v != 0}

    top_k_positions = sorted(non_zero_trades.items(), key = lambda x: x[1], reverse = True)[:k]

    return dict(top_k_positions)

print(get_top_k_positions(trades, k))


#Solution 1

prices = [
 ("buy", 100),
 ("buy", 101),
 ("sell", 102),
 ("sell", 99),
]

def best_trades(prices):
    best_bid_tuple = max(price for price in prices if price[0] == 'buy')
    best_ask_tuple = min(price for price in prices if price[0] == 'sell')

    if not best_bid_tuple or not best_ask_tuple:
        return None, None, 0
    
    best_bid = best_bid_tuple[1]
    best_ask =best_ask_tuple[1]

    if best_bid >= best_ask:
        net_profit = best_bid - best_ask
        prices.remove(best_bid_tuple)
        prices.remove(best_ask_tuple)
    else:
        print('No profitable trades.')
    
    return best_bid, best_ask, net_profit, prices

result = best_trades(prices)
print("Best Bid:", result[0])
print("Best Ask:", result[1])
print("Net Profit:", result[2])
print("Prices:", result[3])

#Solution 2
   
prices = [
 ("buy", 100),
 ("buy", 101),
 ("sell", 102),
 ("sell", 99),
]

def best_trades(prices):
    best_bid = float('-inf')
    best_ask = float('inf')

    for action, price in prices:
        if action =='buy':
            best_bid = max(price, best_bid)
        else:
            best_ask = min(price, best_ask)

    if best_bid == float('-inf') or best_ask == float('inf'):
        return None, None, 0
    
   
    
    return best_bid, best_ask, max(0, best_bid-best_ask), prices

result = best_trades(prices)
print("Best Bid:", result[0])
print("Best Ask:", result[1])
print("Net Profit:", result[2])
print("Prices:", result[3])


#Solution 3
prices = [
 ("buy", 100),
 ("buy", 101),
 ("sell", 102),
 ("sell", 99),
]

def order_book(prices):
    buys = []
    sells = []

    for action, price in prices:
        if action == "buy":
            buys.append(price)
        else:
            sells.append(price)

        if buys and sells:
            best_bid = max(buys)
            best_ask = min(sells)

            if best_bid >= best_ask:
                print(f"Trade executed at {best_ask}")
                buys.remove(best_bid)
                sells.remove(best_ask)

    return best_bid, best_ask, best_bid-best_ask, prices



result = order_book(prices)
print("Best Bid:", result[0])
print("Best Ask:", result[1])
print("Net Profit:", result[2])
print("Prices:", result[3])
'''
    for action, price_point in prices:
        if action == 'buy':
            best_bid = max(prices, key = lambda x: x[1])
        elif action == 'sell':
            best_ask = min(prices, key = lambda x: x[1])
    if best_bid > best_ask:
        net_profit = best_bid.price() - best_ask.price()
    best_trades = ['best_bid =', best_bid, 'best_ask =', best_ask, 'net_profit =', net_profit]
    return best_trades
'''



prices = [100, 101, 99, 102]
positions = [1, 1, -1, 0]

def running_pnl(prices, positions):
    PnL = 0
    for i in range(1, len(prices)):
        PnL += positions[i-1] * (prices[i]- (prices[i-1]))
    return PnL

print(running_pnl(prices, positions))
#Explain how this is running PnL as it doesn't tell if these are buys/sales, or is position representing buy/sell or number of units.
# To loop through different loops separately, use zip- for i, j in zip(price, positions)


#Dice EV Decision (classic)
'''You roll a die:

you can stop anytime
if you roll 1 → lose everything
❓ Task:

Simulate and find optimal stopping threshold

👉 Same structure, different ruin condition'''

import random
def simulate_game(iterations, stop_threshold):
    total_simulations_score = 0

    for game in range(iterations):
        game_score = 0

        while True:
            roll = random.randint(1,6)
            if roll == 1:
                game_score = 0
                break
            else:
                game_score+=roll

            if game_score >= stop_threshold:
                break

        total_simulations_score += game_score
    
    return total_simulations_score/iterations

for stop_threshold in range (1,5):
    avg = simulate_game(1000000, stop_threshold)
    print(stop_threshold, avg)

#After running this, optimal stopping threshold is between 19 and 21, preferably between 19 and 20.

'''

🧪 Problem 5 — Streaming Problem (VERY COMMON)

Given stream:

[1,2,3,4,5,6,...]
❓ Task:

Maintain:

rolling average
rolling variance

👉 Tests:

incremental updates
no recomputation
🧪 Problem 6 — Market Impact Simulation

You buy shares:

price increases by 0.1 per unit bought
❓ Task:

Simulate cost of buying N shares

👉 Tests:

loops
accumulation
modeling'''


class RunningStats:
    def __init__(self):
        self.n = 0
        self.mean = 0
        self.M2 = 0

    def update(self, x):
        self.n += 1
        delta = x - self.mean
        self.mean += delta / self.n
        delta2 = x - self.mean
        self.M2 += delta * delta2

    def get_mean(self):
        return self.mean

    def get_variance(self):
        if self.n < 2:
            return 0
        return self.M2 / (self.n - 1)