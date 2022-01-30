import platform
from coxbuild.extensions.shell import existCommand
from coxbuild.schema import task, precond, postcond, run, group, depend, named

grouped = group("vscode")


def installed():
    return bool(run(["code", "--version"], fail=True, pipe=True))


@grouped
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


@grouped
@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "Microsoft.VisualStudioCode"])
    elif "darwin" in system:
        run(["brew", "upgrade", "vscode"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "vscode"])


@named("install")
@depend(install)
@task
def defaultInstall(): pass


@named("upgrade")
@depend(upgrade)
@task
def defaultUpgrade(): pass