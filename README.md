# Title
Assignment 1. Assignment - filters out top N cryptocurrencies by market capitalization

## Installation
PyPi

```bash
pip install pycoingecko
```
Source
```
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

## Usage

```
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

## Examples
The required parameters for each endpoint are defined as required (mandatory) parameters for the corresponding functions.
Any optional parameters can be passed using same names, as defined in CoinGecko API doc (https://www.coingecko.com/api/docs/v3)

Usage examples:
```# /simple/price endpoint with the required parameters
>>> cg.get_price(ids='bitcoin', vs_currencies='usd')
{'bitcoin': {'usd': 3462.04}}
```

```. bitcoin , $ 43414 , 819812618596
. ethereum , $ 3023.86 , 356920569982
. cardano , $ 2.22 , 71372515162
. tether , $ 1.0 , 69681179039
. binancecoin , $ 376.29 , 58313610871
```
