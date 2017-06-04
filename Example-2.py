# Example 2: how to write Greek letter and math equation in the figure
# using LaTex

import matplotlib.pyplot as plt

plt.clf()

# In python, LaTex form text is started with '$' and also ended with '$'

# 1. Greek letter in small and Capital form
plt.title('$\\theta \\Theta; \sigma \Sigma; \pi \Pi$')

# 2. some basic mathematical operator
plt.xlabel('$\\times \div \\neq \leq \geq \equiv $')

# 3. some calculus symbol
plt.ylabel('$\infty \partial \int \oint \sum \prod$')

# 4. The Angstrom
plt.text(0.8, 0.8, '$\AA$')

# 5. subscript using '_' and superscript using '^', if subscript is a
# long equation, using {} to surround equation, e.g. {i=1}
plt.text(0.5 ,0.5, '$(a_1+a_2)^2 = a_1^2 + 2 a_1 a_2 + a_2^2 $', 
    style='italic')    

# 6. fraction using '\frac{numerator}{denimunator}', similarly, long equation 
# using {}, e.g. {n^2}
plt.text(0.5 ,0.3, '$ \sum_{i=1}^{n} \\frac{1}{n} = p $')    
plt.show()

###############################################################################
# more information about LaTex can be found at:
# https://www.sharelatex.com/learn
###############################################################################