import scipy.stats as st
import math
# the math package is necessary because the expression for t uses the math.sqrt(x) function.

n = int(input("sample size: "))# enter sample size
pop_mean = float(input("population mean: "))# enter population mean
sam_mean = float(input("sample mean: "))# enter sample mean
sd = float(input("std dev: "))# enter standard deviation
df = n-1# enter degrees of freedom

 # write an expression to find the value of t.
t = (sam_mean - pop_mean) / (sd / (math.sqrt(n)))

# use the st.t.sf function to find the probability
prob = st.t.sf(t, df)

print(f'The probability that another 50 household sample will have a sample mean of at least 2.1 is {prob:.6f}.')

#two-tailed:
"""
import scipy.stats as st
import math

# the math package is necessary because the expression for t uses the math.sqrt(x) function.

n = int(input("Sample size: "))  # enter sample size
pop_mean = float(input("Population mean: "))  # enter population mean
sam_mean = float(input("Sample mean: "))  # enter sample mean
sd = float(input("Standard deviation: "))  # enter standard deviation

df = n - 1  # degrees of freedom

# Calculate the t value
t = (sam_mean - pop_mean) / (sd / math.sqrt(n))

# Two-tailed probability
prob = st.t.sf(abs(t), df) * 2

print(f'The two-tailed probability that a sample of size {n} has a mean as extreme as {sam_mean} is {prob:.6f}.')
"""