class Environment:
	def __init__(self):
		self.current_state = (0, 0)
		self.final_state = (1, 1)
		self.init_next_states()
		self.init_rewards()

	def reset(self):
		self.current_state = (0, 0)
		self.final_state = (1, 1)

	def init_next_states(self):
		self.next_states = {}
		for state in [(0, 0), (0, 1), (1, 0), (1, 1)]:
			self.next_states[(state, "up")] = (state[0], max(1, state[1]))
			self.next_states[(state, "left")] = (max(0, state[0]), state[1])
			self.next_states[(state, "down")] = (state[0], max(0, state[1]))
			self.next_states[(state, "right")] = (max(1, state[0]), state[1])

	def init_rewards(self):
		self.rewards = {}
		self.rewards[(0, 0)] = -1.0
		self.rewards[(0, 1)] = -10.0
		self.rewards[(1, 0)] = -1.0
		self.rewards[(1, 1)] = 10.0

	def get_next_state(self, state, action):
		return self.next_states[(state, action)]

	def get_reward(self, state, action):
		return self.rewards[self.get_next_state(state, action)]

	def is_state_final(self, state):
		return (state == self.final_state)

	def is_game_finished(self):
		return self.is_state_final(self.current_state)
