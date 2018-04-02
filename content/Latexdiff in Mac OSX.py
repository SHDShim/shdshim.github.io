
# coding: utf-8

# __(Warning)__ The following procedure only worked with `Ubuntu` and Mac OSX.  
# 
# __(Warning)__ `Latexdiff` from MacTeX did not work with unknown reason.
# 
# To make error free, make sure you do this:
# 
# 1. Your old and new files must exist in separate folders.  Those separate folders must have all the necessary files, such as `*.aux`, `*.blb`, figure `pdf`s, etc. If you mix old and new files in the same folder, you will get a lot of errors.
# 
# 2. It is not absolutely necessary, but you may want to separately compile them to pdf's.
# 
# 3. You can now execute `latexdiff` through one of the followings.
# 
#   ```bash
#   latexdiff --flatten --disable-citation-markup  ./old/original.tex ./new/revised.tex > diff.tex
#   ```
# 
#   `--flatten` : this option is needed when you have `\include`, `\input`, or `\includegraphics`.
# 
#   `--subtype=“SAFE”` : this option does not seem to change anything
# 
#   `--disable-citation-markup` : this option make no tracking for citation.  OK option to avoid confusion because latexdiff does not distinguish new and old citations.
# 
# 4. Then finally `pdflatex FeOxBr_diff.tex`.
# 
# Only problem here is that this procedure does not take care of the citation changes.  But so far this is the best.
