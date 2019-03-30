import numpy as np

class Environment:
	def __init__(self, rows=2, cols=2):
		self.grid_size = (rows, cols)
		self.current_state = (1, 0)
		self.final_state = (0, 1)
		self.init_next_states()
		self.init_rewards()

	def init_next_states(self):
		self.next_states = {}
		self.next_states[((0, 0), "up")] = (0, 0)
		self.next_states[((0, 0), "left")] = (0, 0)
		self.next_states[((0, 0), "down")] = (1, 0)
		self.next_states[((0, 0), "right")] = (0, 1)
		self.next_states[((0, 1), "up")] = (0, 1)
		self.next_states[((0, 1), "left")] = (0, 0)
		self.next_states[((0, 1), "down")] = (1, 1)
		self.next_states[((0, 1), "right")] = (0, 1)
		self.next_states[((1, 0), "up")] = (0, 0)
		self.next_states[((1, 0), "left")] = (1, 0)
		self.next_states[((1, 0), "down")] = (1, 0)
		self.next_states[((1, 0), "right")] = (1, 1)
		self.next_states[((1, 1), "up")] = (0, 1)
		self.next_states[((1, 1), "left")] = (1, 0)
		self.next_states[((1, 1), "down")] = (1, 1)
		self.next_states[((1, 1), "right")] = (1, 1)

	def init_rewards(self):
		self.rewards = {}
		self.rewards[(0, 0)] = -1.0
		self.rewards[(0, 1)] = 10.0
		self.rewards[(1, 0)] = -1.0
		self.rewards[(1, 1)] = -10.0

	def get_next_state(self, state, action):
		return self.next_states[(state, action)]

	def get_reward(self, state, action):
		return self.rewards[self.get_next_state(state, action)]

	def is_state_final(self, state):
		return (state == self.final_state)

	def is_game_finished(self):
		return self.is_state_final(self.current_state)
