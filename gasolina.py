import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('gasolina.csv')
df.head()
sns.lineplot(data=df, x='dia', y='venda',color='red')
plt.title('novo preço da gasolina')
plt.legend(['gasolina'])
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.savefig('gasolina.png')
 