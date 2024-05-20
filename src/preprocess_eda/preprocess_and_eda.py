import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('dataset_HTN.csv')

# Preprocessing
def preprocess_data(df):
    # Checking for missing values
    print("Missing values:\n", df.isnull().sum())
    
    # Dropping duplicates
    df = df.drop_duplicates()
    
    return df

# Exploratory Data Analysis (EDA)
def perform_eda(df):
    # Summary statistics
    print("Summary statistics:\n", df.describe())
    
    # Count of drugs per target
    drug_target_count = df['target_name'].value_counts()
    print("\nCount of drugs per target:\n", drug_target_count)
    
    # Count of drugs per disease
    drug_disease_count = df['disease_name'].value_counts()
    print("\nCount of drugs per disease:\n", drug_disease_count)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    sns.countplot(y='target_name', data=df, order=drug_target_count.index)
    plt.title('Number of Drugs per Target')
    plt.xlabel('Number of Drugs')
    plt.ylabel('Target Name')
    plt.show()
    
    plt.figure(figsize=(10, 6))
    sns.countplot(y='disease_name', data=df, order=drug_disease_count.index)
    plt.title('Number of Drugs per Disease')
    plt.xlabel('Number of Drugs')
    plt.ylabel('Disease Name')
    plt.show()

if __name__ == "__main__":
    # Preprocess data
    df = preprocess_data(df)
    
    # Save the cleaned data
    df.to_csv('dataset_HTN_cleaned.csv', index=False)
    
    # Perform EDA
    perform_eda(df)
