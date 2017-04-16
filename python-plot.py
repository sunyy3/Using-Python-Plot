# In the begining, import several useful modules in python
import matplotlib.pyplot as plt
import numpy as np

# Example 1: simple scatter plot
# For start, let's plot a simple line, and customize your figure and axis.
x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [0, 1, 4, 9,16,25,36,49]
z = [0, 1, 2, 3, 4, 5, 6, 7]
# have a empty canvas
plt.clf()

# scatter and line format: circle point, solid line, red. You can define together or explicitly.
plt.plot(x,y,'ro-',label='quadratic')    
plt.plot(x,z,label='linear',color='purple',marker='o',linestyle='-',linewidth=2.0)
plt.legend(loc='upper left')
################################################################################################################################################
# other option of marker, line
# marker: point '.' ',', circle 'o', triangle 'v' '<' '>' '^', square 's', diamond 'D' 'd', x 'x' 'X', star '*', hexagon 'h' 'H', pentagon 'p'
# linestyle or ls: 'solid' '-', 'dashed' '--', 'dashdot' '-.', 'dotted' ':'
# color: 'red', 'green', 'black', 'blue', 'yellow', 'purple' 
################################################################################################################################################

# The text format in the figure, including size, font, style
plt.title('simple plot',style='italic',fontsize=12,fontweight='bold')
# adding text into figure, the two number give the coordinate of text
plt.text(2,15,'This is a comment!',style='oblique')
plt.annotate('annotate',xy=(1,1),xytext=(1,8),arrowprops=dict(color='black',shrink=0.05))
#################################################################
## more information: http://matplotlib.org/users/text_props.html     
#################################################################

# customize the axis
plt.xlim(0,8)
plt.ylim(0,50)
plt.xlabel('x')
plt.ylabel('y')
plt.tick_params(direction='in')    # make tick face inside

plt.grid(True)                     # show grid
plt.savefig('simplePlot.png')      # save figure you just plot
plt.show()                         # interactive show your figure


# Example 2: how to write Greek letter and math equation in the figure using LaTex
plt.clf()
# In python, LaTex form text is started with '$' and also ended with '$'
# Greek letter in small and Capital form
plt.title('$\\theta \\Theta; \sigma \Sigma; \pi \Pi$')   
# some basic mathematical operator
plt.xlabel('$\\times \div \\neq \leq \geq \equiv $')    
# some calculus symbol: the last one is Angstrom
plt.ylabel('$\infty \partial \int \oint \sum \prod \AA$')    
# subscript using '_' and superscript using '^', if subscript is a long equation, using {} to surround equation, e.g. {i=1}
plt.text(0.5 ,0.5, '$(a_1+a_2)^2 = a_1^2 + 2 a_1 a_2 + a_2^2 $', style='italic')    
# fraction using '\frac{numerator}{denimunator}', similarly, long equation using {}, e.g. {n^2}
plt.text(0.5 ,0.3, '$ \sum_{i=1}^{n} \\frac{1}{n} = p $')    
plt.show()
##################################################################################
## more information about LaTex can be found at: https://www.sharelatex.com/learn
##################################################################################


# Example 3: how to plot histogram from raw data
import random
Alist = []
for i in range(300):
   Alist.append(random.randint(1,100))

# First, plot histogram using count number in every bin range
bins = np.arange(0,105,5)    # define 20 bins from 0 to 100, every 5 as one bin, Note: right boundary doesn't include
plt.clf()
plt.hist(Alist,bins=bins,alpha=0.5,color='red',edgecolor='black')
# option: 'alpha' define transparency, 'color' define fill color, 'edgecolor' define outline color
plt.ylabel('count')
plt.show()

# Second, we can also plot normalized histgram using probability of every bin
# Note: the option: "normed=True" won't give us correct figure, here we need using "weights"
# Basically, here "weights" does: instead of counting every data point in "Alist" as 1, it count as 1/len(Alist), then we easily get the probability
weight_Alist = np.ones_like(Alist)/len(Alist)
bins = np.arange(0,105,5)
plt.clf()
plt.hist(Alist,bins=bins,alpha=0.5,color='red',edgecolor='black',weights=weight_Alist)
plt.ylabel('Probability')
plt.show()

# Third, if you want to know exactly value of each bins, we can using "numpy"
bins = np.arange(0,105,5)
histRes, bin_width = np.histogram(Alist,bins)
# NOTE: the length of bin_width is larger than the length of histRes by 1.
print(histRes,len(histRes))
print(bin_width,len(bin_width))


# Example 4: how to do linear regression
from scipy import stats
x = [  1,  2,  3,  5,  6,  8]
y = [1.3,2.3,3.5,5.7,6.3,8.7]
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print(slope, intercept, r_value, std_err)
y_fit = [item*slope+intercept for item in x]
plt.clf()
plt.plot(x,y,'ro')
plt.plot(x,y_fit,'b-')
plt.text(2,7,' y = {0:6.4f} x + {1:6.4f} \n $R^2$ = {2:6.4f}'.format(slope, intercept, r_value*r_value))
plt.show()


# Example 5: how to draw figures with two y-axis, which share one x-axis
month = [i for i in range(1,13)]
price = [12, 8, 9, 4, 1, 3, 7, 7, 8, 13, 14, 15]
amount = [3, 5, 7, 10, 20, 15, 9, 9, 8, 4, 2, 1]

# here we have two y-axis system: ax1 and ax2
fig, ax1 =plt.subplots()
ax2 = ax1.twinx()
ax1.plot(month,price,'ro-')
ax2.plot(month,amount,'b>-')
ax1.set_xlabel('Month')
ax1.set_ylabel('Price')
ax2.set_ylabel('Amount')
fig.tight_layout()
plt.show()
