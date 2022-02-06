import platform

from coxbuild.extensions.shell import existCommand
from coxbuild.schema import depend, group, named, postcond, precond, run, task


def installed():
    return bool(run(["dotnet", "--version"], fail=True, pipe=True))


@precond(lambda: not installed())
@postcond(lambda: installed())
@task
def install():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "install", "Microsoft.dotnet"])
    elif "darwin" in system:
        run(["brew", "install", "dotnet"])
    elif "linux" in system:
        run(["apt-get", "install", "dotnet"])


@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "Microsoft.dotnet"], fail=True)
    elif "darwin" in system:
        run(["brew", "upgrade", "dotnet"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "dotnet"])
