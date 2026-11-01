# Organización de carpetas — Fase 2

## Objective
Reorganize the LaTeX repository into clear sections, styles, assets, references, and annexes while preserving the four cover designs.

## Authorized scope
- Keep `caratulas/` as the home of the four alternative cover styles.
- Treat `plan.tex` as the first document under `anexos/`; future annexes will be added there.
- Do not compile the project.
- Do not perform content corrections from the academic-consistency phase yet.
- Do not add QA work.
- Do not delete deliverables or source assets.

## Target structure

```text
main/
├── informe.tex
├── plan.tex (not at root; located under anexos/)
├── config/
├── estilos/
├── secciones/
├── caratulas/
├── assets/imagenes/
├── assets/logos/
├── anexos/
└── referencias/
```

## Tasks

- [x] ORG-01 — Create the target folders without deleting source material.
- [x] ORG-02 — Rename the main entry point and move report sections using descriptive, ordered names.
- [x] ORG-03 — Move the shared style, bibliography, images, administrative PDFs, and `plan.tex` to their domains.
- [x] ORG-04 — Update all `input`, `include`, package, image, and README paths.
- [x] ORG-05 — Keep all four caratula variants and preserve their distinct visual content.
- [x] ORG-06 — Update `.gitignore`, README, and this task record with the new structure.

## Acceptance criteria
- `anexos/plan.tex` is the first annex source and future annexes have a clear home.
- The four cover files remain under `caratulas/`.
- No active source references the old root locations.
- No absolute Windows paths are introduced.
- PDFs, images, and source assets remain present.
- No compilation is executed.

## Checks
- Structural readback of all moved/renamed files.
- Search for old paths and stale entry-point names.
- `git status --short` and `git diff --check`.

## Route
Delegated direct writer; this is a multi-file path migration.

## Progress

- [x] ORG-01 — Created `secciones/`, `estilos/`, `referencias/`, `anexos/`, `assets/imagenes/`, and `assets/logos/` without deleting source assets.
- [x] ORG-02 — Renamed the root entry point to `informe.tex` and moved the report sections to ordered files under `secciones/`.
- [x] ORG-03 — Moved the shared style, bibliography, images, administrative PDFs, and annex sources to their target domains. `aceptacion.pdf` was copied into `anexos/` because the original file was locked by another process; the original remains present until that process releases it.
- [x] ORG-04 — Updated active input, package, image, PDF, configuration, and README paths. The annex source continues to use `config/datos.*.tex` from the repository-root working directory, and explicit image paths remain rooted at the repository.
- [x] ORG-05 — Preserved all four cover files under `caratulas/`; cover image paths were updated only where required by the asset move. `Logo_UNAP` and `Sistemaslogo` remain documented as missing assets under `assets/logos/`.
- [x] ORG-06 — Updated `.gitignore`, README, and this task record for the new structure.

## Acceptance evidence

- Structural tree readback confirms the new root entry point, section/style/reference/annex directories, all moved images, and all four cover files.
- Text search found no active references to the old root entry point, old section filenames, `milibreria.sty`, `images/`, or root-level administrative PDFs.
- `plan.pdf`, `carta.pdf`, and `aceptacion.pdf` remain present under `anexos/`; the locked original `aceptacion.pdf` also remains at the root pending safe release by its owning process.
- No compilation or academic-content correction was performed.
