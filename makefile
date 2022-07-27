PYMAIN=src/main.py
PYINT=python
PYREQ=requirements.txt

OUTFILE=gfc.exe
OUTDIR=bin

CFLAGS=--standalone --onefile --remove-output
BINSETTINGS=--windows-company-name="Oliver Karger" --windows-product-name="GitLabFeatureCheck" --windows-file-version=1.0.0 --windows-product-version=0.5.0

install:
	choco install dependencywalker
	$(PYINT) -m pip install -r $(PYREQ)

run:
	python $(PYMAIN) ./config.local

compile:
	-mkdir $(OUTDIR)
	$(PYINT) -m nuitka $(CFLAGS) $(BINSETTINGS) --output-dir=$(OUTDIR) -o $(OUTFILE) $(PYMAIN)

clean:
	-rmdir /s /q $(OUTDIR)
	-del /s /q $(OUTFILE)