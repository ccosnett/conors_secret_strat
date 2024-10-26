from imports import *
from metrics import *
from helpers import *
import actions as act


class SingleAction(BasePolicy):  # type: ignore
    """A policy that executes a single action.

    This is useful for testing the impact of a single action in an environment. For
    example, you might want to see what the final price in a UniswapV3 pool would be if
    you executed a single swap.
    """

    def __init__(self, agent):
        """Initialize the policy.

        :param agent: The agent which is using this policy.
        :param action: The action to execute.
        """
        super().__init__(agent)
        echo_yellow("here")

        
        self.buy = act.buy(agent, "USDC/WETH-0.05", Decimal(100))
        self.sell = act.sell(agent, "USDC/WETH-0.05", Decimal(100))
        self.last_price = Decimal(0)

    def predict(self, obs):
        #p = self.agent.portfolio()
        #echo_red(self.agent.initial_portfolio,"init_p")
        #echo_red(p,"p")
        #echo_red(current_wealth(obs, p),"c_weal")
        #sig(initial_agent_wealth(obs,))

        
        

        buy = self.buy
        sell = self.sell
        x = self.last_price
        y = pric(obs)

        sig(x,'x',obs)
        sig(y,'y',obs)


        if x - y > Decimal(0.1):
            echo_yellow("price has dropped: buy!!!")
            self.last_price = y
            return []
        elif x - y < Decimal(0.1):
            #echo_yellow("price hasn't changed much: do nothing!!!")
            self.last_price = y
            return []
        else:
            echo_yellow("price has risen: sell!!!")
            self.last_price = y
            return [] 
        


        

    #def predict(self, obs):
#        return 1
