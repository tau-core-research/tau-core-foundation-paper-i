from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "paperI_submission_source" / "main.tex"


def test_required_files_exist():
    required = [
        ROOT / "README.md",
        ROOT / "REVIEWER_READINESS.md",
        ROOT / "CITATION.cff",
        ROOT / "DATA_NOTICE.md",
        ROOT / "paperI_submission_source" / "main.tex",
        ROOT / "paperI_submission_source" / "refs.bib",
        ROOT / "paperI_submission_source" / "main.pdf",
        ROOT / "arxiv_submission_source.zip",
    ]
    for path in required:
        assert path.exists(), path


def test_claim_boundary_markers():
    text = TEX.read_text()
    normalized = " ".join(text.split())
    assert "Foundation Paper I" in text
    assert "Atemporal Morphological Readout Framework" in text
    assert "conditional minimum-viable physical completion" in text
    assert "does not claim empirical validation" in text
    assert "nature-level selection" in text
    assert "conditional standard-limit recovery" in text
    assert "not a universal time atom" in text
    assert "Record occurrence and finite A8b are independent" in text
    assert "qor-three-condition-conjunction" in text
    assert "Finite source-signature representation uniqueness" in text
    assert "Primary-SHR recovery differential generates affiliation" in text
    assert "Blockwise spectral-to-amplitude transfer" in text
    assert "Universal-seed rich-body recovery" in text
    assert "complete-body realization defect" in text
    assert "A4-SRCMIN" in text
    assert "prop:finite-source-signature-uniqueness" in text
    assert "prop:marginal-joint-nogo" in text
    assert "Sufficient internal realization of finite A8b" in text
    assert "Pathwise A8b and the holonomy boundary" in text
    assert "unchanged narrow parent does not contain or select this two-leg carrier" in normalized
    assert "source-frozen claim-complete descriptor" in text
    assert "irreversible CPTP relation" in text
    assert "commuting records alone cannot identify reversibility" in text
    assert "coherent off-diagonal witness" in text
    assert "FOC-7" in text
    assert "energy-sharing same-reduct completion" in normalized
    assert "traced two-leg source and source-irredundant branch" in normalized
    assert "physical filling by one full microscopic Tau action remains open" in normalized
    forbidden = [
        "we prove Tau Core",
        "dark matter is explained",
        "dark energy is explained",
        "replaces general relativity",
        "derives the Standard Model",
    ]
    lower = text.lower()
    for phrase in forbidden:
        assert phrase not in lower


def test_finite_response_countermodel_and_exact_branch():
    y1, y2, lam = 0.2, 0.3, 0.7

    def response(y):
        return y + lam * y**2

    defect = response(y1 + y2) - response(y1) - response(y2)
    assert abs(defect - 2 * lam * y1 * y2) < 1e-12
    assert defect != 0

    exact_defect = (y1 + y2) - y1 - y2
    assert abs(exact_defect) < 1e-12


def test_figures_included():
    text = TEX.read_text()
    for fig in [
        "fig_core_spine.pdf",
        "fig_block_vs_tau.pdf",
        "fig_readout_atlas.pdf",
        "fig_cross_scale_readout_composition.pdf",
        "fig_effective_time_readout.pdf",
        "fig_claim_ladder.pdf",
        "fig_status_matrix.pdf",
        "fig_mvp_closure.pdf",
        "fig_common_functional.pdf",
        "fig_standard_limits.pdf",
        "fig_qor_prediction.pdf",
    ]:
        assert fig in text
        assert (ROOT / "paperI_submission_source" / "figures" / fig).exists()


def test_arxiv_zip_source_only():
    zip_path = ROOT / "arxiv_submission_source.zip"
    with zipfile.ZipFile(zip_path) as zf:
        names = zf.namelist()
    assert "main.tex" in names
    assert "refs.bib" in names
    assert "main.pdf" not in names
    for fig in [
        "figures/fig_core_spine.pdf",
        "figures/fig_block_vs_tau.pdf",
        "figures/fig_readout_atlas.pdf",
        "figures/fig_cross_scale_readout_composition.pdf",
        "figures/fig_hidden_defect.pdf",
        "figures/fig_effective_time_readout.pdf",
        "figures/fig_claim_ladder.pdf",
        "figures/fig_status_matrix.pdf",
        "figures/fig_mvp_closure.pdf",
        "figures/fig_common_functional.pdf",
        "figures/fig_standard_limits.pdf",
        "figures/fig_qor_prediction.pdf",
    ]:
        assert fig in names
    assert all(not name.endswith(".aux") for name in names)
