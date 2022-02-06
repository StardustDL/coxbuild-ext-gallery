import platform

from coxbuild.extensions.shell import existCommand
from coxbuild.schema import depend, group, named, postcond, precond, run, task


def installed():
    return bool(run(["pandoc", "--version"], fail=True, pipe=True))


@precond(lambda: not installed())
@postcond(lambda: installed())
@task
def install():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "install", "JohnMacFarlane.Pandoc"])
    elif "darwin" in system:
        run(["brew", "install", "pandoc"])
    elif "linux" in system:
        run(["apt-get", "install", "pandoc"])


@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "JohnMacFarlane.Pandoc"], fail=True)
    elif "darwin" in system:
        run(["brew", "upgrade", "pandoc"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "pandoc"])
