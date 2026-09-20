#O(N2) time , O(N) space - Not optimal solution
systemA = [101, 102, 103, 104, 105]
systemB = [103, 104, 105, 106]
#Trades present in A but missing in B
#Trades present in B but missing in A
def reconcile_trades(systemA, systemB):
    b_absent= []
    a_absent = []
    for num in systemA:
        if num not in systemB:
            b_absent.append(num)
    for num in systemB:
        if num not in systemA:
            a_absent.append(num)
    return (b_absent, a_absent)

print(reconcile_trades(systemA, systemB))


#O(N +M) time, set insertion/look up is O(1) ,multiplied by n elements gives O(N) for setA + O(M) for setB gives O(N+M) time, space:
#O(N+M) Space, O(N) space for setA, O(M) for setB, setA-setB gives new space, and converting back to list.
systemA = [101, 102, 103, 104, 105]
systemB = [103, 104, 105, 106]
#Trades present in A but missing in B
#Trades present in B but missing in A
def reconcile_trades(systemA, systemB):
    setA = set(systemA)
    setB = set(systemB)
    b_absent = list(setA -setB)
    a_absent = list(setB - setA)
    return (b_absent, a_absent)

print(reconcile_trades(systemA, systemB))

#list(map(int, input().rstrip().split()))



#import heapq
#heapq.nlargest, heapq.nsmallest- Use for larger values. O(NLogK)
#sorted()- Use for smaller values. O(NLogN)

#heapq.nlargest(n, iterable, key=key)
#sorted(iterable, key=key, reverse =True/False)[:n]

#top_5_stocks = heapq.nlargest(5, stocks.items(), key = lambda x: x[1])
#top_5_largest_stocks=  sorted(stocks.tems(), key = lambda x: x[1], reverse = True)[:5]



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

#Additions

trades = [
    ("AAPL", +10),
    ("AAPL", -5),
    ("GOOG", +3),
    ("AAPL", -5),
    ("GOOG", -3),
    ("GOOG", 10)
]

def non_zero_net_trades(trades):
    net_trades ={}
    for symbol, value in trades:
        if symbol in net_trades:
            net_trades[symbol] += value
        else:
            net_trades[symbol] = value
    non_zero_net = {symbol:value
                    for symbol, value in net_trades.items()
                    if value != 0}
    return non_zero_net
print(non_zero_net_trades(trades))


def non_zero_net_trades(trades):
    net_trades ={}
    for symbol, value in trades:
        net_trades[symbol] = net_trades.get(symbol, 0) + value
    non_zero_net = {symbol: value for symbol, value in net_trades.items() if value != 0}
    return non_zero_net

print(non_zero_net_trades(trades))


("AAPL", 100)
("GOOG", 200)
("AAPL", -100)

class TradeAggregator:
    def __init__(self):
        self.net_trades = {}
    def add_trade(self, symbol, value):
        self.net_trades[symbol] = self.net_trades.get(symbol, 0) + value

    def get_positions(self):
        return {
            symbol: value 
            for symbol, value in self.net_trades.items()
            if value != 0
        }


agg = TradeAggregator()

agg.add_trade("AAPL", 100)
agg.add_trade("GOOG", 200)
agg.add_trade("AAPL", -100)

print(agg.get_positions())

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

#Solution 4
prices = [
 ("buy", 100),
 ("buy", 101),
 ("sell", 102),
 ("sell", 99),
]

def best_trades(prices):
    best_bid = max(price[1]  for price in prices if price[0] == "buy")
    best_ask = min(price[1]  for price in prices if price[0] == "sell")
    if best_bid > best_ask:
        net_profit = best_bid - best_ask
    
    return best_bid, best_ask, best_bid-best_ask, prices

print(best_trades(prices))



prices = [100, 101, 99, 102]
positions = [1, 1, -1, 0]

def running_pnl(prices, positions):
    PnL = 0
    for i in range(1, len(prices)):
        PnL += positions[i-1] * (prices[i]- (prices[i-1]))
    return PnL

print(running_pnl(prices, positions))
