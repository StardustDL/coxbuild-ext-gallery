import platform

from coxbuild.extensions.shell import existCommand
from coxbuild.schema import depend, group, named, postcond, precond, run, task


def installed():
    return bool(run(["git", "--version"], fail=True, pipe=True))


@precond(lambda: not installed())
@postcond(lambda: installed())
@task
def install():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "install", "Git.Git"])
    elif "darwin" in system:
        run(["brew", "install", "git"])
    elif "linux" in system:
        run(["apt-get", "install", "git"])


@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "Git.Git"], fail=True)
    elif "darwin" in system:
        run(["brew", "upgrade", "git"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "git"])
