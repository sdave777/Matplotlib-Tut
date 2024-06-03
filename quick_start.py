import matplotlib.pyplot as plt
import numpy as np
## commented out the below code to avoid clutter, all this is taken from https://matplotlib.org/stable/users/explain/quick_start.html

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
# fig = plt.figure()  # Create a new figure.
# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# fig, axs = plt.subplots(2, 2)  # Create a figure with a 2x2 grid of axes.
# fig, axs = plt.subplot_mosaic([['left', 'right_top'], ['left', 'right_bottom']])

# b = np.matrix([[1,2], [3,4]])
# b_asarray = np.asarray(b)

# np.random.seed(19680801)
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')

x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.plot(x, x, label='linear')  # Plot some data on the Axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x label')  # Add an x-label to the Axes.
# ax.set_ylabel('y label')  # Add a y-label to the Axes.
# ax.set_title("Simple Plot")  # Add a title to the Axes.
# ax.legend()  # Add a legend.



# def my_plotter(ax, data1, data2, param_dict):
#     """
#     A helper function to make a graph.
#     """
#     out = ax.plot(data1, data2, **param_dict)
#     return out

# data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
# my_plotter(ax1, data1, data2, {'marker': 'x'})
# my_plotter(ax2, data3, data4, {'marker': 'o'})

# fig, ax = plt.subplots(figsize=(5, 2.7))
# x = np.arange(len(data1))
# ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
# l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
# l.set_linestyle(':')

# fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
# xdata = np.arange(len(data1))  # make an ordinal for this
# data = 10**data1
# axs[0].plot(xdata, data)

# axs[1].set_yscale('log')
# axs[1].plot(xdata, data)

# fig, axs = plt.subplots(2, 1, layout='constrained')
# axs[0].plot(xdata, data1)
# axs[0].set_title('Automatic ticks')

# axs[1].plot(xdata, data1)
# axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
# axs[1].set_yticks([-1.5, 0, 1.5])  # note that we don't need to specify labels
# axs[1].set_title('Manual ticks')

from matplotlib.dates import ConciseDateFormatter

# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# dates = np.arange(np.datetime64('2021-11-15'), np.datetime64('2021-12-25'),
#                   np.timedelta64(1, 'h'))
# data = np.cumsum(np.random.randn(len(dates)))
# ax.plot(dates, data)
# ax.xaxis.set_major_formatter(ConciseDateFormatter(ax.xaxis.get_major_locator()))

# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']

# ax.bar(categories, np.random.rand(len(categories)))

# fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(7, 2.7), layout='constrained')
# l1, = ax1.plot(t, s)
# ax2 = ax1.twinx()
# l2, = ax2.plot(t, range(len(t)), 'C1')
# ax2.legend([l1, l2], ['Sine (left)', 'Straight (right)'])

# ax3.plot(t, s)
# ax3.set_xlabel('Angle [rad]')
# ax4 = ax3.secondary_xaxis('top', functions=(np.rad2deg, np.deg2rad))
# ax4.set_xlabel('Angle [°]')



plt.show()  # Display the figure.