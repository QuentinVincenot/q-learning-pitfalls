import random

class Agent:
	def __init__(self, learning_rate=0.5, actualisation_factor=0.9):
		self.epsilon = 1.0
		self.init_q_table()
		self.learning_rate = learning_rate
		self.actualisation_factor = actualisation_factor

	def init_q_table(self):
		self.q_table = {}
		for row in range(2):
			for col in range(2):
				for action in ["up", "left", "down", "right"]:
					self.q_table[((row, col), action)] = 0.0

	def choose_action(self, current_state):
		next_action = "up"
		random_number = random.random()
		if random_number < self.epsilon:
			next_action = self.choose_exploration()
		else:
			next_action = self.choose_exploitation(current_state)
		self.epsilon *= 0.985
		return next_action

	def choose_exploration(self):
		random_number = random.randint(0, 3)
		return ["up", "left", "down", "right"][random_number]

	def choose_exploitation(self, current_state):
		best_action = "up"
		best_q_value = self.q_table[(current_state, best_action)]
		for action in ["left", "down", "right"]:
			if self.q_table[(current_state, action)] > best_q_value:
				best_action = action
				best_q_value = self.q_table[(current_state, action)]
		return best_action

	def act_in_environment(self, environment, next_action):
		current_state = environment.current_state
		reward = environment.get_reward(current_state, next_action)
		environment.current_state = environment.get_next_state(current_state, next_action)
		return environment.current_state, reward

	def update_q_table(self, environment, old_state, action, new_state, reward):
		best_new_state_action = "up"
		best_new_state_q_value = self.q_table[(new_state, best_new_state_action)]
		for possible_action in ["left", "down", "right"]:
			new_state_q_value = self.q_table[(new_state, possible_action)]
			if new_state_q_value > best_new_state_q_value:
				best_new_state_action = possible_action
				best_new_state_q_value = new_state_q_value

		previous_knowledge = (1-self.learning_rate)*(self.q_table[(old_state, action)])
		learnt_knowledge = (self.learning_rate)*(reward + self.actualisation_factor*best_new_state_q_value)
		self.q_table[(old_state, action)] = previous_knowledge + learnt_knowledge
