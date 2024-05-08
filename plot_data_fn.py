
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_data(df, plot_type):
    sns.set(style="whitegrid")
    
    # Define which plots should have rotated x-axis labels
    rotate_x_labels = {'Role in Cosmetics Industry', 'Learned About Brand', 'Use Online Store'}

    plot_functions = {
        'Years Using Brand': lambda ax: sns.histplot(df['Years Using Brand'], bins=15, kde=True, ax=ax),
        'Role in Cosmetics Industry': lambda ax: sns.countplot(x='Role in Cosmetics Industry', data=df, ax=ax),
        'Cosmetic Brand Used Most Frequently': lambda ax: sns.countplot(x='Cosmetic Brand Used Most Frequently', data=df, ax=ax),
        'Learned About Brand': lambda ax: sns.countplot(x='Learned About Brand', data=df, ax=ax),
        'Personal Use at Home': lambda ax: sns.countplot(x='Personal Use at Home', data=df, ax=ax),
        'Issues Encountered': lambda ax: sns.histplot(df['Issues Encountered'], bins=5, kde=True, ax=ax),
        'Loyalty': lambda ax: sns.histplot(df['Loyalty'], bins=10, kde=True, ax=ax),
        'Use Online Store': lambda ax: sns.countplot(x='Use Online Store', data=df, ax=ax),
        'Average Quarterly Spend': lambda ax: sns.histplot(df['Average Quarterly Spend'], bins=20, kde=True, ax=ax)
    }

    if plot_type in plot_functions:
        fig, ax = plt.subplots(figsize=(5, 7))  # Create a figure and an axes.
        plot_functions[plot_type](ax)  # Execute the plotting function with the axes
        plt.title(plot_type)
        ax.set_xlabel('')
        # Apply conditional rotation
        if plot_type in rotate_x_labels:
            plt.xticks(rotation=90, fontsize=8)
        else:
            plt.xticks(rotation=0, fontsize=8)
        
        plt.yticks(rotation=0, fontsize=8)
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.3, top=0.95)
        plt.show()
    else:
        print("Plot type not recognized. Available types are:", list(plot_functions.keys()) + ['all'])


