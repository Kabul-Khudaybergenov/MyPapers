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
    "figsize_heatmap": (7.4, 6.2),
    "figsize_grouped_bar": (9.8, 6.2),

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
        "Kk": [0.990, 0.988, 0.986, 0.990, 0.990, 0.991, 0.992, 0.993,
               0.994, 0.994, 0.994, 0.994, 0.992, 0.990, 0.985, 0.978,
               0.974, 0.968, 0.954, 0.945, 0.928, 0.913, 0.901, 0.889,
               0.868, 0.848, 0.812, 0.778, 0.735, 0.650, 0.558, 0.512],
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
        "Kk": [13.75, 13.9, 13.95, 13.39, 13.5, 13.95, 13.4, 13.55, 14.35, 14.05, 14.6, 13.65,
               14.45, 14.25, 14.7, 15.0, 15.4, 16.95, 16.1, 16.95, 17.6, 18.05],
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
        "Kk": [18.75, 20.0, 22.0, 26.0, 103.5],
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
    values = [16.82, 15.68, 16.74, 17.96]
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
        "Kk": [19.75, 19.0, 18.0, 17.1, 17.0, 17.1, 17.2, 16.55, 15.59, 16.4],
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
# FIGURE 7
# Special-character confusion matrix
# ============================================================
def figure_special_character_confusion():
    reference_chars = ["á", "ó", "ú", "ı", "ń", "ś", "ǵ"]
    predicted_chars = ["a", "o", "u", "i", "n", "s", "g"]
    counts = np.array([
        [22, 0, 0, 0, 0, 0, 0],
        [0, 31, 0, 0, 0, 0, 0],
        [0, 0, 27, 0, 0, 0, 0],
        [0, 0, 0, 40, 0, 0, 0],
        [0, 0, 0, 0, 18, 0, 0],
        [0, 0, 0, 0, 0, 12, 0],
        [0, 0, 0, 0, 0, 0, 8],
    ])

    fig, ax = plt.subplots(figsize=CFG["figsize_heatmap"])
    image = ax.imshow(counts, cmap="YlOrRd", aspect="equal")

    ax.set_xticks(np.arange(len(predicted_chars)))
    ax.set_yticks(np.arange(len(reference_chars)))
    ax.set_xticklabels(predicted_chars)
    ax.set_yticklabels(reference_chars)

    ax.set_xticks(np.arange(-0.5, len(predicted_chars), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(reference_chars), 1), minor=True)
    ax.grid(which="minor", color="white", linestyle="-", linewidth=1.5)
    ax.tick_params(which="minor", bottom=False, left=False)

    for row in range(counts.shape[0]):
        for col in range(counts.shape[1]):
            value = counts[row, col]
            if value > 0:
                ax.text(
                    col,
                    row,
                    f"{value}",
                    ha="center",
                    va="center",
                    color="black",
                    fontsize=18,
                    fontweight="bold",
                )

    style_axes(ax, "Predicted character", "Reference character")
    colorbar = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    colorbar.set_label("Substitution count", fontweight="bold")
    colorbar.ax.tick_params(labelsize=14)

    save_figure(fig, "Fig_7")


# ============================================================
# FIGURE 8
# Multilingual WER trade-off across adaptation methods
# ============================================================
def figure_multilingual_tradeoff():
    languages = ["Karakalpak", "Kazakh", "Uzbek", "Russian", "English"]
    methods = ["PT", "FT", "BAFT", "LoRAFT"]
    data = {
        "PT": [37.7, 18.2, 21.5, 12.4, 3.8],
        "FT": [13.5, 22.8, 28.1, 15.9, 5.1],
        "BAFT": [15.7, 18.9, 22.4, 13.1, 4.1],
        "LoRAFT": [18.6, 19.1, 22.7, 12.9, 4.0],
    }

    x = np.arange(len(languages))
    width = 0.18
    offsets = np.linspace(-1.5 * width, 1.5 * width, len(methods))

    fig, ax = plt.subplots(figsize=CFG["figsize_grouped_bar"])
    for method, offset in zip(methods, offsets):
        values = data[method]
        bars = ax.bar(
            x + offset,
            values,
            width,
            label=method,
            edgecolor="black",
            linewidth=1.0,
        )
        for bar, value in zip(bars, values):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value + 0.35,
                f"{value:.1f}",
                ha="center",
                va="bottom",
                fontsize=11,
                rotation=90,
            )

    ax.set_xlim(-0.6, len(languages) - 0.4)
    ax.set_ylim(0, 42)
    ax.set_xticks(x)
    ax.set_xticklabels(languages)
    ax.set_yticks(np.arange(0, 43, 5))
    ax.set_yticks(np.arange(0, 42.5, 2.5), minor=True)

    style_axes(ax, "Test language", "WER(%)")
    add_legend(ax, loc="upper right")

    save_figure(fig, "Fig_8")


# ============================================================
# MAIN
# ============================================================
def main():
    figure_similarity_layer()
    figure_freezing_bottom_layers()
    figure_reinitialization_top_layers()
    figure_d_bar()
    figure_top_encoder_layers()
    figure_special_character_confusion()
    figure_multilingual_tradeoff()
    plt.close("all")


if __name__ == "__main__":
    main()
