from imports import *
from decimal import Decimal
from helpers import *

global global_list
global_list = []


def removeETH(portfolio):
    erc20_port = portfolio
    erc20_port.pop('ETH',None)
    return erc20_port


def initial_agent_wealth(obs, agent):
        if obs.block == 20129224:
            init_w = tw(obs, agent)
            
            global welt
            welt = init_w
            #echo_magenta(welt, "global welt set")
        else:
            init_w = welt 
            #echo_magenta(init_w, "global welt set")
        
        return init_w


def current_agent_wealth(obs, agent):
    return tw(obs, agent)
    
def HODL_agent_wealth(obs, agent):
    
    return tw_p(obs, agent.initial_portfolio)

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
    out1 = obs.price('WETH','USDC','USDC/WETH-0.05')
    echo_cyan(out1, "obs.price('WETH','UDSC',"+pool+")")
    return out1

def pric(obs):
    echo('pric')
    return weth_price(obs, obs.pools[0])


def holdings(agent):
    return agent.erc20_portfolio()

def portfol(agent):
    return agent.erc20_portfolio()


def conversions(obs):
    #pools =  obs.pools
    d = {}
    d["WBTC/WETH-0.05"] = obs.price('WBTC', 'WETH', "WBTC/WETH-0.05")
    d["USDC/WETH-0.05"] = obs.price('USDC', 'WETH', 'USDC/WETH-0.05')
    return d


def total_wealth(portfolio, conversions):

    echo_yellow(portfolio,'portfolio')
    # Compute USDC per WETH
    USDC_per_WETH = 1 / conversions['USDC/WETH-0.05']  # 1 / 0.000280
    # USDC_per_WETH = 3571.4285714285716

    # Compute USDC per WBTC
    WETH_per_WBTC = conversions['WBTC/WETH-0.05']  # 18.3
    USDC_per_WBTC = WETH_per_WBTC * USDC_per_WETH  # 18.3 * 3571.4285714285716

    # Now compute total wealth
    total_USDC = portfolio.get('USDC', 0)
    total_USDC += portfolio.get('WETH', 0) * USDC_per_WETH
    total_USDC += portfolio.get('WBTC', 0) * USDC_per_WBTC

    print("Total wealth in USDC:", total_USDC)


    #out1 = total_wealth(portfolio, conversions)
    return total_USDC


def tw(obs, agent):
    portf = portfol(agent)
    convers = conversions(obs)
    return total_wealth(portf, convers)

def tw_p(obs, p):
    portf = p
    convers = conversions(obs)
    return total_wealth(portf, convers)






