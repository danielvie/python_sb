target=gtree.py

all: r

b: build-exe

r: run

rg: run-git

run:
	python $(target)

run-git:
	git compare head~1 | python $(target)
	
build-exe:
	pyinstaller --onefile $(target)