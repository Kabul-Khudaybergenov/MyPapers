import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# GLOBAL CONFIGURATION
# Change all common parameters here
# ============================================================
CFG = {
    # Font / text
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "font.size": 17,
    "axes.labelsize": 22,
    "axes.labelweight": "bold",
    "xtick.labelsize": 18,
    "ytick.labelsize": 18,
    "legend.fontsize": 18,

    # Line / marker / axes
    "axes.linewidth": 1.4,
    "lines.linewidth": 2.0,
    "lines.markersize": 8,
    "tick.major.width": 1.4,
    "tick.minor.width": 1.0,
    "tick.major.size": 7,
    "tick.minor.size": 4,

    # DPI: global DPI for all figures and saved files
    "figure.dpi": 300,
    "savefig.dpi": 300,

    # Grid
    "grid.major.linestyle": "--",
    "grid.major.linewidth": 0.8,
    "grid.major.alpha": 0.65,
    "grid.minor.linestyle": ":",
    "grid.minor.linewidth": 0.6,
    "grid.minor.alpha": 0.45,

    # Figure sizes
    "figsize_line": (8.8, 6.4),
    "figsize_bar": (6.0, 5.6),

    # Save options
    "save_png": True,
    "save_pdf": False,   # change to True if needed
    "save_tiff": False,  # change to True if needed
    "bbox_inches": "tight",
}

plt.rcParams.update({
    "font.family": CFG["font.family"],
    "font.serif": CFG["font.serif"],
    "font.size": CFG["font.size"],
    "axes.labelsize": CFG["axes.labelsize"],
    "axes.labelweight": CFG["axes.labelweight"],
    "xtick.labelsize": CFG["xtick.labelsize"],
    "ytick.labelsize": CFG["ytick.labelsize"],
    "legend.fontsize": CFG["legend.fontsize"],
    "axes.linewidth": CFG["axes.linewidth"],
    "lines.linewidth": CFG["lines.linewidth"],
    "lines.markersize": CFG["lines.markersize"],
    "figure.dpi": CFG["figure.dpi"],
    "savefig.dpi": CFG["savefig.dpi"],
})

# ============================================================
# COMMON STYLE HELPERS
# ============================================================
series_style = {
    "Af": {"marker": "s"},
    "Be": {"marker": "o"},
    "Is": {"marker": "^"},
    "Kk": {"marker": "v"},
    "Mr": {"marker": "D"},
    "Ne": {"marker": "<"},
    "Sw": {"marker": ">"},
}


def style_axes(ax, xlabel, ylabel):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.grid(True, which="major",
            linestyle=CFG["grid.major.linestyle"],
            linewidth=CFG["grid.major.linewidth"],
            alpha=CFG["grid.major.alpha"])
    ax.grid(True, which="minor",
            linestyle=CFG["grid.minor.linestyle"],
            linewidth=CFG["grid.minor.linewidth"],
            alpha=CFG["grid.minor.alpha"])

    ax.tick_params(axis="both", which="major",
                   direction="out",
                   length=CFG["tick.major.size"],
                   width=CFG["tick.major.width"],
                   pad=8)
    ax.tick_params(axis="both", which="minor",
                   direction="out",
                   length=CFG["tick.minor.size"],
                   width=CFG["tick.minor.width"])


def add_legend(ax, loc="best", bbox_to_anchor=None):
    legend = ax.legend(
        loc=loc,
        bbox_to_anchor=bbox_to_anchor,
        frameon=True,
        fancybox=False,
        edgecolor="black",
        handlelength=2.6,
        handletextpad=0.5,
    )
    legend.get_frame().set_linewidth(1.0)
    return legend


def save_figure(fig, filename_base):
    fig.tight_layout()
    if CFG["save_png"]:
        fig.savefig(f"{filename_base}.png", bbox_inches=CFG["bbox_inches"])
    if CFG["save_pdf"]:
        fig.savefig(f"{filename_base}.pdf", bbox_inches=CFG["bbox_inches"])
    if CFG["save_tiff"]:
        fig.savefig(f"{filename_base}.tiff", bbox_inches=CFG["bbox_inches"])


