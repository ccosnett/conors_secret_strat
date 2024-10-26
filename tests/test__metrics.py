from decimal import Decimal
import pytest

# Assuming removeETH removes 'ETH' from the portfolio
def removeETH(portfolio):
    dic = portfolio.copy()
    dic.pop('ETH', None)
    return dic

# Mock observation class with necessary methods
class Observation:
    def __init__(self, pools, prices):
        self.pools = pools
        self.prices = prices  # Dict with keys as tuples (token, unit) and values as Decimal prices

    def pool_tokens(self, pool):
        return pool  # Assuming pool is a list of tokens

    def price(self, token, unit, pool):
        return self.prices.get((token, unit), Decimal(0))

# Function to be tested
def current_agent_wealth(obs, portfolio):
    erc20_portfolio = removeETH(portfolio)
    out1 = erc20_portfolio.items()
    pool = obs.pools[0]
    pool_tokens = obs.pool_tokens(pool=pool)
        
    wealth = Decimal(0)   
    for token, quantity in out1:
        wealth += quantity * obs.price(token=token, unit=pool_tokens[0], pool=pool)
    return wealth

# Test cases
def test_current_agent_wealth_basic():
    portfolio = {"USDC": Decimal(1), "WETH": Decimal(1)}
    pools = [['USDC', 'WETH']]
    prices = {('USDC', 'USDC'): Decimal(1),
              ('WETH', 'USDC'): Decimal(3000)}
    obs = Observation(pools, prices)
    expected_wealth = Decimal(1) * Decimal(1) + Decimal(1) * Decimal(3000)
    wealth = current_agent_wealth(obs, portfolio)
    assert wealth == expected_wealth

def test_current_agent_wealth_with_eth_token():
    portfolio = {"USDC": Decimal(1), "WETH": Decimal(1), "ETH": Decimal(2)}
    pools = [['USDC', 'WETH']]
    prices = {('USDC', 'USDC'): Decimal(1),
              ('WETH', 'USDC'): Decimal(3000)}
    obs = Observation(pools, prices)
   


from decimal import Decimal
import pytest

# Helper function to remove 'ETH' from the portfolio
def removeETH(portfolio):
    dic = portfolio.copy()
    dic.pop('ETH', None)
    return dic

# Mock Observation class with necessary methods
class Observation:
    def __init__(self, pools, prices):
        self.pools = pools  # List of pools
        self.prices = prices  # Dict with keys as tuples (token, unit) and values as Decimal prices

    def pool_tokens(self, pool):
        return pool  # Assuming pool is a list of tokens

    def price(self, token, unit, pool):
        return self.prices.get((token, unit), Decimal(0))

# Function to be tested
def HODL_agent_wealth(obs, initial_portfolio):
    erc20_portfolio = removeETH(initial_portfolio)
    pool = obs.pools[0]
    pool_tokens = obs.pool_tokens(pool=pool)

    w = Decimal(0)
    for token, quantity in erc20_portfolio.items():
        w += quantity * obs.price(token=token, unit=pool_tokens[0], pool=pool)
    return w

# Unit tests
def test_HODL_agent_wealth_basic():
    initial_portfolio = {"USDC": Decimal(1), "WETH": Decimal(1)}
    pools = [['USDC', 'WETH']]
    prices = {
        ('USDC', 'USDC'): Decimal(1),
        ('WETH', 'USDC'): Decimal(3000)
    }
    obs = Observation(pools, prices)
    expected_wealth = Decimal(1) * Decimal(1) + Decimal(1) * Decimal(3000)
    wealth = HODL_agent_wealth(obs, initial_portfolio)
    assert wealth == expected_wealth

def test_HODL_agent_wealth_with_eth_token():
    initial_portfolio = {"USDC": Decimal(1), "WETH": Decimal(1), "ETH": Decimal(2)}
    pools = [['USDC', 'WETH']]
    prices = {
        ('USDC', 'USDC'): Decimal(1),
        ('WETH', 'USDC'): Decimal(3000)
    }
    obs = Observation(pools, prices)
    expected_wealth = Decimal(1) * Decimal(1) + Decimal(1) * Decimal(3000)  # ETH is removed
    wealth = HODL_agent_wealth(obs, initial_portfolio)
    assert wealth == expected_wealth

def test_HODL_agent_wealth_different_quantities():
    initial_portfolio = {"USDC": Decimal(100), "WETH": Decimal(2)}
    pools = [['USDC', 'WETH']]
    prices = {
        ('USDC', 'USDC'): Decimal(1),
        ('WETH', 'USDC'): Decimal(3000)
    }
    obs = Observation(pools, prices)
    expected_wealth = Decimal(100) * Decimal(1) + Decimal(2) * Decimal(3000)
    wealth = HODL_agent_wealth(obs, initial_portfolio)
    assert wealth == expected_wealth

def test_HODL_agent_wealth_unknown_token():
    initial_portfolio = {"USDC": Decimal(1), "WETH": Decimal(1), "DAI": Decimal(50)}
    pools = [['USDC', 'WETH']]
    prices = {
        ('USDC', 'USDC'): Decimal(1),
        ('WETH', 'USDC'): Decimal(3000)
    }
    obs = Observation(pools, prices)
    # DAI has no price data, so its contribution is zero
    expected_wealth = Decimal(1) * Decimal(1) + Decimal(1) * Decimal(3000)
    wealth = HODL_agent_wealth(obs, initial_portfolio)
    assert wealth == expected_wealth

def test_HODL_agent_wealth_with_dai():
    initial_portfolio = {"USDC": Decimal(1), "WETH": Decimal(1), "DAI": Decimal(50)}
    pools = [['USDC', 'WETH', 'DAI']]
    prices = {
        ('USDC', 'USDC'): Decimal(1),
        ('WETH', 'USDC'): Decimal(3000),
        ('DAI', 'USDC'): Decimal(1)
    }
    obs = Observation(pools, prices)
    expected_wealth = (
        Decimal(1) * Decimal(1) +
        Decimal(1) * Decimal(3000) +
        Decimal(50) * Decimal(1)
    )
    wealth = HODL_agent_wealth(obs, initial_portfolio)
    assert wealth == expected_wealth

def test_HODL_agent_wealth_missing_price():
    initial_portfolio = {"USDC": Decimal(1), "WETH": Decimal(1)}
    pools = [['USDC', 'WETH']]
    prices = {('USDC', 'USDC'): Decimal(1)}  # WETH price is missing
    obs = Observation(pools, prices)
    expected_wealth = Decimal(1) * Decimal(1)  # Only USDC contributes
    wealth = HODL_agent_wealth(obs, initial_portfolio)
    assert wealth == expected_wealth

def test_HODL_agent_wealth_multiple_pools():
    initial_portfolio = {"USDC": Decimal(1), "WETH": Decimal(1)}
    pools = [['USDC', 'WETH'], ['USDC', 'DAI']]
    prices = {
        ('USDC', 'USDC'): Decimal(1),
        ('WETH', 'USDC'): Decimal(3000),
        ('DAI', 'USDC'): Decimal(1)
    }
    obs = Observation(pools, prices)
    # Only the first pool is used
    expected_wealth = Decimal(1) * Decimal(1) + Decimal(1) * Decimal(3000)
    wealth = HODL_agent_wealth(obs, initial_portfolio)
    assert wealth == expected_wealth   