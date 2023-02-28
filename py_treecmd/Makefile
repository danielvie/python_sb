target=gtree.py

all: r

b: build-exe

r: run

rg: run-git

test:
	python $(target) --test

run:
	python $(target)

run-git:
	git compare head~1 | python $(target)
	
build-exe:
	pyinstaller --onefile $(target)