def plot_multiline(ax, x, data_dict):
    for label, y in data_dict.items():
        ax.plot(
            x, y,
            marker=series_style[label]["marker"],
            label=label,
            markeredgewidth=0.6
        )


# ============================================================
# FIGURE 1
# Layer vs Similarity
# ============================================================
def figure_similarity_layer():
    layers = np.arange(1, 33)

    data = {
        "Af": [1.00, 0.998, 0.997, 0.997, 0.997, 0.996, 0.995, 0.994,
               0.993, 0.992, 0.991, 0.991, 0.990, 0.989, 0.988, 0.987,
               0.986, 0.984, 0.981, 0.977, 0.972, 0.967, 0.961, 0.953,
               0.946, 0.936, 0.895, 0.910, 0.890, 0.835, 0.770, 0.730],
        "Be": [0.998, 0.997, 0.996, 0.996, 0.995, 0.995, 0.994, 0.994,
               0.993, 0.992, 0.992, 0.991, 0.990, 0.989, 0.988, 0.986,
               0.984, 0.980, 0.970, 0.965, 0.952, 0.946, 0.938, 0.929,
               0.918, 0.910, 0.890, 0.868, 0.840, 0.785, 0.700, 0.655],
        "Is": [0.999, 0.998, 0.997, 0.997, 0.996, 0.996, 0.995, 0.994,
               0.993, 0.992, 0.991, 0.991, 0.990, 0.989, 0.988, 0.987,
               0.985, 0.982, 0.976, 0.973, 0.965, 0.958, 0.948, 0.940,
               0.936, 0.932, 0.915, 0.885, 0.855, 0.785, 0.700, 0.648],
        "Kk": [0.990, 0.988, 0.986, 0.990, 0.990, 0.991, 0.992, 0.993,
               0.994, 0.994, 0.994, 0.994, 0.992, 0.990, 0.985, 0.978,
               0.974, 0.968, 0.954, 0.945, 0.928, 0.913, 0.901, 0.889,
               0.868, 0.848, 0.812, 0.778, 0.735, 0.650, 0.558, 0.512],
        "Mr": [1.000, 0.999, 0.998, 0.998, 0.997, 0.997, 0.996, 0.995,
               0.994, 0.993, 0.992, 0.992, 0.991, 0.990, 0.989, 0.988,
               0.986, 0.983, 0.979, 0.975, 0.968, 0.963, 0.957, 0.950,
               0.944, 0.946, 0.935, 0.910, 0.890, 0.830, 0.755, 0.708],
        "Ne": [0.999, 0.998, 0.997, 0.997, 0.997, 0.996, 0.995, 0.994,
               0.993, 0.992, 0.991, 0.991, 0.990, 0.989, 0.988, 0.987,
               0.986, 0.983, 0.979, 0.975, 0.968, 0.962, 0.956, 0.950,
               0.940, 0.930, 0.890, 0.855, 0.820, 0.740, 0.640, 0.562],
        "Sw": [1.000, 0.999, 0.999, 0.999, 0.999, 0.998, 0.998, 0.997,
               0.997, 0.997, 0.997, 0.997, 0.996, 0.996, 0.995, 0.995,
               0.994, 0.993, 0.992, 0.990, 0.988, 0.984, 0.981, 0.976,
               0.968, 0.960, 0.935, 0.905, 0.885, 0.828, 0.770, 0.722],
    }

    fig, ax = plt.subplots(figsize=CFG["figsize_line"])
    plot_multiline(ax, layers, data)

    ax.set_xlim(0.7, 33)
    ax.set_ylim(0.50, 1.01)

    ax.set_xticks(np.arange(4, 33, 4))
    ax.set_xticks(np.arange(2, 33, 2), minor=True)

    ax.set_yticks(np.arange(0.5, 1.01, 0.1))
    ax.set_yticks(np.arange(0.55, 1.01, 0.05), minor=True)

    style_axes(ax, "Layer", "Similarity")
    add_legend(ax, loc="lower left", bbox_to_anchor=(0.03, 0.08))

    save_figure(fig, "Fig_1")


