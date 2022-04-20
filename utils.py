import os
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from functools import reduce
import operator


class ExitCodeError(Exception):
    pass


def sh(x):
    if os.system(x):
        raise ExitCodeError()

def ls(x):
    return [x + "/" + fn for fn in os.listdir(x)]


def lsr(x):
    if os.path.isdir(x):
        return reduce(operator.add, map(lsr, ls(x)), [])
    else:
        return [x]


def fwrite(fname, content):
    with open(fname, "w") as fh:
        fh.write(content)


def fread(fname):
    with open(fname) as fh:
        return fh.read()


def chdir_up_n(n):
    """Goes up n times in the directory tree."""
    for i in range(n):
        os.chdir("..")


def radar_chart_plot(df):

    fig = px.line_polar(df, r="scores", theta="labels", line_close=True)

    return fig


def bar_chart_plot(prediction_result):
    plt.plot()

    height = list(prediction_result.values())
    bars = list(prediction_result.keys())
    y_pos = np.arange(len(bars))

    # Create bars
    plt.bar(y_pos, height)

    # Create names on the x-axis
    plt.xticks(y_pos, bars, rotation="vertical")
