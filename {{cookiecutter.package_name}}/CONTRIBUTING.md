# Contributing to {{ cookiecutter.package_name }}

First off, thank you for taking the time to contribute.

The following document provides guidelines for contributing to the
documentation and the code of {{ cookiecutter.package_name }}. **No
contribution is too small!** Even fixing a simple typo in the documentation is
immensely helpful.


## Contributing to the documentation

We use [mkdocs](https://www.mkdocs.org/) generate our documentation and deploy
it to this site. Most of the pages on the site are created from simple text
files written in markdown. There are three exceptions to this:

1. The API and command line documentation are automatically generated from the
   documentation contained in the code.

2. The Vignettes are created from Jupyter notebooks.

3. The Code of Conduct, Release Notes, and this Contributing document are 
   markdown files that live in the root of the {{ cookiecutter.package_name }} repository.


## Contributing to the code

We welcome contributions to the source code of {{ cookiecutter.package_name }}---particularly 
ones that address discussed [issues]({{ cookiecutter.issues_url }}).

Contributions to {{ cookiecutter.package_name }} follow a standard GitHub contribution workflow:

1. Create your own fork of the {{ cookiecutter.package_name }} repository on GitHub.

2. Clone your forked {{ cookiecutter.package_name }} repository to work on locally.

3. Create a new branch with a descriptive name for your changes:

```bash
git checkout -b fix_x
```

4. Make your changes (make sure to read below first).

5. Add, commit, and push your changes to your forked repository.

6. On the GitHub page for you forked repository, click "Pull request" to propose
   adding your changes to {{ cookiecutter.package_name }}.

7. We'll review, discuss, and help you make any revisions that are required. If
   all goes well, your changes will be added to {{ cookiecutter.package_name }}
   in the next release!


### Python code style

The {{ cookiecutter.package_name }} project follows the [PEP 8
guidelines](https://www.python.org/dev/peps/pep-0008/) for Python code style.
More specifically, we use [black](https://black.readthedocs.io/en/stable/) to
format code and lint Python code in {{ cookiecutter.package_name }}.

We highly recommend setting up a pre-commit hook for black. This will run black
on all of the Python source files before the changes can be committed. Because
we run black for code linting as part of our tests, setting up this hook can
save you from having to revise code formatting. Take the following steps to set
up the pre-commit hook:

1. Verify that black and pre-commit are installed. If not, you can install them
   with pip or conda:

```bash
# Using pip
pip install black pre-commit

# Using conda
conda -c conda-forge black pre-commit
```

2. Navigate to your local copy of the {{ cookiecutter.package_name }} repository and activate the hook:
```bash
pre-commit install
```

One the hook is installed, black will be run before any commit is made. If a
file is changed by black, then you need to `git add` the file again before
finished the commit.