# ============================================================
# FIGURE 2
# Number of freezing bottom layers vs WER(%)
# ============================================================
def figure_freezing_bottom_layers():
    x = np.arange(10, 32)  # 10..31

    data = {
        "Af": [18.5, 18.8, 19.7, 18.5, 18.8, 18.5, 18.7, 18.7, 19.1, 19.8, 19.6, 19.7,
               21.5, 20.3, 21.6, 20.5, 20.9, 21.2, 21.25, 21.2, 21.3, 22.1],
        "Be": [12.25, 12.7, 12.95, 12.9, 12.9, 12.4, 12.55, 12.35, 12.35, 13.15, 12.4, 12.85,
               12.7, 13.25, 12.95, 12.95, 12.98, 13.3, 13.9, 13.95, 14.05, 14.5],
        "Is": [22.5, 23.0, 23.15, 22.8, 22.9, 22.5, 23.2, 23.6, 23.6, 23.6, 23.75, 23.8,
               24.15, 23.85, 23.75, 24.25, 24.35, 24.15, 24.65, 25.0, 26.85, 25.85],
        "Kk": [13.75, 13.9, 13.95, 13.35, 13.5, 13.95, 13.4, 13.55, 14.35, 14.05, 14.6, 13.65,
               14.45, 14.25, 14.7, 15.0, 15.4, 16.95, 16.1, 16.95, 17.6, 18.05],
        "Mr": [15.65, 15.1, 15.65, 15.45, 15.3, 15.2, 15.4, 15.6, 15.1, 15.3, 14.5, 14.8,
               15.0, 15.1, 15.25, 15.0, 15.05, 15.1, 15.1, 15.6, 15.7, 16.1],
        "Ne": [18.15, 18.1, 19.1, 18.6, 18.5, 18.6, 18.25, 18.75, 18.45, 18.9, 18.25, 18.7,
               18.45, 18.65, 18.65, 18.55, 19.0, 18.85, 19.2, 18.85, 19.25, 19.8],
        "Sw": [15.4, 15.25, 15.4, 15.4, 15.25, 15.5, 15.0, 15.45, 15.45, 15.3, 14.7, 14.8,
               15.1, 15.4, 15.3, 15.25, 15.35, 16.0, 16.3, 16.6, 17.2, 17.8],
    }

    fig, ax = plt.subplots(figsize=CFG["figsize_line"])
    plot_multiline(ax, x, data)

    ax.set_xlim(9.3, 31.3)
    ax.set_ylim(12.0, 27.2)

    ax.set_xticks(np.arange(10, 32, 2))
    ax.set_xticks(np.arange(10, 32, 1), minor=True)

    ax.set_yticks(np.arange(12, 28, 2))
    ax.set_yticks(np.arange(12, 27.5, 1), minor=True)

    style_axes(ax, "Number of freezing bottom layers", "WER(%)")
    add_legend(ax, loc="upper left", bbox_to_anchor=(0.99, 1.02))

    save_figure(fig, "Fig_2")


