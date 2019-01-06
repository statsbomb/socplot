import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, ConnectionPatch, Rectangle


class Pitch:

    # default dims to match ArqamFc data
    __width = 120
    __hight = 80
    __fig_size = (12, 8)

    def __init__(self):
        fig, ax = plt.subplots(figsize=self.__fig_size)
        ax.axis('off')  # this hides the x and y ticks
        plt.ylim(-2, 82)
        plt.xlim(-2, 122)
        pitch_components = self.__build_pitch(ax)
        for c in pitch_components:
            ax.add_artist(c)

        self._plt = plt
        self._ax = ax

    def show(self):
        self._plt.show()

    def draw_player(self, x, y, number=False, color=''):
        if not color:
            color = 'red'
        p = Circle((x, y), 1.5, color=color)
        self._ax.add_artist(p)
        if number:
            self._ax.annotate(number, xy=(x-0.9, y-0.3), fontsize=7) # align the text with the circle
    
    def draw_pass(self, start, end, pass_type='low',color=''):
        if not color:
            color = ''
        
        if pass_type == 'low':
            line = '-'
        elif pass_type == 'ground':
            line = '-^'
        elif pass_type == 'high':
            line = '-*'
        if self.__valid_position(start) or self.__valid_position(end):
            raise TypeError('Location should be in range (0~120)(0~80)')
        self._plt.plot(
            [start[0], end[0]],
            [start[1], end[1]], line, color=color)
        self._plt.plot(start[0], start[1], "o", color='green')

    def __valid_position(self, loc):
        return loc[0] < 0 or loc[1] < 0 or loc[0] > self.__width or loc[1] > self.__hight
    def __build_pitch(self, ax):

            return [
                Rectangle((0, 0), width=self.__width, height=self.__hight,
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
