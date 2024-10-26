from imports import *
from metrics import *

# gaia
from helpers import *
from constants import *
from pyperclip import *
from decimal import Decimal
from typing import List, Optional
import os
import sys
from decimal import Decimal
from datetime import timedelta
from typing import Any, Optional
import shelve
from colorama import Fore, Style


#from agents.uniswapV3_pool_wealth import UniswapV3PoolWealthAgent
from dateutil import parser as dateparser
#from policy import DCAPolicy


#policy:
from dojo.actions.base_action import BaseAction
from dojo.actions.uniswapV3 import UniswapV3Trade
from dojo.agents import BaseAgent
from dojo.observations.uniswapV3 import UniswapV3Observation
from dojo.policies import BasePolicy

# agent
from decimal import Decimal
from typing import Optional

from dojo.agents import UniswapV3Agent
from dojo.environments.uniswapV3 import UniswapV3Observation

# backtest run & def env
from dojo.common.constants import Chain
from dojo.environments import UniswapV3Env
from dojo.runners import backtest_run


################################################################################################################################################################################################################
# ################################################################################# AGENT ABOVE #####################################################################################################
# ################################################################################################################################################################################################################ 


class UniswapV3PoolWealthAgent(UniswapV3Agent):
    """This agent implements a pool wealth reward function for a single UniswapV3 pool.

    The agent should not be given any tokens that are not in the UniswapV3Env pool.
    """

    def __init__(
        self, initial_portfolio: dict[str, Decimal], name: Optional[str] = None
    ):
        """Initialize the agent."""
        super().__init__(name=name, initial_portfolio=initial_portfolio)
        self.initial_portfolio = initial_portfolio        
        echo_cyan(self.initial_portfolio,"agents initial portfolio")
        echo_cyan(name,"agents_name")




    def reward(self, obs):
        """       if obs.block == 20129224:
            init_w = hodl_agent_wealth(obs, self.initial_portfolio)
            
            global welt
            welt = init_w
            echo_magenta(welt, "global welt set")
        else:
            init_w = welt 
            echo_magenta(init_w, "global welt set") """

        init_w = initial_agent_wealth(obs, self.initial_portfolio)
        current_w_HODL = HODL_agent_wealth(obs, self.initial_portfolio)
        current_w = current_agent_wealth(obs, self.erc20_portfolio())

        PnL = profit_n_loss(current_w, init_w)
        PnL_HODL = HODL_profit_n_loss(current_w_HODL, init_w)
        PnLP = profit_n_loss_percentage(current_w, init_w)
        PnLP_HODL = HODL_profit_n_loss_percentage(current_w_HODL, init_w)


        echo_magenta(init_w,"initial_wealth")
        echo_magenta(current_w_HODL,"HODL_current_wealth")
        echo_magenta(current_w, "current_wealth")
    
        echo_magenta(PnL, "PnL")
        echo_magenta(PnL_HODL, "PnL HODL")
        echo_magenta(PnLP, "PnL %")
        echo_magenta(PnLP_HODL, "PnL_HODL %")

        sig(PnL, "PnL", obs)
        sig(PnLP, "PnL_Percentage", obs)
        sig(init_w,"initial_wealth",obs)
        sig(PnLP_HODL,"PnL %",obs)
        sig(PnL_HODL,"PnL HODL %",obs)
        
        
        return  current_w #PnLP #obs.price(token="WETH",unit="USDC",pool="USDC/WETH-0.05")

################################################################################################################################################################################################################
# ################################################################################# AGENT ABOVE #####################################################################################################
# ################################################################################################################################################################################################################ 