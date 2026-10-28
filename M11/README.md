# M11 Quarto Portfolio

Open `_site/index.html` for the rendered website or run `quarto preview` in this folder. The dashboard is a genuine Quarto dashboard; the other pages use the Quarto website format.

## Before submission

Replace the clearly marked photo panel in `index.qmd` with your own photo, for example `![Brahhmen](assets/headshot.jpg){width=220}`. Copy the image into assets, then run `quarto render`. Review the bio for accuracy. Do not submit the photo placeholder as a completed photo requirement.

## Reproduce

1. Install Quarto 1.8 or newer.
2. Run `quarto render` from M11. This uses the included SVG charts and needs no additional analysis packages.
3. To recalculate charts after changing the data, install Python packages with `python -m pip install -r requirements.txt`, then run `python scripts/rebuild.py`, followed by `quarto render`.

The original dataset is available from the professor’s public repository. Raw respondent files are not republished here. Download Case 31 Data_efcu_Prepped.sav from the source URL below into data/ before running the script. The Python script validates the employee composite, writes metrics.json, and regenerates the charts. The displayed dashboard narrative is written for this supplied dataset; review the numbers and text after changing data.

## Publish

The project is stored at M11 in the existing IBM6500- repository. With GitHub Pages serving main / (root), the rendered page is https://brahhmen55.github.io/IBM6500-/M11/_site/. If Pages uses a different source, select Settings > Pages > Deploy from a branch > main > /(root) and save. The folder has a .nojekyll marker at the repository root when published to preserve underscore directories. Check the website link before submitting.

Submit `_site/submission.html` and optionally `submission.qmd`. They contain the website and repository links required by the assignment.

## Sources

Case data: https://github.com/jaejungca/case31/blob/main/Case%2031%20Data_efcu_Prepped.sav
Quarto documentation: https://quarto.org/docs/
