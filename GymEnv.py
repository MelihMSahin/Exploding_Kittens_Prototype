
from InputSystem import InputSystem
from Game import Game
from Player import Player
from Agent import CatAgent

from typing import Optional
import numpy as np
import gymnasium as gym


class ExplodingCatEnv(gym.Env):

    def __init__(self, game: Game = Game(2)):
        
        # Initialise the game
        self.game = game

        ''' Not relevant?
        # Define the agent and target location; randomly chosen in `reset` and updated in `step`
        self._agent_location = np.array([-1, -1], dtype=np.int32)
        self._target_location = np.array([-1, -1], dtype=np.int32)
        '''
        
        '''Old obs
        # Observations are dictionaries with the agent's and the target's location.
        # Each location is encoded as an element of {0, ..., `size`-1}^2
        self.observation_space = gym.spaces.Dict(
            {
                "agent": gym.spaces.Box(0, size - 1, shape=(2,), dtype=int),
                "target": gym.spaces.Box(0, size - 1, shape=(2,), dtype=int),
            }
        )'''
        
        self.observation_space = gym.spaces.Dict(
            {
                "last_cards_played": gym.spaces.Sequence(gym.spaces.Discrete(13, start=2)),
                "no_of_cards_left_in_deck": gym.spaces.Discrete(len(game.deck.deck), start=1),
                "no_of_cards_in_opp_hand": gym.spaces.Discrete(21, start=0),
                "no_of_nopes_in_hand": gym.spaces.Discrete(6, start=0),
                "no_of_defuses_in_hand": gym.spaces.Discrete(6, start=0),
                "hand": gym.spaces.Sequence(gym.spaces.Discrete(13, start=2)),
            }
        )

        # Actions are either to play a card (or draw with 2), or to select a position to put the defuse or whther to nope
        self.action_space = gym.spaces.Tuple(gym.spaces.Sequence((gym.spaces.Discrete(13, start=2))), gym.spaces.Discrete(len(self.game.deck.deck) + 1, start=0), gym.spaces.Discrete(2))
        
        def _get_obs(self):
            return {"last_cards_played": self.game.cards_played_last_turn, "": self._target_location}

        