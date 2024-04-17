"""
File: tempo.py
Author: Jeff Martin
Date: 6/6/2021

Copyright © 2022 by Jeffrey Martin. All rights reserved.
Email: jmartin@jeffreymartincomposer.com
Website: https://jeffreymartincomposer.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd


def make_metric_modulation_chain(initial_tempo, ratios: list):
    """
    Calculates a succession of tempos based on the provided metric modulation ratios
    :param initial_tempo: The initial tempo
    :param ratios: A list of ratios
    :return: A list of tempos
    """
    tempos = [Fraction(initial_tempo)]
    for i in range(len(ratios)):
        tempos.append(tempos[i] * ratios[i])
    return tempos


def plot_tempo_table(quarter_note_tempos: list, durations: list=None):
    """
    Makes a table of tempos based on a list of quarter-note tempos
    :param quarter_note_tempos: A list of quarter-note tempos
    :param durations: An optional list of durations if you want to override the provided one
    :return: None
    """
    # A list of fractional durations (whole note, half note, half triplet, etc.)
    DURATIONS = [Fraction(4, 1), Fraction(2, 1), Fraction(4, 3), Fraction(1, 1), Fraction(4, 5), Fraction(2, 3),
                 Fraction(4, 7), Fraction(1, 2), Fraction(2, 5), Fraction(1, 3), Fraction(2, 7), Fraction(1, 4),
                 Fraction(1, 5), Fraction(1, 6), Fraction(1, 7), Fraction(1, 8)]
    if durations is None:
        durations = DURATIONS

    # Set up colors for duplicate color flagging in the table
    colors = mcolors.CSS4_COLORS
    colors_del = []
    for color in colors:
        if "white" in color or "grey" in color or "gray" in color or "black" in color or "dark" in color:
            colors_del.append(color)
    for color in colors_del:
        del colors[color]

    # Set up table headers
    columns = []
    for f in durations:
        if f.denominator == 1:
            columns.append(f"{f.numerator}")
        else:
            columns.append(f"{f.numerator}/{f.denominator}")

    # Convert the tempo list to Fractions
    tempos = [Fraction(t) for t in quarter_note_tempos]

    # Build the tempo table
    duplicate_tempi = {}
    tempo_table = np.zeros((len(tempos), len(durations)))
    for i in range(len(tempos)):
        for j in range(len(durations)):
            current_tempo = tempos[i] / durations[j]
            tempo_table[i][j] = current_tempo
            if current_tempo not in duplicate_tempi:
                duplicate_tempi[current_tempo] = [1, ""]
            else:
                duplicate_tempi[current_tempo][0] += 1
    for key in duplicate_tempi:
        if duplicate_tempi[key][0] > 1:
            color = colors.popitem()
            duplicate_tempi[key][1] = color[1]

    # Display the table
    df = pd.DataFrame(tempo_table, columns=columns)
    colors = mcolors.CSS4_COLORS
    plt.rcParams["font.family"] = "Segoe UI"
    fig, ax = plt.subplots()
    # fig.set_size_inches(10, 5)
    fig.canvas.setWindowTitle("Tempo Table")
    fig.patch.set_visible(False)
    ax.axis("off")
    # ax.axis("tight")
    t = ax.table(cellText=df.values.round(2), colLabels=columns, colColours=["#DDDDDD" for i in range(len(durations))], loc="center")
    t.auto_set_font_size(False)
    t.set_fontsize(11)
    p = t.properties()
    # print(p)
    for c in p["celld"]:
        print(c)
        if (c[0] < len(tempos)):
            if tempo_table[c[0], c[1]] in duplicate_tempi:
                if duplicate_tempi[tempo_table[c[0], c[1]]][0] > 1:
                    p["celld"][(c[0] + 1, c[1])].set(color=duplicate_tempi[tempo_table[c[0], c[1]]][1])
    fig.tight_layout()
    plt.show()

    