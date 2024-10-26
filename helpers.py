# gaia
import pickle
from agent import *
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
import logging
#logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO) # is missing


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
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
# HELPER
#    )                             (                                           
# ( /(       (                     )\ )                      )                 
# )\())   (  )\          (   (    (()/(   (               ( /( (               
#((_)\   ))\((_)`  )    ))\  )(    /(_)) ))\   (      (   )\()))\   (    (     
# _((_) /((_)_  /(/(   /((_)(()\  (_))_|/((_)  )\ )   )\ (_))/((_)  )\   )\ )  
#| || |(_)) | |((_)_\ (_))   ((_) | |_ (_))(  _(_/(  ((_)| |_  (_) ((_) _(_/(  
#| __ |/ -_)| || '_ \)/ -_) | '_| | __|| || || ' \))/ _| |  _| | |/ _ \| ' \)) 
#|_||_|\___||_|| .__/ \___| |_|   |_|   \_,_||_||_| \__|  \__| |_|\___/|_||_|  
#              |_|                                                             

def echo(expr, label=None):
    """
    prints expr and returns expr
    """
    expr = str(expr)
    if label:
        print(f"{label}: {expr}")
    else:
        print(expr)
    return expr

#def print_red()

def echo_red(expr, label=None):
    """
    prints expr and returns expr
    """
    red = Fore.RED
    expr = str(expr)

    if label:
        print(red + f"{label} = {expr}" + Style.RESET_ALL)
    else:
        print(red + expr + Style.RESET_ALL)
    return expr

def echo_cyan(expr, label=None):
    """
    prints expr and returns expr
    """
    col = Fore.CYAN
    expr = str(expr)

    if label:
        print(col + f"{label} = {expr}" + Style.RESET_ALL)
    else:
        print(col + expr + Style.RESET_ALL)
    return expr

def echo_blue(expr, label=None):
    """
    prints expr and returns expr
    """
    col = Fore.BLUE
    expr = str(expr)

    if label:
        print(col + f"{label} = {expr}" + Style.RESET_ALL)
    else:
        print(col + expr + Style.RESET_ALL)
    return expr


def echo_green(expr, label=None):
    """
    prints expr and returns expr
    """
    col = Fore.GREEN
    expr = str(expr)

    if label:
        print(col + f"{label} = {expr}" + Style.RESET_ALL)
    else:
        print(col + expr + Style.RESET_ALL)
    return expr


def echo_magenta(expr, label=None):
    """
    prints expr and returns expr
    """
    col = Fore.MAGENTA
    expr = str(round(expr, 2))

    if label:
        print(col + f"{label} : $ {expr}" + Style.RESET_ALL)
    else:
        print(col + expr + Style.RESET_ALL)
    return expr


def echo_yellow(expr, label=None):
    """
    prints expr and returns expr
    """
    col = Fore.LIGHTYELLOW_EX
    expr = str(expr)

    if label:
        print(col + f"{label} = {expr}" + Style.RESET_ALL)
    else:
        print(col + expr + Style.RESET_ALL)
    return expr

def yellow(strin_expr):
    echo_yellow(eval(strin_expr), strin_expr)

def cop(text):
    """
    copies text to clipboard and then echo's it
    """
    copy(echo(text))
    pass


def print_block(obs):
    echo_yellow(obs.block)
    return obs.block

def sig(sig, name, obs):
    obs.add_signal(name, sig)
    return None



def globalize(obj, name):
    globals()[name] = obj


######### VARIABLES

start_time = dateparser.parse("2024-06-20 00:00:00 UTC")


#global global_observation
#global_observation = obs

def pickle_dump(objekt):
    fil = 'filename.pkl'
    with open('filename.pkl', 'wb') as file:
        pickle.dump(objekt, file)
    echo_cyan("object dumped! to "+ fil)


# Replace 'my_object' with the object you want to save

    
        