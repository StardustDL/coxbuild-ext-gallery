from coxbuild.schema import task, precond, postcond, run

from coxbuild.extensions.shell import existCommand

import platform


def installed():
    return bool(run(["vim", "--version"], fail=True, pipe=True))


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


@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "vim.vim"])
    elif "darwin" in system:
        run(["brew", "upgrade", "vim"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "vim"])
