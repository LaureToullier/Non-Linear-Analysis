import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider


def animate(x, y, duration=10, interval=5, ax=None):

    x = np.array(x)
    y = np.array(y)

    fig, (ax, slider_ax) = plt.subplots(nrows=2, gridspec_kw=dict(height_ratios=(5, 1)))

    title = ax.set_title("Iteration 0 (0%)")
    line, = ax.plot(x, y)
    point, = ax.plot(x[:1], y[:1], "o")
    slider = Slider(
        slider_ax,
        "index",
        0, x.size,
        valinit=0,
        valstep=1,
    )

    def update(val):
        point.set_data(x[val:val+1],y[val:val+1])
        fig.canvas.draw_idle()
    
    slider.on_changed(update)

    plt.show()


if __name__=="__main__":
    import pandas as pd
    df = pd.read_csv("C1.csv")
    animate(df["Rotation"], df["Base moment [kN.m]"], duration=5)