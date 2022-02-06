import platform

from coxbuild.extensions.shell import existCommand
from coxbuild.schema import depend, group, named, postcond, precond, run, task


def installed():
    return bool(run(["pwsh", "--version"], fail=True, pipe=True))


@precond(lambda: not installed())
@postcond(lambda: installed())
@task
def install():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "install", "Microsoft.PowerShell"])
    elif "darwin" in system:
        run(["brew", "install", "pwsh"])
    elif "linux" in system:
        run(["apt-get", "install", "pwsh"])


@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "Microsoft.PowerShell"], fail=True)
    elif "darwin" in system:
        run(["brew", "upgrade", "pwsh"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "pwsh"])
