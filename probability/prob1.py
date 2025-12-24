#Normal Distribution 
import scipy.stats as stats 
import seaborn as sns 
import matplotlib.pyplot as plt 

data= stats.norm(scale=10, loc=0).rvs(1000)
sns.histplot(data, kde=True)
plt.title("Normal Distribution with mean=0 and std=10")
plt.show()
