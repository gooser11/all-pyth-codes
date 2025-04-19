#Values less than given:
"""
# import required libraries
from scipy.stats import norm
import numpy as np

# Given information
mean = int(input("Mean: ")) # 78
std_dev = int(input("std dev: "))# 25
total_students = int(input("total samples: ")) # 100
score = int(input("thing we want: "))#60

# Calculate z-score for given
z_score = (score - mean) / std_dev

# Calculate the probability of getting a score less than 60
prob = norm.cdf(z_score)

# Calculate the percentage of students who got less than 60 marks
percent = prob * 100

# Print the result
print("Percentage of samples who got less than given input:", round(percent, 2), "%")
"""


#Values greather than given:
"""
# import required libraries
from scipy.stats import norm
import numpy as np

# Given information
mean = int(input("Mean: ")) #78
std_dev = int(input("std dev: ")) #25
total_students = int(input("num samples: ")) # 100
score = int(input("Thing we want: ")) # 70

# Calculate z-score for 70
z_score = (score - mean) / std_dev

# Calculate the probability of getting a more than 70
prob = norm.cdf(z_score)

# Calculate the percentage of students who got more than 70 marks
percent = (1-prob) * 100

# Print the result
print("Percentage of samples who got more than given input: ", round(percent, 2), " %")
"""


#number between
"""
# import required libraries
from scipy.stats import norm
import numpy as np

# Given information
mean = int(input("Mean: ")) #78
std_dev = int(input("Std dev: ")) # 25
total_students = int(input("Num Samples: ")) # 100
min_score = int(input("Min: ")) # 75
max_score = int(input("Max: ")) # 85

# Calculate z-score for 75
z_min_score = (min_score - mean) / std_dev
# Calculate z-score for 85
z_max_score = (max_score - mean) / std_dev


# Calculate the probability of getting less than 70
min_prob = norm.cdf(z_min_score)

# Calculate the probability of getting  less than 85
max_prob = norm.cdf(z_max_score)

percent = (max_prob-min_prob) * 100

# Print the result
print("Percentage of samples that are between min and max is", round(percent, 2), "%")
"""


#Calculate for single point normal dist:
"""
import numpy as np

def normal_dist(x, mean, sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density

mean = 0
sd = 1
x = 1
result = normal_dist(x, mean, sd)
print(result)
"""

# Plotting:
"""
import numpy as np
import matplotlib.pyplot as plt
 
# Mean of the distribution 
Mean = 100

# satndard deviation of the distribution
Standard_deviation  = 5
 
# size
size = 100000
 
# creating a normal distribution data
values = np.random.normal(Mean, Standard_deviation, size)
 
# plotting histograph
plt.hist(values, 100)
# plotting mean line
plt.axvline(values.mean(), color='k', linestyle='dashed', linewidth=2)
plt.show()
"""

