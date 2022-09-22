"""These tests are adapted from:
https://github.com/drivendata/cookiecutter-data-science
"""
import os
import sys
import pytest
from pathlib import Path
from importlib import metadata
from subprocess import check_output
from conftest import system_check
from contextlib import contextmanager


@contextmanager
def cwd(path):
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


def no_curlies(filepath):
    """Utility to make sure no curly braces appear in a file.
    That is, was Jinja able to render everything?
    """
    with open(filepath, "r") as f:
        data = f.read()

    template_strings = ["{{", "}}", "{%", "%}"]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


@pytest.mark.usefixtures("default_baked_project")
class TestCookieSetup(object):
    def check(self, arg):
        args = ["python", str(self.path.parent), "--" + str(arg)]
        with cwd(self.path):
            p = check_output(args).decode("ascii").strip()

        return p

    def test_project_name(self):
        package = self.path
        if pytest.param.get("package_name"):
            name = system_check("test-package")
            assert package.name == name
        else:
            assert package.name == "package_name"

    def test_author(self):
        return # Disabled
        p = self.check("author")
        if pytest.param.get("author_name"):
            assert p == "Will"
        else:
            assert p == "Your name (or your organization/company/team)"

    def test_readme(self):
        readme_path = self.path / "README.md"
        assert readme_path.exists()
        assert no_curlies(readme_path)
        if pytest.param.get("package_name"):
            with open(readme_path) as fin:
                assert "# test-package" == next(fin).strip()

    def test_license(self):
        license_path = self.path / "LICENSE"
        assert license_path.exists()
        assert no_curlies(license_path)

    def test_license_type(self):
        return # Disabled
        p = self.check("license")
        if pytest.param.get("license"):
            assert p == "GPLv3"
        else:
            assert p == "Apache 2.0"

    def test_folders(self):
        if pytest.param.get("package_name"):
            pkg_dir = "test_package"
        else:
            pkg_dir = "package_name"

        expected_dirs = [
            ".github",
            ".github/workflows",
            "docs",
            "tests",
            "tests/unit_tests",
            "tests/system_tests",
            pkg_dir,
        ]

        print(os.listdir(self.path))
        ignored_dirs = [str(self.path)]
        abs_expected_dirs = [str(self.path / d) for d in expected_dirs]
        abs_dirs, _, _ = list(zip(*os.walk(self.path)))
        assert len(set(abs_expected_dirs + ignored_dirs) - set(abs_dirs)) == 0
