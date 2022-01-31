import platform

from coxbuild.extensions.shell import existCommand
from coxbuild.schema import depend, group, named, postcond, precond, run, task

grouped = group("pwsh")


def installed():
    return bool(run(["pwsh", "--version"], fail=True, pipe=True))


@grouped
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


@grouped
@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "Microsoft.PowerShell"], fail=True)
    elif "darwin" in system:
        run(["brew", "upgrade", "pwsh"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "pwsh"])


@named("install")
@depend(install)
@task
def defaultInstall(): pass


@named("upgrade")
@depend(upgrade)
@task
def defaultUpgrade(): pass
