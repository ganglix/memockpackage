# mock-modules

`mock-modules` is a Python package designed for demonstration purposes to showcase a directory structure and packaging approach. It provides a collection of mock modules with no functional implementation.

Please note that this package is intended for learning and demonstration purposes only and should not be used in production environments.

## Installation

You can install `mock-modules` using pip:

pip install mock-modules


## Usage
As mock-modules is a mock package, it does not provide any usable functionality. However, it serves as an example of organizing a Python package structure and can be used as a reference for creating your own packages.

Directory Structure
The project directory has the following structure:
```bash
memockpackage/
 ├── mock_modules/
 │   ├── __init__.py
 │   ├── module1.py
 │   └── module2.py
 ├── tests/
 │   ├── test_module1.py
 │   └── test_module2.py
 ├── docs/
 ├── README.md
 ├── LICENSE
 └── pyproject.toml
 ```

Notes about path in development mode: 

Development Mode (a.k.a. “Editable Installs”)

When creating a Python project, developers usually want to implement and test changes iteratively, before cutting a release and preparing a distribution archive.

In normal circumstances this can be quite cumbersome and require the developers to manipulate the PYTHONPATH environment variable or to continuously re-build and re-install the project.

You can enter this “development mode” by performing an editable installation inside of a virtual environment, using pip’s -e/--editable flag, as shown below:

$ cd your-python-project
$ python -m venv .venv  # or use conda virtual environment
# Activate your environment with:
#      `source .venv/bin/activate` on Unix/macOS
# or   `.venv\Scripts\activate` on Windows

$ pip install --editable .

# Now you have access to your package
# as if it was installed in .venv
$ python -c "import your_python_project"


read more: https://setuptools.pypa.io/en/latest/userguide/development_mode.html


Notes on __init__.py:
with an empty __init__.py, submodules (module1, module2) are not imported when you import mock_modules
to import module1
import mock_modules.module1 as m1



Notes on development-packaging procedure:
1 draft source code with import module (may use base environment without changing it)
2 debug and revise with import package.module + added path
3 remove added path and add pyproject.toml
3.5 must use virtual environment if not done earlier
4 $ pip install --editable .
5 revise
7 uninstall (optional)
6 build and publish