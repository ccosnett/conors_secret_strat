from datetime import timedelta

run_length = timedelta(hours=10)

from decimal import Decimal
from helpers import *
# Defining Environment which includes time
start_time = dateparser.parse("2024-06-20 00:00:00 UTC")
end_time = start_time + run_length
date_range=(start_time, end_time)
echo_green(run_length,"run_length")



   
# DEFINING INITIAL PORTFOLIO OF GARY

""" portfolio = {

     "USDC": Decimal(77777),
     "WETH": Decimal(77777),
     "ETH" : Decimal(7777),
     #"ETH": Decimal(100),
     #"WBTC" : Decimal(1),
     #"PEPE" : Decimal(1_000_000_000),
}
 """
#echo_green(portfolio,"initial_portfolio")
# pools=["USDC/WETH-0.05"]



pool0 = "USDC/WETH-0.05"
pool1 = "PEPE/USDC-1"
pool2 = "WBTC/USDC-0.3"

pools = [pool0, pool1, pool2]
#pools=["USDC/WETH-0.05","USDC/WETH-0.3"]
chain=Chain.ETHEREUM

backend_type="forked"
echo_cyan(backend_type,"backendtype")
market_impact="replay"
    


""" env = UniswapV3Env(
    pools,
    chain,
    agents=agents, 
    date_range=(start_time, end_time), 
    backend_type="forked", 
    market_impact="replay"
    )
 """# portfolio

