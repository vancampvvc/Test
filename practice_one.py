# Define the variables
a = [1,2,3,4,5,6,7,8,9,10]
b = [11,12,13,14,15,16,17,18,19,20]
c = ['apple', 'organge', 'grape', 'grapefruit', 'passionfruit', 'pumpkin', 'banana', 'pea', 'carrot', 'beef']

# Create the table
table = list(zip(a, b, c))
print (table)

# Run statistical analysis
average = sum(a) / len(a)
print (average)

# Create a bar chart for variables a and c
from matplotlib import colors
import matplotlib.pyplot as plt
plt.bar (c,a, color = 'lightgreen', size = '8')
plt.gca() .set_facecolor('grey')
plt.xlabel('Food Type')
plt.ylabel('Amount')
plt.title('Bar Chart of Food Type and Amount')
plt.show()
