"""Format Python code."""

from coxbuild.extensions.python import format as pyformat
from coxbuild.schema import depend, ext, task

ext(pyformat)


@depend(pyformat.format)
@task
def default():
    pass
