from coxbuild.extensions.shell import existCommand
import platform
from coxbuild.schema import depend, group, named, postcond, precond, run, task

grouped = group("vim")


def installed():
    return bool(run(["vim", "--version"], fail=True, pipe=True))


@grouped
@precond(lambda: not installed())
@postcond(lambda: installed())
@task
def install():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "install", "vim.vim"])
    elif "darwin" in system:
        run(["brew", "install", "vim"])
    elif "linux" in system:
        run(["apt-get", "install", "vim"])


@grouped
@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "vim.vim"], fail=True)
    elif "darwin" in system:
        run(["brew", "upgrade", "vim"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "vim"])


@named("install")
@depend(install)
@task
def defaultInstall(): pass


@named("upgrade")
@depend(upgrade)
@task
def defaultUpgrade(): pass
