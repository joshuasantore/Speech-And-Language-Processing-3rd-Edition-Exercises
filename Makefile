.PHONY: test lint clean # cov

test:
	pytest tests/

# cov:
#	 pytest --cov=src tests/

lint:
	flake8 src/ tests/

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .coverage .pytest_cache
