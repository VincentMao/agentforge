.PHONY: train eval test lint typecheck check clean

# Train with default config
train:
	python src/train.py

# Train with a specific experiment config (EXP=baseline)
train-exp:
	python src/train.py experiment=$(EXP)

# Evaluate from a checkpoint
eval:
	python src/eval.py ckpt_path=$(CKPT)

# Run all tests with coverage
test:
	pytest tests/ --cov=src --cov-report=term-missing -v

# Lint and format
lint:
	ruff check src/ tests/ --fix
	ruff format src/ tests/

# Type check
typecheck:
	mypy src/ --strict

# Full quality check — run before committing
check: lint typecheck test

# Clean generated artifacts
clean:
	rm -rf logs/ outputs/ wandb/ .pytest_cache/ .mypy_cache/ .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
