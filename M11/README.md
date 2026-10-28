# M11: Quarto website in RStudio

1. Open M11.Rproj in RStudio.
2. Run install.packages(c("foreign", "knitr", "rmarkdown")) once in the R Console.
3. Open dashboard.qmd to see the R analysis. Use Render, or run quarto render in the Terminal to build the whole website.

Edit index.qmd (home), dashboard.qmd, styling.qmd, and listings.qmd. The projects folder contains three small QMD entries used by the required Listings demonstration. styles.scss controls the appearance; _quarto.yml controls navigation.

_site is the automatically generated website, including its supporting files. You do not edit those files. No Python or separate analysis script is required.

The dashboard downloads the original course dataset into a temporary file when needed. Alternatively, put Case 31 Data_efcu_Prepped.sav beside dashboard.qmd. Raw respondent records are not republished in GitHub.

Before submitting, replace the photo placeholder in index.qmd with your headshot. Save it as headshot.jpg beside index.qmd and use ![Brahhmen](headshot.jpg){width=220}.

Published website: https://brahhmen55.github.io/IBM6500-/M11/_site/
Source: https://github.com/Brahhmen55/IBM6500-/tree/main/M11
Submit the rendered submission.html or the supplied standalone M11_Submission.html.
