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
	plot_lines_and_contours(ax)
	color_floor(ax, 0, 1, 0, 1, 'r', 0.2)
	color_floor(ax, 1, 2, 0, 1, 'r', 0.2)
	color_floor(ax, 2, 3, 0, 1, 'r', 0.2)
	color_floor(ax, 0, 1, 1, 2, 'r', 0.2)
	color_floor(ax, 1, 2, 1, 2, 'r', 0.7)
	color_floor(ax, 2, 3, 1, 2, 'r', 0.2)
	color_floor(ax, 0, 1, 2, 3, 'r', 0.2)
	color_floor(ax, 1, 2, 2, 3, 'r', 0.7)
	color_floor(ax, 2, 3, 2, 3, 'b', 0.7)

def plot_lines_and_contours(ax):
	plot_line_start_stop(ax, (0,0), (0,3))
	plot_line_start_stop(ax, (0,3), (3,3))
	plot_line_start_stop(ax, (3,3), (3,0))
	plot_line_start_stop(ax, (3,0), (0,0))
	plot_line_start_stop(ax, (1,0), (1,3))
	plot_line_start_stop(ax, (2,0), (2,3))
	plot_line_start_stop(ax, (0,1), (3,1))
	plot_line_start_stop(ax, (0,2), (3,2))

def plot_line_start_stop(ax, start, stop):
	ax.plot([start[0],stop[0]], [start[1],stop[1]], linestyle="--", color="#000000")

def color_floor(ax, minx, maxx, miny, maxy, color, alpha):
	ax.fill([minx, maxx, maxx, minx], [miny, miny, maxy, maxy], color, alpha=alpha)

def plot_position(environment, ax):
	position = environment.current_state
	return ax.scatter([position[0]+0.5], [position[0]+0.5], marker="o", c="g", s=250, alpha=1.0)

def update_position(environment, fig, scatterplot):
	position = environment.current_state
	scatterplot._offsets = [[position[0]+0.5, position[1]+0.5]]
	fig.canvas.draw()

def erase_position(scatterplot):
	scatterplot._offsets = []
