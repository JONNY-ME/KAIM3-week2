import matplotlib.pyplot as plt
import seaborn as sns

def plot_grouped_univariate_analysis(data, variables, group_size=3):
    """
    Function to plot grouped histograms and box plots for quantitative variables.

    Parameters:
        data (pd.DataFrame): The input DataFrame.
        variables (list): List of quantitative variables to analyze.
        group_size (int): Number of plots to display in a single figure.

    Returns:
        None: Displays grouped histograms and box plots.
    """
    num_vars = len(variables)
    num_groups = (num_vars + group_size - 1) // group_size  # Calculate number of groups
    
    for group_idx in range(num_groups):
        # Determine the variables for the current group
        start_idx = group_idx * group_size
        end_idx = min(start_idx + group_size, num_vars)
        group_vars = variables[start_idx:end_idx]

        # Create grouped histogram plots
        plt.figure(figsize=(16, 6))
        for idx, var in enumerate(group_vars, start=1):
            plt.subplot(1, group_size, idx)
            sns.histplot(data[var], kde=True, bins=30, color='blue', alpha=0.6)
            plt.title(f"Distribution of {var}", fontsize=12)
            plt.xlabel(var, fontsize=10)
            plt.ylabel("Frequency", fontsize=10)
            plt.tight_layout()
        plt.suptitle("Grouped Histograms", fontsize=14, y=1.02)
        plt.show()

        # Create grouped box plots
        plt.figure(figsize=(16, 6))
        for idx, var in enumerate(group_vars, start=1):
            plt.subplot(1, group_size, idx)
            sns.boxplot(x=data[var], color='skyblue')
            plt.title(f"Box Plot of {var}", fontsize=12)
            plt.xlabel(var, fontsize=10)
            plt.tight_layout()
        plt.suptitle("Grouped Box Plots", fontsize=14, y=1.02)
        plt.show()