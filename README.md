# Tau Core Foundation Paper I

Private foundation-paper repository:

**Tau Core: An Atemporal Morphological Readout Framework for Emergent Physical Dynamics**

This is the first Roman-numbered Tau Core foundation paper.  It is deliberately
separate from the Arabic-numbered Paper 1--14 empirical/protocol sequence.

## Main Claim

The paper proposes a formal vocabulary in which observed physical dynamics are
treated as sector readouts of an endpoint-blind parent response:

```text
s -> R_tau(s) -> U_i(R_tau(s)).
```

It argues that physical time, 4D spacetime description, quantum state,
gravitational response, and observer-time can be framed as readout channels
rather than primitive inputs.

## Does Not Claim

- It does not claim empirical validation of Tau Core.
- It does not derive physical time, GR, QFT, the Standard Model, or LCDM.
- It does not replace dark matter, dark energy, or general relativity.
- It does not claim that any Paper 1--14 numerical result proves the framework.
- It does not present a final parent action or a complete physical theory.

## Included Material

- `paperI_submission_source/main.tex`: manuscript source.
- `paperI_submission_source/refs.bib`: references.
- `figures/`: generated schematic figures.
- `scripts/`: figure, PDF, arXiv, and reproduction scripts.
- `tests/`: smoke tests for the public package.

## Reproduce

```bash
python scripts/reproduce.py
```

Expected terminal marker:

```text
FOUNDATION_PAPER_I_REPRODUCTION_COMPLETE
```

## Scope

This repository is a position-paper / formal-conjecture package.  Its job is
to make the Tau Core parent-state/readout vocabulary discussable without
smuggling in a completed theory.
