import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing 
import seaborn as sb
import openpyxl
data=pd.read_csv("Titanic-Dataset.csv")
print(data)

print(data.shape)

print(data.isna().sum())

print(data.dtypes)


label_encoder=preprocessing.LabelEncoder()
data['Sex']=label_encoder.fit_transform(data['Sex'])
data['Sex'].value_counts
print(data['Sex'])

print(data)



Age=data['Age'].median()
print("Average age of passangers",Age)


data['Age']=data['Age'].fillna(value=28)
print(data['Age'])
print(data)



# eliminate_data=data.drop(['Ticket','Cabin','Name'],axis=1)
# print(eliminate_data)

embarked_values=data['Embarked'].value_counts()
print(embarked_values)



grouped = data.groupby(['Embarked', 'Survived'])
grouped_count = grouped.size().unstack()
print(grouped_count)


data['Embarked']=data['Embarked'].fillna(value='S')
print(data['Embarked'])





grouped = data.groupby(['Embarked', 'Survived'])
grouped_count = grouped.size().unstack()
print(grouped_count)


label_encoder=preprocessing.LabelEncoder()
data['Embarked']=label_encoder.fit_transform(data['Embarked'])
data['Embarked'].value_counts()
print(data['Embarked'])


eliminate_data=data.drop(['Ticket','Cabin','Name'],axis=1)
print(eliminate_data)


print(eliminate_data.isna().sum())


final_data=data.drop(['Pclass','SibSp','Parch','Fare','Embarked','Ticket','Cabin','Name'],axis=1)
print(final_data)


plot_data = data[['Embarked', 'Survived']]



# Specify the file path for the Excel file where you want to save the data
excel_file_path = r"C:\Users\Sai kumar\OneDrive\Documents\projects\titanic_Final_data.xlsx"

# Use the to_excel method to save the DataFrame to the specified Excel file
final_data.to_excel(excel_file_path, index=False, engine='openpyxl')  # Specify 'openpyxl' as a string

print("final_data has been saved to", excel_file_path)



# Plot the data using Seaborn countplot
sb.countplot(x='Embarked', hue='Survived', data=plot_data)

# Customize the plot
plt.xlabel('Embarked')
plt.ylabel('Count')
plt.title('Survival Count by Embarked')
plt.legend(title='Survived')

# Show the plot
plt.show()



