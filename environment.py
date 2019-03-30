class Environment:
	def __init__(self):
		self.reset()
		self.init_next_states()
		self.init_rewards()

	def reset(self):
		self.current_state = (0, 0)
		self.final_state = (2, 2)

	def generate_all_possible_states(self):
		possible_states = []
		for row in range(3):
			for col in range(3):
				possible_states += [(row, col)]
		return possible_states

	def init_next_states(self):
		self.next_states = {}
		for state in self.generate_all_possible_states():
			self.next_states[(state, "up")] = (state[0], min(2, state[1]+1))
			self.next_states[(state, "left")] = (max(0, state[0]-1), state[1])
			self.next_states[(state, "down")] = (state[0], max(0, state[1]-1))
			self.next_states[(state, "right")] = (min(2, state[0]+1), state[1])

	def init_rewards(self):
		self.rewards = {}
		self.rewards[(0, 0)] = -1.0
		self.rewards[(0, 1)] = -1.0
		self.rewards[(0, 2)] = -1.0
		self.rewards[(1, 0)] = -1.0
		self.rewards[(1, 1)] = -10.0
		self.rewards[(1, 2)] = -10.0
		self.rewards[(2, 0)] = -1.0
		self.rewards[(2, 1)] = -1.0
		self.rewards[(2, 2)] = 10.0

	def get_next_state(self, state, action):
		return self.next_states[(state, action)]

	def get_reward(self, state, action):
		return self.rewards[self.get_next_state(state, action)]

	def is_state_final(self, state):
		return (state == self.final_state)

	def is_game_finished(self):
		return self.is_state_final(self.current_state)
