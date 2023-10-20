# advanced testing techniques
This is a repo for doing testing

# Setup Project

1. Create a and source virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Create scaffold

```bash
touch Makefile && touch requirements.txt && touch hello.py && touch test_hello.py

```

3. Populate Makefile

```bash
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=hellocli test_hello.py

lint:
	pylint --disable=R,C hello.py hellocli.py

all: install lint test

```

### How to debug

* Print
* pdb
* testing
