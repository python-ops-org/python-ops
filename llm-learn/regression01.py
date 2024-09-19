import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model

# Load the dataset
df = pd.read_csv('homes.csv')

# Plot the data
plt.xlabel('Area in sqft')
plt.ylabel('Price in USD')
plt.scatter(df.area, df.price, color='red', marker='+')

# Display the plot
plt.show()
