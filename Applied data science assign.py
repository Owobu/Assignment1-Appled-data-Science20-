# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt

# Load diabetes dataset from CSV file
diabetes_df = pd.read_csv('diabetes.csv')
print(diabetes_df)

# A function line plot of BMI and Glucose
def plot_line_chart():
    plt.plot(diabetes_df['BMI'], diabetes_df['Glucose'])
    plt.xlabel('BMI')
    plt.ylabel('Disease progression')
    plt.title('Diabetes Dataset - Line Chart')
    plt.legend(['Disease progression'])
    plt.show()
    
#This for loop function create multiple bar chart of age groups and number of patients
def plot_multiple_bar_chart():
    age_groups = ['0-25', '25-50', '50-75', '75-100']
    num_patients = [sum(1 for i in diabetes_df['BMI'] if i <= 25), 
                    sum(1 for i in diabetes_df['BMI'] if 25 < i <= 50), 
                    sum(1 for i in diabetes_df['BMI'] if 50 < i <= 75), 
                    sum(1 for i in diabetes_df['BMI'] if 75 < i <= 100)]
    plt.bar(age_groups, num_patients)
    plt.xlabel('BMI Age Groups')
    plt.ylabel('Number of Patients')
    plt.title('Diabetes Dataset - Multiple Bar Chart')
    plt.legend(['Number of Patients'])
    plt.show()
    
#A function that plot histogram of BMI in diabetes_df
def plot_histogram():
    plt.hist(diabetes_df['BMI'], bins=10)
    plt.xlabel('BMI')
    plt.ylabel('Frequency')
    plt.title('Diabetes Dataset - Histogram')
    plt.legend(['Frequency'])
    plt.show()

plot_line_chart()
plot_multiple_bar_chart()
plot_histogram()