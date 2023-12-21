import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


def animate(x, y, duration=10, interval=5, ax=None):

    x = np.array(x)
    y = np.array(y)

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.get_figure()

    title = ax.set_title("Iteration 0 (0%)")
    line, = plt.plot(x[:1], y[:1])
    ax.dataLim.x0 = x.min()
    ax.dataLim.x1 = x.max()
    ax.dataLim.y0 = y.min()
    ax.dataLim.y1 = y.max()

    step = int((x.size*interval/1000) // duration)
    print(f"{step = }")
    step = max(1, step)
    step = min(x.size, step)
    n = x.size // step

    def plot_until(i):
        it = i*step
        title.set_text(f"Iteration {it} ({it/x.size:.1%})")
        line.set_data(x[:it+1], y[:it+1])

    anim_running = True

    def onClick(event):
        nonlocal anim_running
        if anim_running:
            anim.event_source.stop()
            anim_running = False
        else:
            anim.event_source.start()
            anim_running = True

    fig.canvas.mpl_connect('button_press_event', onClick)
    anim = FuncAnimation(fig, plot_until, frames=n, interval=5)

    plt.show()


if __name__=="__main__":
    import pandas as pd
    df = pd.read_csv("C1.csv")
    fig, ax = plt.subplots()
    ax.set_xlabel("Rotation")
    ax.set_ylabel("Base moment [kN.m]")
    animate(df["Rotation"], df["Base moment [kN.m]"], ax=ax, duration=5)