from imports import *
from helpers import *
from metrics import *
from constants import *
from agent import *
from conors_secret_strategy import SingleAction #as strat
from actions import buy
import time


start_t = time.time()
run_length = timedelta(hours=0.05) 
portfolio_at_time_zero = {"USDC": Decimal(50_000), "WETH": Decimal(25), "ETH" : Decimal(1)}#, "PEPE":1_000_000_000} #"ETH": Decimal(100), #"WBTC" : Decimal(1),#"PEPE" : Decimal(1_000_000_000),}
echo_green(portfolio_at_time_zero,"initial_portfolio")
date_range=(start_time, end_time)
agents = [UniswapV3PoolWealthAgent(portfolio_at_time_zero,"gary the agent")]
agent1 = agents[0]
policy = SingleAction(agent1)
env = UniswapV3Env(chain, agents, date_range, pools, market_impact, backend_type)
backtest_run(
    env=env,
    policies=[policy],
    dashboard_server_port=6666,
    output_file="dollar_cost_averaging.db",
    auto_close=True,
    simulation_status_bar=True,
    simulation_title="Dollar Cost Averaging",
    simulation_description="Investing in regular intervals.",
    )
end_t = time.time()
echo_yellow(end_t - start_t,"absolute time")