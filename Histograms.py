import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV data
df = pd.read_csv('fantasy500.csv')

# Filter top 90 players by position
top_90_qbs = df[df['POS'] == 'QB'].sort_values(by='FPPG', ascending=False).head(90)
top_90_rbs = df[df['POS'] == 'RB'].sort_values(by='FPPG', ascending=False).head(90)
top_90_wrs = df[df['POS'] == 'WR'].sort_values(by='FPPG', ascending=False).head(90)
top_90_tes = df[df['POS'] == 'TE'].sort_values(by='FPPG', ascending=False).head(90)

# Create a function to plot histograms with mean and std
def plot_histogram_for_position(ax, position_data, position_name):
    mean_fppg = position_data.mean()
    std_fppg = position_data.std()

    sns.histplot(position_data, kde=True, bins=30, color='skyblue', stat='density', ax=ax)

    ax.axvline(mean_fppg, color='red', linestyle='--', label=f'Mean: {mean_fppg:.2f}')
    ax.axvline(mean_fppg + std_fppg, color='green', linestyle='--', label=f'+1 STD: {mean_fppg + std_fppg:.2f}')
    ax.axvline(mean_fppg - std_fppg, color='green', linestyle='--', label=f'-1 STD: {mean_fppg - std_fppg:.2f}')

    ax.set_title(f'Distribution of Fantasy Points per Game (FPPG) - {position_name}')
    ax.set_xlabel('Fantasy Points per Game (FPPG)')
    ax.set_ylabel('Density')
    ax.legend()

# Create a grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))  # 2x2 grid of subplots

# Plot histograms on each subplot
plot_histogram_for_position(axes[0, 0], top_90_qbs['FPPG'], 'Quarterbacks (QB)')
plot_histogram_for_position(axes[0, 1], top_90_rbs['FPPG'], 'Running Backs (RB)')
plot_histogram_for_position(axes[1, 0], top_90_wrs['FPPG'], 'Wide Receivers (WR)')
plot_histogram_for_position(axes[1, 1], top_90_tes['FPPG'], 'Tight Ends (TE)')

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
