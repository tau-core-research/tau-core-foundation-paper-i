from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "paperI_submission_source" / "main.tex"


def test_required_files_exist():
    required = [
        ROOT / "README.md",
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
    assert "Foundation Paper I" in text
    assert "Atemporal Morphological Readout Framework" in text
    assert "does not claim empirical validation" in text
    assert "does not derive general relativity" in text
    assert "does not derive quantum mechanics" in text
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


def test_figures_included():
    text = TEX.read_text()
    for fig in [
        "fig_core_spine.pdf",
        "fig_block_vs_tau.pdf",
        "fig_readout_atlas.pdf",
        "fig_hidden_defect.pdf",
        "fig_effective_time_readout.pdf",
        "fig_claim_ladder.pdf",
        "fig_status_matrix.pdf",
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
        "figures/fig_hidden_defect.pdf",
        "figures/fig_effective_time_readout.pdf",
        "figures/fig_claim_ladder.pdf",
        "figures/fig_status_matrix.pdf",
    ]:
        assert fig in names
    assert all(not name.endswith(".aux") for name in names)
