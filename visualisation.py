import matplotlib.pyplot as plt

def initialise_plot():
	plt.ion()
	fig = plt.figure(figsize=(10, 8))
	ax = plt.gca()
	plt.axes().set_aspect('equal')
	plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
	ax.axis('off')
	plot_grid_and_color_floors(ax)
	plt.show()
	return plt, fig, ax

def plot_grid_and_color_floors(ax):
	ax.plot([0,0], [0,2], linestyle="--", color="#000000")
	ax.plot([0,2], [2,2], linestyle="--", color="#000000")
	ax.plot([0,2], [0,0], linestyle="--", color="#000000")
	ax.plot([2,2], [0,2], linestyle="--", color="#000000")
	ax.plot([1,1], [0,2], linestyle="--", color="#000000")
	ax.plot([0,2], [1,1], linestyle="--", color="#000000")
	ax.fill([0, 1, 1, 0], [0, 0, 1, 1], 'r', alpha=0.2)
	ax.fill([1, 2, 2, 1], [0, 0, 1, 1], 'r', alpha=0.2)
	ax.fill([0, 1, 1, 0], [1, 1, 2, 2], 'r', alpha=0.7)
	ax.fill([1, 2, 2, 1], [1, 1, 2, 2], 'b', alpha=0.7)

def plot_position(environment, ax):
	position = environment.current_state
	return ax.scatter([position[0]+0.5], [position[0]+0.5], marker="o", c="g", s=250, alpha=1.0)

def update_position(environment, fig, scatterplot):
	position = environment.current_state
	scatterplot._offsets = [[position[0]+0.5, position[1]+0.5]]
	fig.canvas.draw()

def erase_position(scatterplot):
	scatterplot._offsets = []
