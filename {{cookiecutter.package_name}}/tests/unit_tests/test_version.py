"""Test that setuptools-scm is working correctly"""
import {{ cookiecutter.import_name }}


def test_version():
    """Check that the version is not None"""
    assert {{ cookiecutter.import_name }}.__version__ is not None
