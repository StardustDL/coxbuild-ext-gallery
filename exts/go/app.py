from coxbuild.schema import task, precond, postcond, run, group, named, depend

grouped = group("go")

from coxbuild.extensions.shell import existCommand

import platform


def installed():
    return bool(run(["go", "version"], fail=True, pipe=True))

@grouped
@precond(lambda: not installed())
@postcond(lambda: installed())
@task
def install():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "install", "GoLang.Go"])
    elif "darwin" in system:
        run(["brew", "install", "go"])
    elif "linux" in system:
        run(["apt-get", "install", "go"])

@grouped
@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "GoLang.Go"])
    elif "darwin" in system:
        run(["brew", "upgrade", "go"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "go"])

@named("install")
@depend(install)
@task
def defaultInstall(): pass


@named("upgrade")
@depend(upgrade)
@task
def defaultUpgrade(): pass
