import matplotlib.pyplot as plt

def initialise_plot(environment):
	plt.ion()
	fig = plt.figure(figsize=(10, 8))
	ax = plt.gca()
	plt.axes().set_aspect('equal')
	plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
	ax.axis('off')
	plot_grid_and_color_floors(ax, environment)
	plt.show()
	return plt, fig, ax

def plot_grid_and_color_floors(ax, environment):
	plot_lines_and_contours(ax, environment)
	for reward in environment.rewards:
		color = 'r' if environment.rewards[reward] < 0.0 else 'b'
		alpha = 0.2 if abs(environment.rewards[reward]) < 10.0 else 0.7
		color_floor(ax, reward[0], reward[0]+1, reward[1], reward[1]+1, color, alpha)

def plot_lines_and_contours(ax, environment):
	minx = environment.current_state[0]
	maxx = environment.final_state[0] + 1
	miny = environment.current_state[1]
	maxy = environment.final_state[1] + 1
	for row in range(maxx+1):
		plot_line_start_stop(ax, (minx, row), (maxx, row))
	for col in range(maxy+1):
		plot_line_start_stop(ax, (col, miny), (col, maxy))

def plot_line_start_stop(ax, start, stop):
	ax.plot([start[0],stop[0]], [start[1],stop[1]], linestyle="--", color="#000000")

def color_floor(ax, minx, maxx, miny, maxy, color, alpha):
	ax.fill([minx, maxx, maxx, minx], [miny, miny, maxy, maxy], color, alpha=alpha)

def plot_position(ax, environment):
	position = environment.current_state
	scatterplot = ax.scatter([position[0]+0.5], [position[0]+0.5], marker="o", c="g", s=250, alpha=1.0)
	plt.pause(0.05)
	return scatterplot

def update_position(fig, scatterplot, environment):
	position = environment.current_state
	scatterplot._offsets = [[position[0]+0.5, position[1]+0.5]]
	fig.canvas.draw()
	plt.pause(0.025)

def erase_position(scatterplot):
	scatterplot._offsets = []
