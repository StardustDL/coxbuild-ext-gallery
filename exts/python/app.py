import platform

from coxbuild.extensions.shell import existCommand
from coxbuild.schema import depend, group, named, postcond, precond, run, task


def installed():
    r = bool(run(["python", "--version"], fail=True, pipe=True))
    return r if r else bool(run(["python3", "--version"], fail=True, pipe=True))


@precond(lambda: not installed())
@postcond(lambda: installed())
@task
def install():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "install", "Python.Python.3"])
    elif "darwin" in system:
        run(["brew", "install", "python3"])
    elif "linux" in system:
        run(["apt-get", "install", "python3"])


@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "Python.Python.3"], fail=True)
    elif "darwin" in system:
        run(["brew", "upgrade", "python3"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "python3"])
