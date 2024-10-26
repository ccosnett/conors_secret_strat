
from imports import *

def buy(agent, pool, amount):
    
    out1 = UniswapV3Trade(
                        agent=agent,
                        pool=pool,
                        quantities=(amount, Decimal(0))
                        )

    return out1

def buy_weth(agent, pool, amount):
    
    out1 = UniswapV3Trade(
                        agent=agent,
                        pool=pool,
                        quantities=(amount, Decimal(0))
                        )

    return out1

def sell(agent, pool, amount):
    
    out1 = UniswapV3Trade(
                        agent=agent,
                        pool=pool,
                        quantities=(-amount, Decimal())
                        )

    return out1


def sell_weth(agent, pool, amount):
    
    out1 = UniswapV3Trade(
                        agent=agent,
                        pool=pool,
                        quantities=(amount, Decimal(0))
                        )

    return out1

#action1 = UniswapV3Trade(agent=self.agent, pool=pool, quantities=(Decimal(self.buying_amount), Decimal(0)))
            