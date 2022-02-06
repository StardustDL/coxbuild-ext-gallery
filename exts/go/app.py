import platform

from coxbuild.extensions.shell import existCommand
from coxbuild.schema import depend, group, named, postcond, precond, run, task


def installed():
    return bool(run(["go", "version"], fail=True, pipe=True))


@precond(lambda: not installed())
@postcond(lambda: installed())
@task
def install():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "install", "GoLang.Go"])
    elif "darwin" in system:
        run(["brew", "install", "go"])
    elif "linux" in system:
        run(["apt-get", "install", "go"])


@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "GoLang.Go"], fail=True)
    elif "darwin" in system:
        run(["brew", "upgrade", "go"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "go"])
