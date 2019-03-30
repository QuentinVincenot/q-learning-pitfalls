from environment import *
from agent import *
from visualisation import *


def train_AI_for_n_episodes(agent, environment, fig, ax, episodes=10):
	for i in range(episodes):
		run_episode(agent, environment, fig, ax, training=True)


def run_episode(agent, environment, fig, ax, training=False):
	environment.reset()
	scatterplot = plot_position(environment, ax)
	plt.pause(0.1)
	while(environment.is_game_finished() == False):
		current_state = environment.current_state
		next_action = agent.choose_action(current_state)
		new_state, reward = agent.act_in_environment(environment, next_action)
		update_position(environment, fig, scatterplot)
		plt.pause(0.05)
		if training == True:
			agent.update_q_table(environment, current_state, next_action, new_state, reward)
	erase_position(scatterplot)


agent = Agent(learning_rate=0.5, actualisation_factor=0.9)
environment = Environment()

plt, fig, ax = initialise_plot()
train_AI_for_n_episodes(agent, environment, fig, ax, 100)
