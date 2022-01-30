import os
from pathlib import Path

from coxbuild.extensions.python import format as pyformat
from coxbuild.schema import depend, ext, run, task

ext(pyformat)


@task
def list():
    for item in Path(os.getcwd()).glob('exts/**/*.py'):
        print(f"Testing: {item}")
        run(["cb", "-f", str(item), ":list"])


@task
def install():
    for item in Path(os.getcwd()).glob('exts/**/install.py'):
        print(f"Testing Install: {item}")
        run(["cb", "-f", str(item), "install"])


@depend(list, install)
@task
def default():
    pass


@depend(pyformat.format)
@task
def format():
    pass