# ============================================================
# FIGURE 3
# Number of re-initialization top layers vs WER(%)
# ============================================================
def figure_reinitialization_top_layers():
    x = np.arange(1, 6)

    data = {
        "Af": [22.3, 26.0, 37.5, 91.0, 102.5],
        "Be": [16.0, 18.2, 25.0, 32.0, 99.0],
        "Is": [31.0, 33.0, 44.8, 60.0, 102.0],
        "Kk": [19.0, 20.0, 22.0, 26.0, 103.5],
        "Mr": [17.5, 18.5, 23.0, 54.0, 94.0],
        "Ne": [20.0, 22.0, 33.0, 42.5, 97.0],
        "Sw": [19.5, 20.8, 22.8, 31.8, 102.0],
    }

    fig, ax = plt.subplots(figsize=CFG["figsize_line"])
    plot_multiline(ax, x, data)

    ax.set_xlim(0.8, 5.1)
    ax.set_ylim(12, 108)

    ax.set_xticks(np.arange(1, 6, 1))
    ax.set_xticks(np.arange(1, 5.1, 0.5), minor=True)

    ax.set_yticks(np.arange(20, 101, 20))
    ax.set_yticks(np.arange(10, 111, 10), minor=True)

    style_axes(ax, "Number of re-initialization top layers", "WER(%)")
    add_legend(ax, loc="upper left", bbox_to_anchor=(0.03, 0.86))

    save_figure(fig, "Fig_3")


# ============================================================
# FIGURE 4
# d vs WER(%)
# ============================================================
def figure_d_bar():
    x_labels = ["32", "64", "128", "256"]
    values = [29.06, 28.47, 30.52, 33.04]
    x = np.arange(len(x_labels))

    fig, ax = plt.subplots(figsize=CFG["figsize_bar"])

    bars = ax.bar(x, values, width=0.8, edgecolor="black", linewidth=1.2)

    ax.set_xlim(-0.7, len(x_labels) - 0.5)
    ax.set_ylim(0, 35)

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)

    ax.set_yticks(np.arange(0, 36, 5))
    ax.set_yticks(np.arange(0, 35.1, 2.5), minor=True)

    style_axes(ax, r"$d$", "WER(%)")

    for bar, val in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            val + 0.15,
            f"{val:.2f}",
            ha="center",
            va="bottom",
            fontsize=16
        )

    save_figure(fig, "Fig_5")


# ============================================================
# FIGURE 5
# Number of top encoder layers vs WER(%)
# ============================================================
def figure_top_encoder_layers():
    x = np.arange(1, 11)

    data = {
        "Af": [23.1, 23.0, 22.85, 22.95, 22.1, 23.1, 22.45, 22.4, 21.95, 22.15],
        "Be": [15.5, 14.85, 14.7, 14.72, 14.3, 14.02, 14.03, 14.12, 14.03, 13.9],
        "Is": [29.75, 29.35, 28.95, 28.15, 27.15, 26.15, 26.65, 27.45, 27.85, 27.05],
        "Kk": [19.75, 19.0, 18.0, 17.1, 17.0, 17.1, 17.2, 16.55, 15.55, 16.4],
        "Mr": [17.8, 17.45, 17.3, 17.1, 17.05, 16.95, 16.75, 16.75, 16.7, 16.65],
        "Ne": [20.7, 20.4, 20.85, 20.45, 20.45, 20.3, 20.1, 19.8, 19.75, 20.3],
        "Sw": [19.4, 18.9, 17.75, 17.25, 16.8, 16.8, 17.3, 16.5, 16.85, 16.8],
    }

    fig, ax = plt.subplots(figsize=CFG["figsize_line"])
    plot_multiline(ax, x, data)

    ax.set_xlim(0.9, 10.1)
    ax.set_ylim(13.0, 30.0)

    ax.set_xticks(np.arange(1, 11, 1))
    ax.set_xticks(np.arange(1, 10.5, 0.5), minor=True)

    ax.set_yticks(np.arange(14, 31, 2))
    ax.set_yticks(np.arange(13, 30.5, 1), minor=True)

    style_axes(ax, "Number of top encoder layers", "WER(%)")
    add_legend(ax, loc="upper left", bbox_to_anchor=(0.99, 1.02))

    save_figure(fig, "Fig_6")


# ============================================================
# MAIN
# ============================================================
def main():
    figure_similarity_layer()
    figure_freezing_bottom_layers()
    figure_reinitialization_top_layers()
    figure_d_bar()
    figure_top_encoder_layers()
    plt.show()


if __name__ == "__main__":
    main()
