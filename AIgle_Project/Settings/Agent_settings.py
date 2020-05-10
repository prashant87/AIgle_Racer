
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '7/02/2020'

##################################################################################################################


class Agent_settings:
    def gen_agent_settings(self):
        # --> Agent properties
        self.nb_agents = 1

        self.agent_min_move = 0         # Min move
        self.agent_max_move = 5         # Max move

        self.agent_min_speed = 10        # Min speed
        self.agent_max_speed = 16       # Max speed
        self.max_step = 20