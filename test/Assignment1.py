from pycoingecko import CoinGeckoAPI
from operator import itemgetter
cg = CoinGeckoAPI()
#n = input("num of crypcoins: ")
n = 5
coins = cg.get_coins_markets('usd')
coins_sorted = sorted(coins, key=itemgetter('market_cap'), reverse=True)
for i in range(n):
    coin = coins[i]
    print(".",coin['id'],",","$", coin['current_price'],",", coin['market_cap'])
 