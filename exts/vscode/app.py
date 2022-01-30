from coxbuild.schema import task, precond, postcond, run

from coxbuild.extensions.shell import existCommand

import platform


def installed():
    return bool(run(["code", "--version"], fail=True, pipe=True))


@precond(lambda: not installed())
@postcond(lambda: installed())
@task
def install():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "install", "Microsoft.VisualStudioCode"])
    elif "darwin" in system:
        run(["brew", "install", "vscode"])
    elif "linux" in system:
        run(["apt-get", "install", "vscode"])


@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "Microsoft.VisualStudioCode"])
    elif "darwin" in system:
        run(["brew", "upgrade", "vscode"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "vscode"])
