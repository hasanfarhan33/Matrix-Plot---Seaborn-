import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

# print(tips.head())
# print("")
# print(flights.head())

tc = tips.corr()

# HEAT MAPS
# sns.heatmap(tc, annot=True, cmap='coolwarm')

fc = flights.pivot_table(index='month', columns='year', values='passengers')
# sns.heatmap(fc)

# CLUSTER MAP
sns.clustermap(fc, cmap='coolwarm', standard_scale=1)

plt.show()