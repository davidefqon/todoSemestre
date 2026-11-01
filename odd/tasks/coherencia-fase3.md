# Coherencia de contenido — Fase 3

## Objective
Make small, factual adjustments to dates, duration, workflow description, terminology, and conclusions without changing the report's overall content or cover designs.

## Authorized scope
- Practice period: four months, from 15/04/2025 through 15/08/2025.
- Describe the actual workflow as iterative and incremental: design each functionality, present it to the office supervisor, implement it, and adjust from feedback.
- Explain that the workflow is compatible with practices associated with Scrum and XP without claiming a formal framework was fully adopted.
- Preserve the existing activities, evidence, and overall narrative.
- Do not compile.
- Do not add QA work.

## Tasks

- [x] CON-01 — Update the practice period to four months and align activity dates/durations within that period.
- [x] CON-02 — Replace the abrupt methodology claims with a faithful iterative workflow explanation.
- [x] CON-03 — Correct small terminology and consistency issues in requirements, activities, and conclusions.
- [x] CON-04 — Align conclusions with the stated 100%, 90%, and 40% progress values.
- [x] CON-05 — Structurally verify that old dates and contradictory methodology wording are gone, without compiling.

## Checks
- Search for obsolete dates, three-month duration, and contradictory methodology claims.
- Read back changed sections.
- `git diff --check`.
- No `pdflatex`, `latexmk`, or equivalent.

## Route
Delegated direct writer; the correction spans multiple report sections and the annex.

## Progress
- Implemented in `config/datos.local.tex`, `informe.tex`, `secciones/01-contexto-institucional.tex`, `secciones/02-requerimientos.tex`, and `anexos/plan.tex`.
- Structural searches found no obsolete activity dates, three-month duration, September work, or contradictory formal-methodology claims.
- Read back all changed files and ran `git diff --check`; no compilation or QA work was performed.
