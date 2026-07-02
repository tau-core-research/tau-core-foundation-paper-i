#!/usr/bin/env python3
"""Build publication-style schematic figures for Foundation Paper I.

The figures are conceptual, not empirical. They are generated as vector PDFs
so the paper remains reproducible and arXiv-friendly.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
SRC_FIG = ROOT / "paperI_submission_source" / "figures"

mpl.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "axes.linewidth": 0.8,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }
)

COL = {
    "parent": "#eaf4ea",
    "parent_edge": "#2f6b35",
    "morph": "#f3efff",
    "morph_edge": "#6247aa",
    "readout": "#eaf2ff",
    "readout_edge": "#285c9f",
    "warning": "#fff1e1",
    "warning_edge": "#ad5a00",
    "defect": "#ffe9e9",
    "defect_edge": "#b22222",
    "neutral": "#f7f7f7",
    "neutral_edge": "#555555",
    "dark": "#333333",
    "grid": "#777777",
}


def setup(width=9.8, height=4.8):
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def save(fig, name):
    for d in (FIG, SRC_FIG):
        d.mkdir(parents=True, exist_ok=True)
        fig.savefig(d / name, bbox_inches="tight")
    plt.close(fig)


def box(ax, x, y, w, h, text, fc, ec, fs=9, lw=1.1, align="center"):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.010,rounding_size=0.014",
        linewidth=lw,
        edgecolor=ec,
        facecolor=fc,
        zorder=3,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha=align,
        va="center",
        fontsize=fs,
        color="#111111",
        linespacing=1.20,
        zorder=4,
    )
    return patch


def label(ax, x, y, text, fs=9, color="#333333", ha="center", va="center", weight="normal", bbox=False):
    kwargs = {}
    if bbox:
        kwargs["bbox"] = dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.96)
    ax.text(x, y, text, fontsize=fs, color=color, ha=ha, va=va, weight=weight, zorder=5, **kwargs)


def arrow(ax, start, end, color="#333333", lw=1.15, rad=0.0, style="-|>", z=2):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle=style,
            mutation_scale=12,
            linewidth=lw,
            color=color,
            connectionstyle=f"arc3,rad={rad}",
            shrinkA=0,
            shrinkB=0,
            zorder=z,
        )
    )


def line(ax, xs, ys, color="#333333", lw=1.0, z=1):
    ax.plot(xs, ys, color=color, lw=lw, zorder=z)


def panel_label(ax, text):
    label(ax, 0.02, 0.965, text, fs=10, weight="bold", ha="left")


def figure_core_spine():
    fig, ax = setup(width=10.2, height=4.4)
    panel_label(ax, "A. Minimal Tau Core spine")
    y = 0.58
    nodes = [
        (0.055, 0.14, "source seed\n$s$", COL["warning"], COL["warning_edge"]),
        (0.285, 0.18, "endpoint-blind\nresponse\n$R_\\tau(s)$", COL["parent"], COL["parent_edge"]),
        (0.535, 0.18, "morphological\nbody\n$M_\\tau$", COL["morph"], COL["morph_edge"]),
        (0.785, 0.16, "sector readout\n$U_i[R_\\tau(s)]$", COL["readout"], COL["readout_edge"]),
    ]
    centers = []
    for x, w, text, fc, ec in nodes:
        box(ax, x, y, w, 0.16, text, fc, ec, fs=9)
        centers.append((x, x + w, x + w / 2))
    # Arrows run only in the gaps between boxes; labels sit above with white backing.
    arrow(ax, (centers[0][1] + 0.018, y + 0.08), (centers[1][0] - 0.018, y + 0.08), color=COL["dark"])
    arrow(ax, (centers[1][1] + 0.018, y + 0.08), (centers[2][0] - 0.018, y + 0.08), color=COL["dark"])
    arrow(ax, (centers[2][1] + 0.018, y + 0.08), (centers[3][0] - 0.018, y + 0.08), color=COL["dark"])
    label(ax, 0.245, 0.80, "not time evolution", fs=7.8, color=COL["warning_edge"], bbox=True)
    label(ax, 0.500, 0.80, "conditions readout", fs=7.8, color=COL["morph_edge"], bbox=True)
    label(ax, 0.745, 0.80, "sector exit", fs=7.8, color=COL["readout_edge"], bbox=True)
    box(
        ax,
        0.18,
        0.24,
        0.64,
        0.16,
        "Claim level: formal framework / position paper\nnot empirical validation; not a completed physical theory",
        "#ffffff",
        "#777777",
        fs=9,
    )
    label(ax, 0.50, 0.10, "$s \\mapsto R_\\tau(s) \\mapsto U_i(R_\\tau(s))$", fs=13, weight="bold")
    save(fig, "fig_core_spine.pdf")


def figure_block_comparison():
    fig, ax = setup(width=10.2, height=5.1)
    panel_label(ax, "B. Block-universe ontology versus Tau Core readout")

    # Left: a clean 4D block sketch.
    ax.add_patch(Rectangle((0.07, 0.25), 0.34, 0.48, facecolor="#f8f8f8", edgecolor="#555555", lw=1.1, zorder=2))
    for i in range(5):
        x = 0.11 + 0.052 * i
        line(ax, [x, x + 0.14], [0.29, 0.69], color="#9a9a9a", lw=0.8, z=3)
    for i in range(4):
        y = 0.34 + 0.08 * i
        line(ax, [0.10, 0.38], [y, y + 0.035], color="#b0b0b0", lw=0.8, z=3)
    label(ax, 0.24, 0.82, "Block-universe reading", fs=11, weight="bold")
    label(ax, 0.24, 0.16, "$\\mathrm{Reality}=M_{4D}$", fs=12, weight="bold")
    label(ax, 0.24, 0.10, "4D spacetime history is the final object", fs=8)

    # Right: parent response -> readout -> 4D block, vertically separated.
    box(ax, 0.62, 0.62, 0.22, 0.13, "parent response\n$R_\\tau(s)$", COL["parent"], COL["parent_edge"])
    box(ax, 0.62, 0.40, 0.22, 0.13, "4D readout\n$U_{4D}$", COL["readout"], COL["readout_edge"])
    box(ax, 0.62, 0.20, 0.22, 0.10, "$M_{4D}$", COL["neutral"], COL["neutral_edge"], fs=11)
    arrow(ax, (0.73, 0.62), (0.73, 0.53), color=COL["readout_edge"])
    arrow(ax, (0.73, 0.40), (0.73, 0.30), color=COL["readout_edge"])
    label(ax, 0.73, 0.82, "Tau Core reading", fs=11, weight="bold")
    label(ax, 0.73, 0.13, "$M_{4D}=U_{4D}(R_\\tau(s))$", fs=12, weight="bold")
    label(ax, 0.73, 0.07, "4D block is a sector output, not final ontology", fs=8)

    line(ax, [0.50, 0.50], [0.10, 0.86], color="#bbbbbb", lw=1.0, z=1)
    label(ax, 0.50, 0.90, "comparison", fs=8, color="#666666", bbox=True)
    save(fig, "fig_block_vs_tau.pdf")


def figure_readout_atlas():
    fig, ax = setup(width=10.8, height=5.9)
    panel_label(ax, "C. Readout atlas with null and closure boundaries")
    box(ax, 0.40, 0.79, 0.20, 0.11, "parent response\n$R_\\tau(s)$", COL["parent"], COL["parent_edge"])

    # A bus avoids arrows crossing node labels.
    bus_y = 0.71
    line(ax, [0.13, 0.87], [bus_y, bus_y], color=COL["readout_edge"], lw=1.0, z=1)
    arrow(ax, (0.50, 0.79), (0.50, bus_y), color=COL["readout_edge"], lw=1.0)

    nodes = [
        ("$U_{4D}$\nspacetime", 0.06),
        ("$U_{time}$\nobserver-time", 0.245),
        ("$U_q$\nquantum access", 0.43),
        ("$U_g$\ngravity", 0.615),
        ("$U_m$\nmass/source", 0.80),
    ]
    for text, x in nodes:
        cx = x + 0.07
        arrow(ax, (cx, bus_y), (cx, 0.64), color=COL["readout_edge"], lw=1.0)
        box(ax, x, 0.54, 0.14, 0.10, text, COL["readout"], COL["readout_edge"], fs=8)
        arrow(ax, (cx, 0.54), (cx, 0.47), color="#777777", lw=0.8)
        box(ax, x, 0.38, 0.14, 0.09, "null quotient\n$N_i$", "#ffffff", "#777777", fs=7.6)
        arrow(ax, (cx, 0.38), (cx, 0.32), color="#777777", lw=0.8)
        box(ax, x, 0.23, 0.14, 0.09, "closure test\n$C_i$", "#ffffff", "#777777", fs=7.6)
    label(ax, 0.50, 0.13, "Each sector needs its own codomain, null quotient, closure test, and validation boundary.", fs=9)
    label(ax, 0.50, 0.07, "A shared parent response does not imply automatic additivity of readout components.", fs=9)
    save(fig, "fig_readout_atlas.pdf")


def figure_defect():
    fig, ax = setup(width=10.4, height=5.4)
    panel_label(ax, "D. Relift failure as a readout-relative hidden defect")
    box(ax, 0.04, 0.54, 0.16, 0.14, "$r=(a,b,c)$\nparent record", COL["parent"], COL["parent_edge"], fs=8.5)

    rows = [
        (0.68, "$U_A(r)=(a,b)$", "$J_AU_A(r)=(a,b,0)$", "$h_A=(0,0,-c)$"),
        (0.35, "$U_B(r)=(a,c)$", "$J_BU_B(r)=(a,0,c)$", "$h_B=(0,-b,0)$"),
    ]
    for y, u, relift, defect in rows:
        box(ax, 0.30, y, 0.17, 0.11, u, COL["readout"], COL["readout_edge"], fs=8.8)
        box(ax, 0.56, y, 0.19, 0.11, relift, COL["warning"], COL["warning_edge"], fs=8.3)
        box(ax, 0.83, y, 0.13, 0.11, defect, COL["defect"], COL["defect_edge"], fs=8.3)
        arrow(ax, (0.20, 0.61), (0.30, y + 0.055), color=COL["dark"], rad=0.0)
        arrow(ax, (0.47, y + 0.055), (0.56, y + 0.055), color=COL["dark"])
        arrow(ax, (0.75, y + 0.055), (0.83, y + 0.055), color=COL["dark"])
    label(ax, 0.385, 0.84, "readout", fs=8, color=COL["readout_edge"], weight="bold")
    label(ax, 0.655, 0.84, "canonical relift", fs=8, color=COL["warning_edge"], weight="bold")
    label(ax, 0.895, 0.84, "hidden defect", fs=8, color=COL["defect_edge"], weight="bold")
    box(
        ax,
        0.18,
        0.12,
        0.64,
        0.13,
        "Hiddenness is relative to the declared readout and relift policy.\nA defect is not automatically a new substance, force, or empirical discovery.",
        "#ffffff",
        "#777777",
        fs=8.8,
    )
    save(fig, "fig_hidden_defect.pdf")


def figure_effective_time():
    fig, ax = setup(width=10.4, height=5.1)
    panel_label(ax, "E. Effective time as a readout ordering")
    label(ax, 0.20, 0.80, "atemporal parent record", fs=9, weight="bold")
    x0 = 0.06
    for k in range(6):
        ax.add_patch(Rectangle((x0 + 0.055 * k, 0.65), 0.045, 0.075, facecolor=COL["parent"], edgecolor=COL["parent_edge"], lw=0.8, zorder=3))
        label(ax, x0 + 0.055 * k + 0.0225, 0.687, f"$a_{k}$", fs=8)
    ax.add_patch(Rectangle((x0 + 0.36, 0.65), 0.045, 0.075, facecolor=COL["defect"], edgecolor=COL["defect_edge"], lw=0.8, zorder=3))
    label(ax, x0 + 0.382, 0.687, "$c$", fs=8)

    # Branch from a clean split point, not from a text box.
    split = (0.46, 0.687)
    arrow(ax, (0.43, 0.687), split, color=COL["dark"])
    line(ax, [split[0], split[0]], [0.47, 0.72], color=COL["dark"], lw=1.0, z=1)

    box(ax, 0.56, 0.66, 0.16, 0.11, "$U_{seq}$\nordered sequence", COL["readout"], COL["readout_edge"], fs=8)
    box(ax, 0.80, 0.66, 0.15, 0.11, "$\\Delta a_k$\neffective dynamics", COL["warning"], COL["warning_edge"], fs=8)
    arrow(ax, (split[0], 0.72), (0.56, 0.715), color=COL["dark"])
    arrow(ax, (0.72, 0.715), (0.80, 0.715), color=COL["dark"])

    box(ax, 0.56, 0.39, 0.16, 0.11, "$U_{sum}$\naggregate", COL["readout"], COL["readout_edge"], fs=8)
    box(ax, 0.80, 0.39, 0.15, 0.11, "$\\sum_k a_k$\nno internal order", COL["neutral"], COL["neutral_edge"], fs=8)
    arrow(ax, (split[0], 0.47), (0.56, 0.445), color=COL["dark"])
    arrow(ax, (0.72, 0.445), (0.80, 0.445), color=COL["dark"])
    label(ax, 0.50, 0.17, "The parent record need not evolve for a readout to display an ordered time parameter.", fs=9)
    save(fig, "fig_effective_time_readout.pdf")


def figure_claim_ladder():
    fig, ax = setup(width=10.4, height=5.0)
    panel_label(ax, "F. Claim-boundary ladder")
    levels = [
        ("Definition", "symbols\nand objects", COL["neutral"], COL["neutral_edge"]),
        ("Postulate", "declared\nframework", COL["warning"], COL["warning_edge"]),
        ("Conditional\ntheorem", "if assumptions\npass", COL["parent"], COL["parent_edge"]),
        ("Toy model", "mechanism\ncheck", COL["readout"], COL["readout_edge"]),
        ("Empirical\nvalidation", "held-out data\n+ controls", COL["defect"], COL["defect_edge"]),
    ]
    xs = [0.055, 0.245, 0.435, 0.625, 0.815]
    w = 0.145
    for idx, (title, subtitle, fc, ec) in enumerate(levels):
        box(ax, xs[idx], 0.55, w, 0.19, f"{title}\n{subtitle}", fc, ec, fs=8.0)
        if idx < len(levels) - 1:
            arrow(ax, (xs[idx] + w + 0.015, 0.645), (xs[idx + 1] - 0.015, 0.645), color=COL["dark"])
    box(
        ax,
        0.16,
        0.22,
        0.68,
        0.17,
        "Foundation Paper I stops before empirical validation.\nLater branches must add units, known limits, covariance,\ncontrols, and failure rules.",
        "#ffffff",
        "#777777",
        fs=8.8,
    )
    save(fig, "fig_claim_ladder.pdf")


def figure_status_matrix():
    fig, ax = plt.subplots(figsize=(10.4, 4.9))
    rows = [
        "Tau substrate",
        "Seed-response map",
        "Morphological body",
        "Sector readouts",
        "Effective time",
        "Hidden defect",
        "GR / quantum / QFT",
        "Empirical validation",
    ]
    cols = ["Defined", "Postulated", "Toy mechanism", "Validated", "Open blocker"]
    data = np.array(
        [
            [1, 1, 0, 2, 3],
            [1, 1, 0, 2, 3],
            [1, 1, 0, 2, 3],
            [1, 1, 1, 2, 3],
            [1, 1, 1, 2, 3],
            [1, 1, 1, 2, 3],
            [0, 0, 0, 2, 3],
            [0, 0, 0, 2, 3],
        ],
        dtype=int,
    )
    colors = ["#ffffff", "#dff0df", "#ffe7c7", "#f2dede"]
    cmap = mpl.colors.ListedColormap(colors)
    ax.imshow(data, cmap=cmap, vmin=0, vmax=3, aspect="auto")
    ax.set_xticks(range(len(cols)))
    ax.set_xticklabels(cols, fontsize=8)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels(rows, fontsize=8)
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False, length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks(np.arange(-0.5, len(cols), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(rows), 1), minor=True)
    ax.grid(which="minor", color=COL["grid"], linestyle="-", linewidth=0.7)
    ax.tick_params(which="minor", bottom=False, left=False)
    labels = {1: "yes", 2: "not\nclaimed", 3: "open"}
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i, j]:
                ax.text(j, i, labels[data[i, j]], ha="center", va="center", fontsize=7.6, color="#111111")
    ax.set_title("G. Foundation Paper I claim-status matrix", loc="left", fontsize=10, weight="bold", pad=28)
    ax.text(
        0.5,
        -0.16,
        "Green cells mark framework content supplied here; orange/red cells mark explicit non-claims or blockers.",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=8.5,
        color="#333333",
    )
    fig.tight_layout(pad=1.6)
    save(fig, "fig_status_matrix.pdf")


def main():
    figure_core_spine()
    figure_block_comparison()
    figure_readout_atlas()
    figure_defect()
    figure_effective_time()
    figure_claim_ladder()
    figure_status_matrix()


if __name__ == "__main__":
    main()
