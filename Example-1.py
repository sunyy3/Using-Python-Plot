# Example 1: simple scatter plot

# In the begining, import several useful modules in python
import matplotlib.pyplot as plt
import numpy as np

# For start, let's plot a simple line, and customize your figure and axis.
x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [0, 1, 4, 9, 16, 25, 36, 49]
z = [0, 1, 2, 3, 4, 5, 6, 7]

# have a empty canvas and customize the position of axes
plt.clf()
plt.figure().add_axes([0.15, 0.15, 0.8, 0.8])
###############################################################################
# 1. Scatter and line format: circle point, solid line, red.
#   You can define together or explicitly.
plt.plot(x, y, 'ro-', label='quadratic')
plt.plot(x, z, label='linear', color='purple', mec='b', marker='o',
    linestyle='-', linewidth=2.0)
# Other option of marker, line: here "" quotes the option we used above.
# (1) "marker": point '.' ',', circle 'o', triangle 'v' '<' '>' '^', 
# square 's', diamond 'D' 'd', x 'x' 'X', star '*', hexagon 'h' 'H',
# pentagon 'p'.
# (2) Other marker setting up: "markerdegecolor" or "mec", "markeredgewidth"
# or 'mew', "markerfacecolor" or 'mfc', "markersize" or "ms".
# (3) "linestyle" or "ls": 'solid' '-', 'dashed' '--', 'dashdot' '-.',
# 'dotted' ':'.
# (4) "linewidth" or "lw": any float number.
# (5) "color" or "c": r 'red', g 'green', k 'black', b 'blue', y 'yellow',
# c 'cyan', m 'magenta', w 'white', 'purple'.
# (6) "alpha": float number (0.0 transparent through 1.0 opaque).
###############################################################################

###############################################################################
# 2. Set up the legend for different groups of data.
# Above code, the option 'label' give us the content of legend.
# Here we can set up some other option for this legend.
plt.legend(loc='upper left', prop={'size': 12})
# Options can be useful:
# (1) "loc": the position of legend, with combination of ['left', 'center',
# 'right'] and ['upper', 'center', 'lower'].
# (2) "borderpad": integer, the blank in the border of the legend box.
# (3) "labelspacing": integer, similar to line space.
# (4) "prop": define the size of the text.
# (5) "frameon": True or False, remove the box of the legend
###############################################################################

###############################################################################
# 3. The text format in the figure, including size, font, style
plt.title('simple plot', style='italic', fontsize=12, fontweight='bold')
# adding text into figure, the two number give the coordinate of text
plt.text(2, 15, 'This is a comment!', style='oblique')
plt.annotate('annotate', xy=(1,1), xytext=(1,8), arrowprops=dict(color='black',
    shrink=0.05))
# Option could be useful:
# (1) "size" or "fontsize": integer, or 'smaller', 'x-large'.
# (2) "style" or "fontstyle": 'normal', 'italic' 'oblique'.
# (3) "weight" or "fontweight": 'normal', 'bold', 'heavy', 'light',
# 'ultrabold', 'ultralight'.
# more information: http://matplotlib.org/users/text_props.html     
#################################################################


###############################################################################
# 4. customize the axis
plt.xlim(0,8)
plt.ylim(0,50)
plt.xticks(np.arange(0, 8.1, 1))  # Setting up the position of ticks 
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.tick_params(axis='both', top='off', right='off', direction='in',
    labelsize=12)
# tick_params has some useful options:
# (1) "axis": 'x', 'y', 'both', which axis these parameters are applied.
# (2) "which": 'major', 'minor', 'both'.
# (3) "direction": 'in', 'out', 'inout'.
# (4) "right": 'on' 'off', show ticks of right axis.
###############################################################################

###############################################################################
# 5. Grid and vertical or horizontal line
plt.grid(True)                     # show grid in x and y
plt.gca().yaxis.grid(True)         # only show grid of y axis.
plt.gca().xaxis.grid(False)
plt.axvline(x=4, linestyle='--', color='black')  # vertical line
plt.axhline(y=20, color='blue', alpha=0.5)       # horizontal line
###############################################################################

plt.savefig('simplePlot.png')      # save figure you just plot
plt.show()                         # interactive show your figure
