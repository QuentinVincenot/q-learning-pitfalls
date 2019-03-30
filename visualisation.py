import matplotlib.pyplot as plt

def first_plot():
	plt.ion()
	fig = plt.figure(figsize=(10, 8))
	ax = plt.gca()
	plt.axes().set_aspect('equal')
	plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
	ax.axis('off')
	ax.plot([0,0], [0,2], linestyle="--", color="#000000")
	ax.plot([0,2], [2,2], linestyle="--", color="#000000")
	ax.plot([0,2], [0,0], linestyle="--", color="#000000")
	ax.plot([2,2], [0,2], linestyle="--", color="#000000")
	ax.plot([1,1], [0,2], linestyle="--", color="#000000")
	ax.plot([0,2], [1,1], linestyle="--", color="#000000")
	ax.fill([0, 1, 1, 0], [0, 0, 1, 1], 'r', alpha=0.2)
	ax.fill([1, 2, 2, 1], [0, 0, 1, 1], 'r', alpha=0.7)
	ax.fill([0, 1, 1, 0], [1, 1, 2, 2], 'r', alpha=0.2)
	ax.fill([1, 2, 2, 1], [1, 1, 2, 2], 'b', alpha=0.7)
	scatterplot = ax.scatter([0.5], [0.5], marker="o", c="g", s=250, alpha=1.0)
	#ax.scatter([0.5], [1.5], marker="o", c="g", s=250, alpha=1.0)
	#ax.scatter([1.5], [0.5], marker="o", c="g", s=250, alpha=1.0)
	#ax.scatter([1.5], [1.5], marker="o", c="g", s=250, alpha=1.0)
	plt.show()
	return plt, fig, scatterplot

def update_plot(environment, plt, fig, scatterplot):
	scatterplot._offsets = [[1.5, 0.5]]
	fig.canvas.draw()
