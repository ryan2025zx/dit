#!/bin/bash

# Set filename variable
filename="COMP90043-research-project-report"

# First compilation to generate auxiliary files
echo "Running first compilation to generate auxiliary files..."
xelatex -interaction=nonstopmode "${filename}.tex"

# Check if biber is needed for bibliography processing
if grep -q "\\printbibliography" "${filename}.tex" || grep -q "\\addbibresource" "${filename}.tex"; then
    echo "Running biber for references..."
    biber "${filename}"
fi

# Second compilation to update references and TOC
echo "Running second compilation..."
xelatex -interaction=nonstopmode "${filename}.tex"

# Check .log file for unresolved references to decide if third compilation is needed
if grep -q "Rerun to get cross-references right" "${filename}.log"; then
    echo "Running third compilation to finalize cross-references and TOC..."
    xelatex -interaction=nonstopmode "${filename}.tex"
fi

# Check if the last compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful."
else
    echo "Compilation failed."
    exit 1
fi

# Remove generated intermediate files, keep necessary files for debugging
rm -f "${filename}.aux" "${filename}.bbl" "${filename}.blg" "${filename}.bcf" "${filename}.log" "${filename}.out" "${filename}.toc" "${filename}.lof" "${filename}.lot" "${filename}.run.xml"

echo "Clean up complete."
