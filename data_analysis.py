import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a pandas DataFrame
netflix_data = pd.read_csv('Netflix_data.csv')

# Remove rows with missing dates
netflix_data = netflix_data.dropna(subset=['Date'])

# Display basic statistics of the dataset
print(netflix_data.describe())
plt.figure(figsize=(12, 6))
plt.plot(netflix_data['Date'], netflix_data['Close'], color='red')
plt.title('Netflix Stock Price (2023-24)')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.grid(True)
plt.show()

