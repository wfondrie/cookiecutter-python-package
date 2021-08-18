"""These tests are adapted from:
https://github.com/drivendata/cookiecutter-data-science
"""
import sys
import pytest
import shutil
from pathlib import Path
from cookiecutter import main

CCDS_ROOT = Path(__file__).parents[1].resolve()

args = {
    "package_name": "test-package",
    "author_name": "Will",
    "open_source_license": "GPLv3",
    "require_numpy": "no",
    "require_pandas": "no",
    "require_sklearn": "no",
    "require_numba": "no",
}

def system_check(basename):
    platform = sys.platform
    if "linux" in platform:
        basename = basename.lower()
    return basename


@pytest.fixture(scope="class", params=[{}, args])
def default_baked_project(tmpdir_factory, request):
    temp = tmpdir_factory.mktemp("cc-package")
    out_dir = Path(temp).resolve()

    pytest.param = request.param
    main.cookiecutter(
        str(CCDS_ROOT),
        no_input=True,
        extra_context=pytest.param,
        output_dir=out_dir,
    )

    pn = pytest.param.get("package_name") or "package_name"

    # project name gets converted to lower case on Linux but not Mac
    pn = system_check(pn)

    proj = out_dir / pn
    request.cls.path = proj
    yield

    # cleanup after
    shutil.rmtree(out_dir)
