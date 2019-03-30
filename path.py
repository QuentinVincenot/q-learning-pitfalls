from environment import *
from agent import *
from visualisation import *


def train_AI_for_n_episodes(agent, environment, episodes=10):
	for i in range(episodes):
		run_episode(agent, environment, training=True)


def run_episode(agent, environment, training=False):
	environment.reset()
	while(environment.is_game_finished() == False):
		current_state = environment.current_state
		next_action = agent.choose_action(current_state)
		new_state, reward = agent.act_in_environment(environment, next_action)
		if training == True:
			agent.update_q_table(environment, current_state, next_action, new_state, reward)


agent = Agent()
environment = Environment()

train_AI_for_n_episodes(agent, environment, 100)

plt, fig, scatterplot = first_plot()

plt.pause(1.0)
update_plot(environment, plt, fig, scatterplot)
plt.pause(1.0)
