
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_data(df, plot_type):
    sns.set(style="whitegrid")
    
    plot_functions = {
        'Years Using Brand': lambda: sns.histplot(df['Years Using Brand'], bins=15, kde=True),
        'Role in Cosmetics Industry': lambda: sns.countplot(x='Role in Cosmetics Industry', data=df),
        'Cosmetic Brand Used Most Frequently': lambda: sns.countplot(x='Cosmetic Brand Used Most Frequently', data=df),
        'Learned About Brand': lambda: sns.countplot(x='Learned About Brand', data=df),
        'Personal Use at Home': lambda: sns.countplot(x='Personal Use at Home', data=df),
        'Issues Encountered': lambda: sns.histplot(df['Issues Encountered'], bins=5, kde=True),
        'Loyalty': lambda: sns.histplot(df['Loyalty'], bins=10, kde=True),
        'Use Online Store': lambda: sns.countplot(x='Use Online Store', data=df),
        'Average Quarterly Spend': lambda: sns.histplot(df['Average Quarterly Spend'], bins=20, kde=True)
    }

    if plot_type == "all":
        fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(18, 18))
        fig.subplots_adjust(hspace=0.5, wspace=0.5)
        for i, (title, func) in enumerate(plot_functions.items()):
            plt.subplot(3, 3, i+1)
            func()
            plt.title(title)
        plt.tight_layout()
        plt.show()
    elif plot_type in plot_functions:
        plt.figure(figsize=(5, 7))
        plot_functions[plot_type]()
        plt.title(plot_type)
        
        plt.xticks(rotation=90, fontsize=8)
        plt.yticks(rotation=0, fontsize=8)

        plt.tight_layout()
        plt.subplots_adjust(bottom=0.3, top=0.95)

        plt.show()
    else:
        print("Plot type not recognized. Available types are:", list(plot_functions.keys()) + ['all'])

