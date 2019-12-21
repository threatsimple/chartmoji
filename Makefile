VENV_DIR=pyvenv

DEFAULT=chartmoji

chartmoji: run

build: venv bin/create.py
	mkdir -p out/line out/bar
	pyvenv/bin/python3 bin/create.py

bin/create.py: venv

venv: $(VENV_DIR)/bin/activate
$(VENV_DIR)/bin/activate:
	python3 -m venv pyvenv
	pyvenv/bin/pip3 install -r reqs.pip

clean:
	rm -rf $(VENV_DIR) out __pycache__
