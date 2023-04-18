import numpy as np
import matplotlib.pyplot as plt
n = 10000 # Define the number of dice rolls
rolls = np.random.randint(1, 6, size=n) # Roll the dice n times and calculate the mean of the outcomes
avg = [ ]
for i in range(1, n+1):
    avg.append(np.mean(rolls[:i]))
plt.hist(avg, bins=100)
plt.title("Distribution of the average for the rolls")
plt.xlabel("Average of Outcomes")
plt.ylabel("Frequency")
plt.show() # Plot the distribution of the average
