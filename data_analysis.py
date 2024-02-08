import pandas as pd
import matplotlib.pyplot as plt

#Loads the dataset
netflix_data = pd.read_csv('Netflix_data.csv')

#Removes rows with no date
netflix_data = netflix_data.dropna(subset=['Date'])

#Displays basic statistics of the netflix data
print(netflix_data.describe())
plt.figure(figsize=(12, 6))
plt.plot(netflix_data['Date'], netflix_data['Close'], color='red')
plt.title('Netflix Stock Price (2023-24)')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.grid(True)
plt.show()

netflix_high_sorted = netflix_data.sort_values(by='High', ascending=False)

#Displays the top ten high dates in the data set to get a better idea of the 
#best days for netflix and look for patterns
print(netflix_high_sorted.head(10))

netflix_low_sorted = netflix_data.sort_values(by='Low', ascending=True)

#Displays the bottom ten dates in the data set to get a better idea of the best 
#days for netflix and look for patterns
print(netflix_low_sorted.head(10))