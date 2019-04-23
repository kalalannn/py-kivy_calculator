PYTHON=python
.PHONY=all pack run pack profile doc help test

all:
	( cd src && $(PYTHON) Calculator_tk.pyw )
pack: clean
	mkdir odevzdani
	(cd odevzdani && mkdir repo)
	(cd odevzdani && mkdir doc)
	(cd odevzdani && mkdir install)
	(robocopy mockup odevzdani/repo/mockup) ^& exit 0
	(robocopy plan odevzdani/repo/plan) ^& exit 0
	(robocopy profiling odevzdani/repo/profiling) ^& exit 0
	(robocopy src odevzdani/repo/src) ^& exit 0
	copy "debugging.png" "odevzdani/repo"
	copy ".gitignore" "odevzdani/repo"
	copy "debugging.png" "odevzdani/repo"
	copy "dokumentace.pdf" "odevzdani/repo"
	copy "hodnoceni.txt" "odevzdani/repo"
	copy "Makefile" "odevzdani/repo"
	copy "README.md" "odevzdani/repo"
	copy "skutecnost.txt" "odevzdani/repo"
run: all

profile:
	(cd src && echo 1 2 3 4 5 | $(PYTHON) profiling.py)
clean:
	type nul >> src/cprof
	(cd src && del cprof *.spec)
	if exist src/dist rmdir /s /q dist
	if exist src/build rmdir /s /q build
	if exist src\__pycache__ rmdir /s /q src\__pycache__ 

	if exist doc rmdir /s /q doc
	if exist odevzdani rmdir /s /q odevzdani
doc: 
	(cd src && doxygen)
	mv src/html doc
help:
	echo Je potreba mit nainstalovany interpret pythonu 3
test:
	( cd src && echo Neuspesne testy: && parse.py )
