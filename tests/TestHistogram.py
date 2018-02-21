import numpy as np
import scr.FigureSupport as cls


obs = np.random.normal(4, 3, 1000)
cls.graph_histogram(
    observations=obs,
    title='Histogram',
    x_label='Values',
    y_label='Counts',
    legend='Number of patients')
