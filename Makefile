TDIR = tests
VENV = venv

all: tests_run

$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	chmod +x $(VENV)/bin/activate
	./$(VENV)/bin/activate

$(VENV)/bin/pytest: $(VENV)/bin/activate
	$(VENV)/bin/pip install -r requirements.txt
	$(VENV)/bin/pip install -e .

tests_run: $(VENV)/bin/pytest
	$(VENV)/bin/pytest $(TDIR)

.PHONY: tests_run lint

clean:
	@ find . -type d -name __pycache__ -exec rm -rf {} +
	@ rm -rf .mypy_cache
	@ rm -rf .pytest_cache
	@ rm -rf src/*.egg-info

fclean: clean
	@ rm -rf $(VENV)

re: fclean all

.PHONY: clean fclean re
