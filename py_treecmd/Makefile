target=gtree.py

all: t

b: build-exe

r: run

t: test

i: install

rg: run-git

test:
	python $(target) --test

run:
	python $(target)

run-git:
	git compare head~1 | python $(target)
	
build-exe:
	pyinstaller --onefile $(target)
	
install:
	cp dist/gtree.exe C:/SANDBOX/APP/bin