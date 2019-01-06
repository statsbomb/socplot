import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Arc, Circle, ConnectionPatch, Rectangle


class Pitch:
    """
    Pitch object. Represents a dynamic pitch visualization.
    
    Methods
    -------
    plot_player
    plot_pass
    plot_heatmap
    show
    """

    # default dims to match ArqamFc data
    _width = 120
    _hight = 80
    _fig_size = (12, 8)

    def __init__(self):
        _, ax = plt.subplots(figsize=self._fig_size)
        ax.axis('off')  # this hides the x and y ticks
        plt.ylim(-2, 82)
        plt.xlim(-2, 122)
        pitch_components = self._build_pitch()
        for c in pitch_components:
            ax.add_artist(c)

        self._plt = plt
        self._ax = ax

    def show(self):
        """
        Same as plt.show()
        """
        self._plt.show()

    def plot_player(self, x, y, number=False, color=''):
        """
        Plot a player figure for the pitch figure 
        Parameters
        ----------
        x : x position of the player(float).
        y : y position of the player(float).
        number: player jersey number[optional].
        color: player color. Same as matplotlib color (named, hexa, rbg)
        Returns
        -------
        None
        """
        if not color:
            color = 'firebrick'
        p = Circle((x, y), 1.5, color='black', fc=color)
        self._ax.add_artist(p)
        if number:
            self._ax.annotate(number, xy=(x-0.9, y-0.3), fontsize=7) # align the text with the circle
    
    def plot_pass(self, start, end, pass_type='low',color=''):
        """
        Plot a new pass in the pitch
        Parameters
        ----------
        start : (X(float), Y(float)) represents start location of the path.
        end : (X(float), Y(float)) represents end location of the path.
        pass_type : str represents the pass type (high, low, ground)
        color: pass arrow color. Same as matplotlib color (named, hexa, rbg)
        Returns
        -------
        True if 
        """
        
        if not color:
            color = 'orange'
        if pass_type == 'low':
            line = 'D'
        elif pass_type == 'ground':
            line = 'o'
        elif pass_type == 'high':
            line = '*'
        else:
            raise TypeError('Invalid pass type')
        if self._invalid_position(start) or self._invalid_position(end):
            raise TypeError('Location should be in range (0~120)(0~80)')
        self._plt.plot(
            [start[0], end[0]],
            [start[1], end[1]], color=color)
        self._plt.plot(start[0], start[1], line, color='green')

    def _invalid_position(self, loc):
        """
        *this is an internal non-public method*
        check if specific location is valid
        Parameters
        ----------
        loc : (float, float) represents location 

        Returns
        -------
        True if 
        """
        return loc[0] < 0 or loc[1] < 0 or loc[0] > self._width or loc[1] > self._hight
    
    def _build_pitch(self, fig_type='complete'):
        """
        *this is an internal non-public method*
        build plt pitch figure 
        Parameters
        ----------
        fig_type : pitch type. Either compelete, right-half or left-half.

        Returns
        -------
        List of matplotlib patches which builds up the figure.
        """
        if fig_type == 'complete':
            return [
                Rectangle((0, 0), width=self._width, height=self._hight,
                            fill=False, color='grey'),  # pitch
                Rectangle([0, 22.3], width=14.6, height=35.3,
                            fill=False),  # left penalty area
                Rectangle([105.4, 22.3], width=14.6, height=35.3,
                            fill=False),  # right penalty area
                ConnectionPatch([60, 0], [60, 80], "data", "data"),
                Rectangle([0, 32], width=4.9, height=16, fill=False),
                Rectangle([115.1, 32], width=4.9, height=16, fill=False),
                plt.Circle((60, 40), 9.1, color="black", fill=False),
                plt.Circle((60, 40), 0.33, color="black"),
                plt.Circle((9.7, 40), 0.33, color="black"),
                plt.Circle((110.3, 40), 0.33, color="black"),
                Arc((9.7, 40), height=16.2, width=16.2, angle=0,
                    theta1=310, theta2=50, color="black"),
                Arc((110.3, 40), height=16.2, width=16.2, angle=0,
                    theta1=130, theta2=230, color="black")
            ]
        else:
            raise NotImplementedError

    def heat_map(self, x, y, color=''):
        """
        Add heatmap for the pitch figure 
        Parameters
        ----------
        x : array of x(float) positions in the pitch.
        y : array of y(float) positions in the pitch.

        Returns
        -------
        None
        """
        sns.kdeplot(x, y, shade=True, n_levels=50, color=color)
