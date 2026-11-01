# Estabilización del proyecto LaTeX

## Objective
Improve reproducibility, source organization, and local handling of personal data without changing the valid cover styles or compiling the project.

## Authorized scope
- Repository root: `main/`
- Preserve all files under `caratulas/` as intentional cover styles.
- Do not remove or rewrite the cover variants.
- Do not perform compilation or alter generated PDFs.
- Do not add a QA section or QA-related work.

## Tasks

- [x] EST-01 — Replace absolute asset paths with repository-relative paths and make missing logo references explicit.
- [x] EST-02 — Add a local LaTeX data configuration pattern using a tracked example and an ignored local file; replace personal-data literals in active sources where practical.
- [x] EST-03 — Extend `.gitignore` for local data, CodeGraph metadata, and LaTeX build output without ignoring deliverable PDFs or source assets.
- [x] EST-04 — Remove only known generated auxiliary files from the previous manual compilation; do not remove user deliverables.
- [x] EST-05 — Add concise repository instructions for Visual Studio Code compilation without running compilation.

## Acceptance criteria
- No active source depends on `C:/Users/...` paths.
- Personal data is provided through an ignored local configuration, with a non-sensitive example committed.
- All cover variants remain present and unchanged.
- Generated auxiliary files are not left as repository noise.
- PDF deliverables, images, and source files remain trackable.
- No compilation is executed by the implementation.

## Checks
- Structural readback of changed files.
- `git status --short` and `git check-ignore` for local configuration and generated files.
- No `pdflatex`, `latexmk`, or equivalent command.

## Route
Delegated direct writer. The change spans multiple non-trivial source/configuration files; no SDD workflow is selected.

## Progress
- Implemented repository-relative graphics resolution in the active report entry point and removed the prior absolute path.
- Added `config/datos.example.tex` and ignored `config/datos.local.tex`; active sources load the local file first and fall back to the example.
- Replaced practical personal-data literals in `plan.tex`, `parte1to4.tex`, `informe_Final_2025_I.tex`, `milibreria.sty`, and all four cover styles with configuration macros while preserving each cover design.
- Extended `.gitignore`, removed only `plan.aux`, `plan.log`, `plan.out`, and `plan.toc`, and added `README.md`.
- Structural evidence: the four cover files remain present; `plan.pdf`, source assets, and image files were not removed. `Logo_UNAP` and `Sistemaslogo` are absent and are documented as assets to supply or replace with an alternative cover.
