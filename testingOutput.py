# scores = {'1000hz':10,'2000hz':15,'3000hz':10,'4000hz':15,'5000hz':10,'6000hz':15,'7000hz':10,'8000hz':15,'9000hz':10,'10000hz':15,'500hz':10,'250hz':15,}
# for score in scores:
#     log.write(score[:-2],str(scores[score]))
    
# Import the necessary modules
scores = {'1000hz':5,'2000hz':10}
import csv


# Create a list of the keys and values in the dictionary
keys = list(scores.keys())
values = list(scores.values())

# Open the CSV file for writing
with open('C:\\gitRepos\\Audiometric-Testing-Interface\\output-data.csv', 'w', newline='') as csvfile:

    # Create a writer object
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Frequency', 'Amplitude'])

    # Write the data rows
    for i in range(len(keys)):
        writer.writerow([keys[i][:-2], values[i]])

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('C:\\gitRepos\\Audiometric-Testing-Interface\\output-data.csv')
fig = plt.figure(figsize=(10,6))

# fig = plt.figure(figsize=(15, 20))
# Plot the data as a scatter plot
ax = plt.gca()
ax.scatter(df['Frequency'], df['Amplitude'])
ax.set_ylabel('Amplitude (dB)')
ax.set_xlabel('Frequency (Hz)')
ax.xaxis.set_label_coords(.5, 1.06)
ax.set_ylim(-25, 30)

ax.axhline(y=25, linestyle='--', color='gray')

# Add text to the right of the horizontal line
ax.text(x=775, y=25, s='Beginning of hearing loss', va='center', ha='left', fontsize=6)


# Set the x- and y-axis labels
# plt.xlabel('Frequency (Hz)')
# plt.xaxis.set_label_coords(.5, 1)
# x_label = plt.gca().xaxis.get_label()
# x_label.set_position((0.5, 1.08))
# x_label.set_y(1.05)
# plt.ylabel('Amplitude (dB HL)')

# Set the plot title
plt.title('Audiogram',y=1.1)
plt.tick_params(axis='x', which='both', top=True)
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
ax.invert_yaxis()
# Show the plot


# plt.figure(fig)
plt.show()

fig.savefig('C:\\gitRepos\\Audiometric-Testing-Interface\\audiogram.png')

