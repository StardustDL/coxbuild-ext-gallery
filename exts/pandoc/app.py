from coxbuild.schema import task, precond, postcond, run, group, named, depend

grouped = group("pandoc")

from coxbuild.extensions.shell import existCommand

import platform


def installed():
    return bool(run(["pandoc", "--version"], fail=True, pipe=True))

@grouped
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

@grouped
@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "JohnMacFarlane.Pandoc"])
    elif "darwin" in system:
        run(["brew", "upgrade", "pandoc"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "pandoc"])

@named("install")
@depend(install)
@task
def defaultInstall(): pass


@named("upgrade")
@depend(upgrade)
@task
def defaultUpgrade(): pass

