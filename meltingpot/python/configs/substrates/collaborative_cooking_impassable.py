# Copyright 2020 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Configuration for Collaborative Cooking: Impassable.

Example video: https://youtu.be/yn1uSNymQ_U

Players need to collaborate to follow recipes. They are separated by an
impassable kitchen counter, so no player can complete the objective alone.

The recipe they must follow is for tomato soup:
1.   Add three tomatoes to the cooking pot.
2.   Wait for the soup to cook (status bar completion).
3.   Bring a bowl to the pot and pour the soup from the pot into the bowl.
4.   Deliver the bowl of soup at the goal location.

This substrate is a pure common interest game. All players share all rewards.

Players have a `5 x 5` observation window.
"""

# pylint: disable=g-line-too-long
from meltingpot.python.configs.substrates import collaborative_cooking as base_config


def get_config():
  """Default config for training on collaborative cooking."""
  config = base_config.get_config("impassable")
  return config