import matplotlib.pyplot as plt
import seaborn as sns

def plot_regression(data, x, y, xlabel=None, ylabel=None, figsize=(8, 6), 
                   point_alpha=0.5, title=None):
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.regplot(data=data, x=x, y=y,
                scatter_kws={'color': 'black', 'alpha': point_alpha},
                line_kws={'color': 'blue'})
    ax.set_xlabel(xlabel or x)
    ax.set_ylabel(ylabel or y)
    if title:
        ax.set_title(title)
    plt.tight_layout()
    return fig, ax