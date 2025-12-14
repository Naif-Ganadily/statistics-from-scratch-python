#!/usr/bin/env bash
set -euo pipefail

PKG="statsfs"

# Folders
mkdir -p \
  src/$PKG/{descriptive,probability,inference,models,utils} \
  tests/{descriptive,probability,inference,models,utils} \
  notebooks/data \
  scripts \
  docs

# Package init files
for f in \
  src/$PKG/__init__.py \
  src/$PKG/descriptive/__init__.py \
  src/$PKG/probability/__init__.py \
  src/$PKG/inference/__init__.py \
  src/$PKG/models/__init__.py \
  src/$PKG/utils/__init__.py
do
  [ -f "$f" ] || printf "" > "$f"
done

# Module files (placeholders)
for f in \
  src/$PKG/descriptive/central_tendency.py \
  src/$PKG/descriptive/dispersion.py \
  src/$PKG/descriptive/shape.py \
  src/$PKG/probability/distributions.py \
  src/$PKG/probability/sampling.py \
  src/$PKG/inference/hypothesis.py \
  src/$PKG/inference/intervals.py \
  src/$PKG/models/regression.py \
  src/$PKG/utils/validation.py
do
  [ -f "$f" ] || printf "# TODO\n" > "$f"
done

# Test placeholders
[ -f tests/conftest.py ] || printf "" > tests/conftest.py
for f in \
  tests/descriptive/test_central_tendency.py \
  tests/descriptive/test_dispersion.py \
  tests/descriptive/test_shape.py \
  tests/probability/test_distributions.py \
  tests/probability/test_sampling.py \
  tests/inference/test_hypothesis.py \
  tests/inference/test_intervals.py \
  tests/models/test_regression.py \
  tests/utils/test_validation.py
do
  [ -f "$f" ] || printf "# TODO\n" > "$f"
done

# Small placeholders
[ -f scripts/examples.py ] || printf "# TODO\n" > scripts/examples.py
[ -f docs/index.md ] || printf "# statsfs docs\n" > docs/index.md

echo "Scaffold created."