# Variablen
PYTHON = plot.py ../matplotlibrc ../header-matplotlib.tex
DATA = content/tables/txt/data.txt
TEXT = content/theorie.tex content/durchfuehrung.tex content/auswertung.tex content/diskussion.tex
TABLES = build/data.tex
PLOTS = build/plot.pdf

all vXXX: build/vXXX.pdf

# hier Python-Skripte:
$(TABLES) $(PLOTS): $(PYTHON) $(DATA) | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

# hier weitere Abhängigkeiten für build/vXXX.pdf deklarieren:
build/vXXX.pdf: $(TEXT) $(TABLES) $(PLOTS)

build/vXXX.pdf: | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	vXXX.tex

build:
	mkdir -p build

clean:
	rm -rf build

################## Creating Fake data for the example ##########################

$(DATA): create_data.py ../matplotlibrc ../header-matplotlib.tex | content/tables/txt
	python create_data.py

content/tables/txt:
	mkdir -p content/tables/txt

################################################################################

.PHONY: all vXXX clean
