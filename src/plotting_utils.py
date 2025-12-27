import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle

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

def add_strike_zone(ax, facecolor='lightgray', edgecolor='black', linewidth=1.5, alpha=1.0):
    """Add MLB strike zone rectangle to an existing plot."""
    strike_zone = Rectangle(
        (-0.947, 1.5),
        width=0.947 * 2,
        height=3.6 - 1.5,
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        alpha=alpha
    )
    ax.add_patch(strike_zone)
    return strike_zone
