#!/usr/bin/env python3
"""Build publication-style schematic figures for Foundation Paper I.

The figures are conceptual, not empirical.  They are generated as vector PDFs
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
    "neutral": "#f5f5f5",
    "neutral_edge": "#555555",
    "dark": "#333333",
}


def setup(width=9.5, height=4.8):
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
        boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=lw,
        edgecolor=ec,
        facecolor=fc,
        zorder=2,
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
        linespacing=1.22,
        zorder=3,
    )
    return patch


def label(ax, x, y, text, fs=9, color="#333333", ha="center", weight="normal"):
    ax.text(x, y, text, fontsize=fs, color=color, ha=ha, va="center", weight=weight)


def arrow(ax, start, end, color="#333333", lw=1.2, rad=0.0, style="-|>"):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle=style,
            mutation_scale=13,
            linewidth=lw,
            color=color,
            connectionstyle=f"arc3,rad={rad}",
            shrinkA=4,
            shrinkB=4,
            zorder=1,
        )
    )


def panel_label(ax, text):
    label(ax, 0.02, 0.965, text, fs=10, weight="bold", ha="left")


def figure_core_spine():
    fig, ax = setup(height=4.2)
    panel_label(ax, "A. Minimal Tau Core spine")
    y = 0.56
    box(ax, 0.04, y, 0.14, 0.16, "source seed\n$s$", COL["warning"], COL["warning_edge"])
    box(ax, 0.25, y, 0.18, 0.16, "endpoint-blind\nresponse\n$R_\\tau(s)$", COL["parent"], COL["parent_edge"])
    box(ax, 0.50, y, 0.18, 0.16, "morphological\nbody\n$M_\\tau$", COL["morph"], COL["morph_edge"])
    box(ax, 0.76, y, 0.18, 0.16, "sector readout\n$U_i[R_\\tau(s)]$", COL["readout"], COL["readout_edge"])
    arrow(ax, (0.18, y + 0.08), (0.25, y + 0.08))
    arrow(ax, (0.43, y + 0.08), (0.50, y + 0.08))
    arrow(ax, (0.68, y + 0.08), (0.76, y + 0.08))
    label(ax, 0.215, 0.73, "not time evolution", fs=8, color=COL["warning_edge"])
    label(ax, 0.465, 0.73, "conditions readout", fs=8, color=COL["morph_edge"])
    label(ax, 0.72, 0.73, "sector exit", fs=8, color=COL["readout_edge"])

    box(
        ax,
        0.06,
        0.17,
        0.88,
        0.20,
        "Claim level: formal framework / position paper.\nNot empirical validation, not a completed physical theory.",
        "#ffffff",
        "#777777",
        fs=9,
    )
    label(ax, 0.50, 0.06, "$s \\mapsto R_\\tau(s) \\mapsto U_i(R_\\tau(s))$", fs=13, weight="bold")
    save(fig, "fig_core_spine.pdf")


def figure_block_comparison():
    fig, ax = setup(height=5.0)
    panel_label(ax, "B. Block-universe ontology versus Tau Core readout")

    # Left block: standard block universe.
    ax.add_patch(Rectangle((0.07, 0.20), 0.36, 0.58, facecolor="#f7f7f7", edgecolor="#555555", lw=1.1))
    for i in range(5):
        x = 0.10 + 0.06 * i
        ax.plot([x, x + 0.15], [0.24, 0.74], color="#9a9a9a", lw=0.8)
    for i in range(4):
        y = 0.30 + 0.10 * i
        ax.plot([0.09, 0.40], [y, y + 0.04], color="#b0b0b0", lw=0.8)
    label(ax, 0.25, 0.83, "Block-universe reading", fs=11, weight="bold")
    label(ax, 0.25, 0.13, "$\\mathrm{Reality}=M_{4D}$", fs=12, weight="bold")
    label(ax, 0.25, 0.08, "4D spacetime history is the final object", fs=8)

    # Right: Tau Core.
    box(ax, 0.58, 0.60, 0.22, 0.14, "parent response\n$R_\\tau(s)$", COL["parent"], COL["parent_edge"])
    box(ax, 0.58, 0.34, 0.22, 0.14, "4D readout\n$U_{4D}$", COL["readout"], COL["readout_edge"])
    ax.add_patch(Rectangle((0.56, 0.15), 0.26, 0.10, facecolor="#f7f7f7", edgecolor="#555555", lw=1.0))
    label(ax, 0.69, 0.20, "$M_{4D}$", fs=11, weight="bold")
    arrow(ax, (0.69, 0.60), (0.69, 0.48), color=COL["readout_edge"])
    arrow(ax, (0.69, 0.34), (0.69, 0.25), color=COL["readout_edge"])
    label(ax, 0.69, 0.83, "Tau Core reading", fs=11, weight="bold")
    label(ax, 0.69, 0.08, "$M_{4D}=U_{4D}(R_\\tau(s))$", fs=12, weight="bold")
    label(ax, 0.69, 0.03, "4D block is a sector output, not final ontology", fs=8)

    ax.plot([0.50, 0.50], [0.10, 0.88], color="#bbbbbb", lw=1.0, ls="--")
    label(ax, 0.50, 0.92, "comparison", fs=8, color="#666666")
    save(fig, "fig_block_vs_tau.pdf")


def figure_readout_atlas():
    fig, ax = setup(width=10.2, height=5.8)
    panel_label(ax, "C. Readout atlas with null and closure boundaries")
    box(ax, 0.39, 0.78, 0.22, 0.12, "parent response\n$R_\\tau(s)$", COL["parent"], COL["parent_edge"])

    nodes = [
        ("$U_{4D}$\nspacetime", 0.06),
        ("$U_{time}$\nobserver-time", 0.245),
        ("$U_q$\nquantum access", 0.43),
        ("$U_g$\ngravity", 0.615),
        ("$U_m$\nmass/source", 0.80),
    ]
    for text, x in nodes:
        box(ax, x, 0.58, 0.14, 0.10, text, COL["readout"], COL["readout_edge"], fs=8)
        arrow(ax, (0.50, 0.78), (x + 0.07, 0.68), color=COL["readout_edge"], lw=1.0)
        box(ax, x, 0.40, 0.14, 0.09, "null quotient\n$N_i$", "#ffffff", "#777777", fs=7.6)
        box(ax, x, 0.26, 0.14, 0.09, "closure test\n$C_i$", "#ffffff", "#777777", fs=7.6)
        arrow(ax, (x + 0.07, 0.58), (x + 0.07, 0.49), color="#777777", lw=0.8)
        arrow(ax, (x + 0.07, 0.40), (x + 0.07, 0.35), color="#777777", lw=0.8)
    label(ax, 0.50, 0.14, "Each sector needs its own codomain, null quotient, closure test, and validation boundary.", fs=9)
    label(ax, 0.50, 0.07, "A shared parent response does not imply automatic additivity of readout components.", fs=9)
    save(fig, "fig_readout_atlas.pdf")


def figure_defect():
    fig, ax = setup(height=5.0)
    panel_label(ax, "D. Relift failure as a readout-relative hidden defect")
    box(ax, 0.05, 0.62, 0.14, 0.12, "$r=(a,b,c)$\nparent record", COL["parent"], COL["parent_edge"], fs=8)
    box(ax, 0.29, 0.68, 0.16, 0.12, "$U_A(r)=(a,b)$", COL["readout"], COL["readout_edge"], fs=9)
    box(ax, 0.55, 0.68, 0.17, 0.12, "$J_AU_A(r)=(a,b,0)$", COL["warning"], COL["warning_edge"], fs=8)
    box(ax, 0.81, 0.68, 0.14, 0.12, "$h_A=(0,0,-c)$", COL["defect"], COL["defect_edge"], fs=8)
    arrow(ax, (0.19, 0.68), (0.29, 0.74))
    arrow(ax, (0.45, 0.74), (0.55, 0.74))
    arrow(ax, (0.72, 0.74), (0.81, 0.74))

    box(ax, 0.29, 0.36, 0.16, 0.12, "$U_B(r)=(a,c)$", COL["readout"], COL["readout_edge"], fs=9)
    box(ax, 0.55, 0.36, 0.17, 0.12, "$J_BU_B(r)=(a,0,c)$", COL["warning"], COL["warning_edge"], fs=8)
    box(ax, 0.81, 0.36, 0.14, 0.12, "$h_B=(0,-b,0)$", COL["defect"], COL["defect_edge"], fs=8)
    arrow(ax, (0.19, 0.67), (0.29, 0.42), rad=-0.08)
    arrow(ax, (0.45, 0.42), (0.55, 0.42))
    arrow(ax, (0.72, 0.42), (0.81, 0.42))

    label(ax, 0.50, 0.20, "Hiddenness is relative to the declared readout and relift policy.", fs=9)
    label(ax, 0.50, 0.12, "A defect is not automatically a new substance, force, or empirical discovery.", fs=9)
    save(fig, "fig_hidden_defect.pdf")


def figure_effective_time():
    fig, ax = setup(height=4.8)
    panel_label(ax, "E. Effective time as a readout ordering")
    # Parent record as ordered slots plus hidden component.
    x0 = 0.08
    for k in range(6):
        ax.add_patch(Rectangle((x0 + 0.055 * k, 0.62), 0.045, 0.08, facecolor="#eaf4ea", edgecolor="#2f6b35", lw=0.8))
        label(ax, x0 + 0.055 * k + 0.0225, 0.66, f"$a_{k}$", fs=8)
    ax.add_patch(Rectangle((x0 + 0.36, 0.62), 0.045, 0.08, facecolor="#ffe9e9", edgecolor="#b22222", lw=0.8))
    label(ax, x0 + 0.382, 0.66, "$c$", fs=8)
    label(ax, 0.22, 0.78, "atemporal parent record", fs=9, weight="bold")

    box(ax, 0.50, 0.66, 0.16, 0.11, "$U_{seq}$\nordered sequence", COL["readout"], COL["readout_edge"], fs=8)
    box(ax, 0.76, 0.66, 0.16, 0.11, "$\\Delta a_k=a_{k+1}-a_k$\neffective dynamics", COL["warning"], COL["warning_edge"], fs=8)
    arrow(ax, (0.44, 0.66), (0.50, 0.71))
    arrow(ax, (0.66, 0.71), (0.76, 0.71))

    box(ax, 0.50, 0.33, 0.16, 0.11, "$U_{sum}$\naggregate", COL["readout"], COL["readout_edge"], fs=8)
    box(ax, 0.76, 0.33, 0.16, 0.11, "$\\sum_k a_k$\nno internal order", COL["neutral"], COL["neutral_edge"], fs=8)
    arrow(ax, (0.44, 0.64), (0.50, 0.39), rad=-0.15)
    arrow(ax, (0.66, 0.39), (0.76, 0.39))
    label(ax, 0.50, 0.13, "The parent record need not evolve for a readout to display an ordered time parameter.", fs=9)
    save(fig, "fig_effective_time_readout.pdf")


def figure_claim_ladder():
    fig, ax = setup(width=10.2, height=5.0)
    panel_label(ax, "F. Claim-boundary ladder")
    levels = [
        ("Definition", "symbols\nand objects", COL["neutral"], COL["neutral_edge"]),
        ("Postulate", "declared\nframework", COL["warning"], COL["warning_edge"]),
        ("Conditional\ntheorem", "if assumptions\npass", COL["parent"], COL["parent_edge"]),
        ("Toy model", "mechanism\ncheck", COL["readout"], COL["readout_edge"]),
        ("Empirical\nvalidation", "held-out data\n+ controls", COL["defect"], COL["defect_edge"]),
    ]
    x = 0.045
    for idx, (title, subtitle, fc, ec) in enumerate(levels):
        box(ax, x, 0.54, 0.15, 0.20, f"{title}\n{subtitle}", fc, ec, fs=8.0)
        if idx < len(levels) - 1:
            arrow(ax, (x + 0.15, 0.64), (x + 0.19, 0.64))
        x += 0.19
    box(
        ax,
        0.12,
        0.20,
        0.76,
        0.18,
        "Foundation Paper I stops before empirical validation.\nLater branches must add units, known limits, covariance,\ncontrols, and failure rules.",
        "#ffffff",
        "#777777",
        fs=8.8,
    )
    save(fig, "fig_claim_ladder.pdf")


def figure_status_matrix():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
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
    # Codes: 0 blank, 1 present, 2 explicitly not claimed, 3 open blocker.
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
    ax.grid(which="minor", color="#777777", linestyle="-", linewidth=0.7)
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
