.PHONE: all build rebuild clean

all: rebuild

build:
	pip install -e .
	pip install build
	python -m build --wheel
	pip install dist/tic_tac_toe-0.1.0-py3-none-any.whl

rebuild: clean build

clean:
	rm -rf build/ dist/ src/*.egg-info/ && pip uninstall tic_tac_toe -y

