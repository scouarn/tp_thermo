
SVG_FILES := $(wildcard figs/*.svg)
PDF_FILES := $(patsubst figs/%.svg, figs/%.pdf, $(SVG_FILES))

all: $(PDF_FILES)
	pdflatex -shell-escape main.tex
	evince main.pdf

$(PDF_FILES): figs/%.pdf : figs/%.svg
	inkscape $<  -o $@ --export-type=pdf
	#inkscape -D $<  -o $@ --export-latex

clean:
	-rm *.toc *.nav *.log *.snm *.out *.aux
	-rm figs/*.pdf_tex figs/*.pdf
