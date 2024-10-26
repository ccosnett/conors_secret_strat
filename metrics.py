from imports import *
from decimal import Decimal
from helpers import *

global global_list
global_list = []


def removeETH(portfolio):
    erc20_port = portfolio
    erc20_port.pop('ETH',None)
    return erc20_port


def initial_agent_wealth(obs, initial_portfolio):
        if obs.block == 20129224:
            init_w = HODL_agent_wealth(obs, initial_portfolio)
            
            global welt
            welt = init_w
            #echo_magenta(welt, "global welt set")
        else:
            init_w = welt 
            #echo_magenta(init_w, "global welt set")
        
        return init_w


def current_agent_wealth(obs, portfolio):
    #echo_green(portfolio,"c w p")
    #dic = portfolio
    #dic.pop('ETH', None)

    #out1 = dic.items()
    erc20_portfolio = removeETH(portfolio)
    out1 = erc20_portfolio.items()
    echo_green(out1,"2")
    pool = obs.pools[0]
    pool_tokens = obs.pool_tokens(pool=pool)
        
    wealth = Decimal(0)   
    for token, quantity in out1:
        wealth += quantity * obs.price(token=token, unit=pool_tokens[0], pool=pool)
    return wealth


# def current_wealth(obs, agent):
#     """The agent wealth in units of asset y according to the UniswapV3 pool."""

    
#     out1 = agent.portolio().items()
#     pool = obs.pools[0]
#     pool_tokens = obs.pool_tokens(pool=pool)
        
#     wealth = Decimal(0)   
#     for token, quantity in out1:
#         wealth += quantity * obs.price(token=token, unit=pool_tokens[0], pool=pool)
#     return wealth

def HODL_agent_wealth(obs, initial_portfolio):
    echo('1')
        
    erc20_portfolio = removeETH(initial_portfolio)
    #echo_magenta(erc20_portfolio,"remov")

    pool = obs.pools[0]
    pool_tokens = obs.pool_tokens(pool=pool)

    itemz = erc20_portfolio.items()
    w = Decimal(0)
    for token, quantity in itemz:
#            echo_yellow([token, quantity],"token,quant")
        w = w + quantity * obs.price(token=token, unit=pool_tokens[0], pool=pool)

    out = w

    return out#float(out) #initial_erc20_portfolio.items()



def profit_n_loss(current_wealth, initial_wealth):
    out1 = current_wealth - initial_wealth
    out2 = out1
    return out2

def HODL_profit_n_loss(HODL_current_wealth, initial_wealth):
    out1 = HODL_current_wealth - initial_wealth
    out2 = out1
    return out2


def profit_n_loss_percentage(current_wealth, initial_wealth):
    out1 = 100*(current_wealth - initial_wealth)/initial_wealth
    return out1

def HODL_profit_n_loss_percentage(HODL_current_wealth, initial_wealth):
    out1 = 100*(HODL_current_wealth - initial_wealth)/initial_wealth
    return out1



def weth_price(obs, pool):
    echo('weth_price')
    out1 = obs.price('WETH','USDC','USDC/WETH-0.3')
    echo_cyan(out1, "obs.price('WETH','UDSC',"+pool+")")
    return out1

def pric(obs):
    echo('pric')
    return weth_price(obs, obs.pools[0])




