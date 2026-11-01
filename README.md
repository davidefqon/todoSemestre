# Informe final de prácticas

This repository contains the LaTeX sources and supporting assets for the practice plan and final report.

## Main entry points

- `plan.tex` — practice plan.
- `informe_Final_2025_I.tex` — final report; it includes the report sections and `plan.pdf` as a deliverable.

## Visual Studio Code workflow

Install the **LaTeX Workshop** extension, open this repository as the workspace, and open either entry point. Use the extension's **Build LaTeX project** command to compile from Visual Studio Code. Configure the extension's output directory as `build/` if generated files should stay outside the repository root.

Compilation is intentionally performed by Visual Studio Code rather than by repository scripts.

## Local data

The entry points load `config/datos.local.tex` when it exists and otherwise use the tracked, non-sensitive `config/datos.example.tex`. Copy the example to the local filename and edit the values for a local document. The local file is ignored by Git; this is source separation, not encryption or data protection.

## Cover styles and assets

The four files in `caratulas/` are preserved alternative cover styles. The report currently selects `caratulas/caratula4.tex`. That style still references the absent `Logo_UNAP` asset, and the shared report header names `Sistemaslogo` and `Logo_UNAP`; provide those assets or select a cover style that uses repository assets. Existing images under `images/` remain trackable and are used by the report where applicable.
