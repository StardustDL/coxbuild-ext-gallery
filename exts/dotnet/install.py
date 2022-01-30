from coxbuild.schema import task, precond, postcond, run

from coxbuild.extensions.shell import existCommand

import platform


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
        run(["winget", "upgrade", "Microsoft.dotnet"])
    elif "darwin" in system:
        run(["brew", "upgrade", "dotnet"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "dotnet"])
