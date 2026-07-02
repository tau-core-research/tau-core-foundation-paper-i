#!/usr/bin/env python3
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
SRC_FIG = ROOT / "paperI_submission_source" / "figures"


def box(ax, xy, w, h, text, fc="#f7fbff", ec="#3b6ea8", fs=9):
    patch = FancyBboxPatch(
        xy,
        w,
        h,
        boxstyle="round,pad=0.03,rounding_size=0.03",
        linewidth=1.2,
        edgecolor=ec,
        facecolor=fc,
    )
    ax.add_patch(patch)
    ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center", fontsize=fs)


def arrow(ax, start, end):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=13,
            linewidth=1.1,
            color="#333333",
        )
    )


def save(fig, name):
    for d in (FIG, SRC_FIG):
        d.mkdir(parents=True, exist_ok=True)
        fig.savefig(d / name, bbox_inches="tight")
    plt.close(fig)


def figure_core_spine():
    fig, ax = plt.subplots(figsize=(9.5, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis("off")
    box(ax, (0.2, 1.1), 1.4, 0.8, "seed\ns", "#fff7ec", "#b45f06")
    box(ax, (2.1, 1.1), 1.8, 0.8, "Tau response\nR_tau(s)", "#eef7ee", "#3c7d3c")
    box(ax, (4.6, 1.1), 1.9, 0.8, "morphological\nbody M_tau", "#f4f0ff", "#6a51a3")
    box(ax, (7.2, 1.1), 2.0, 0.8, "sector readouts\nU_i(R_tau(s))", "#eef5ff", "#2f5d9b")
    arrow(ax, (1.65, 1.5), (2.05, 1.5))
    arrow(ax, (3.95, 1.5), (4.55, 1.5))
    arrow(ax, (6.55, 1.5), (7.15, 1.5))
    ax.text(
        5,
        0.35,
        "Foundation Paper I claim: a formal readout architecture, not empirical validation.",
        ha="center",
        fontsize=9,
        color="#444444",
    )
    save(fig, "fig_core_spine.pdf")


def figure_readout_atlas():
    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    box(ax, (3.85, 4.65), 2.3, 0.75, "parent response\nR_tau(s)", "#eef7ee", "#3c7d3c")
    labels = [
        ("U_4D", "spacetime\nreadout", 0.5, 2.55),
        ("U_time", "observer-time\nreadout", 2.6, 1.2),
        ("U_q", "quantum\nreadout", 4.15, 2.55),
        ("U_g", "gravity\nreadout", 6.1, 1.2),
        ("U_m", "mass/source\nreadout", 7.9, 2.55),
    ]
    for sym, text, x, y in labels:
        box(ax, (x, y), 1.55, 0.85, f"{sym}\n{text}", "#f7fbff", "#2f5d9b", fs=8)
        arrow(ax, (5.0, 4.65), (x + 0.78, y + 0.9))
    ax.text(5, 0.35, "Each readout has its own nulls, closure tests, and validation boundary.", ha="center", fontsize=9)
    save(fig, "fig_readout_atlas.pdf")


def figure_defect():
    fig, ax = plt.subplots(figsize=(9.5, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3.5)
    ax.axis("off")
    box(ax, (0.4, 1.75), 1.5, 0.65, "r in R_tau", "#eef7ee", "#3c7d3c")
    box(ax, (2.55, 1.75), 1.7, 0.65, "readout\nU_A(r)", "#eef5ff", "#2f5d9b")
    box(ax, (5.0, 1.75), 1.6, 0.65, "relift\nJ_A U_A(r)", "#fff7ec", "#b45f06")
    box(ax, (7.35, 1.75), 1.85, 0.65, "defect\nh_A=J_AU_A(r)-r", "#fff0f0", "#b22222", fs=8)
    arrow(ax, (1.95, 2.08), (2.5, 2.08))
    arrow(ax, (4.3, 2.08), (4.95, 2.08))
    arrow(ax, (6.65, 2.08), (7.3, 2.08))
    box(ax, (2.55, 0.55), 1.7, 0.65, "readout\nU_B(r)", "#eef5ff", "#2f5d9b")
    box(ax, (5.0, 0.55), 1.6, 0.65, "relift\nJ_B U_B(r)", "#fff7ec", "#b45f06")
    box(ax, (7.35, 0.55), 1.85, 0.65, "defect\nh_B", "#fff0f0", "#b22222", fs=8)
    arrow(ax, (1.95, 2.0), (2.5, 0.95))
    arrow(ax, (4.3, 0.88), (4.95, 0.88))
    arrow(ax, (6.65, 0.88), (7.3, 0.88))
    ax.text(5, 3.05, "Hidden defects are readout-relative incompleteness records.", ha="center", fontsize=10)
    save(fig, "fig_hidden_defect.pdf")


def figure_claim_ladder():
    fig, ax = plt.subplots(figsize=(9.5, 3.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    items = [
        ("definition", "#f0f0f0"),
        ("postulate", "#fff7ec"),
        ("conditional\ntheorem", "#eef7ee"),
        ("toy\nmodel", "#eef5ff"),
        ("empirical\nvalidation", "#ffecec"),
    ]
    x = 0.35
    for i, (label, color) in enumerate(items):
        box(ax, (x, 1.55), 1.55, 0.8, label, color, "#555555")
        if i < len(items) - 1:
            arrow(ax, (x + 1.6, 1.95), (x + 2.0, 1.95))
        x += 1.95
    ax.text(
        5,
        0.65,
        "This paper stops at definitions, postulates, conditional routes, and toy mechanisms.",
        ha="center",
        fontsize=9,
    )
    ax.text(5, 0.25, "It does not claim empirical validation or a completed physical theory.", ha="center", fontsize=9)
    save(fig, "fig_claim_ladder.pdf")


def main():
    figure_core_spine()
    figure_readout_atlas()
    figure_defect()
    figure_claim_ladder()


if __name__ == "__main__":
    main()
