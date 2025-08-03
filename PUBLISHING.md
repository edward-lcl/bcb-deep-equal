# Publishing to PyPI

## Prerequisites

1. Create accounts:
   - PyPI: https://pypi.org/account/register/
   - TestPyPI: https://test.pypi.org/account/register/

2. Install build tools:
   ```bash
   pip install --upgrade build twine
   ```

## Building the Package

1. Clean previous builds:
   ```bash
   rm -rf dist/ build/ *.egg-info
   ```

2. Build the package:
   ```bash
   python -m build
   ```

   This creates:
   - `dist/bcb_deep_equal-0.1.0-py3-none-any.whl`
   - `dist/bcb_deep_equal-0.1.0.tar.gz`

## Testing on TestPyPI

1. Upload to TestPyPI:
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

2. Test installation:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple bcb-deep-equal
   ```

3. Verify it works:
   ```python
   from bcb_deep_equal import deep_equal
   assert deep_equal(0.1 + 0.2, 0.3)
   ```

## Publishing to PyPI

1. Upload to PyPI:
   ```bash
   python -m twine upload dist/*
   ```

2. Install from PyPI:
   ```bash
   pip install bcb-deep-equal
   ```

## Post-Publishing

1. Create a GitHub repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: BCB Deep Equal v0.1.0"
   git remote add origin https://github.com/aaron-sandoval/bcb-deep-equal.git
   git push -u origin main
   ```

2. Create a release on GitHub with the same version tag

3. Update the main project to use the PyPI package:
   - Update requirements.txt: `bcb-deep-equal>=0.1.0`
   - Replace local imports with: `from bcb_deep_equal import deep_equal`

## Version Updates

1. Update version in `pyproject.toml`
2. Update version in `src/bcb_deep_equal/__init__.py`
3. Add changelog entry
4. Rebuild and republish