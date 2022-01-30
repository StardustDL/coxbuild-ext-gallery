from coxbuild.schema import task, precond, postcond, run

from coxbuild.extensions.shell import existCommand

import platform


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
        run(["winget", "upgrade", "Microsoft.PowerShell"])
    elif "darwin" in system:
        run(["brew", "upgrade", "pwsh"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "pwsh"])
