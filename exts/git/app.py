from coxbuild.schema import task, precond, postcond, run, group, named, depend

grouped = group("git")

from coxbuild.extensions.shell import existCommand

import platform


def installed():
    return bool(run(["git", "--version"], fail=True, pipe=True))

@grouped
@precond(lambda: not installed())
@postcond(lambda: installed())
@task
def install():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "install", "Git.Git"])
    elif "darwin" in system:
        run(["brew", "install", "git"])
    elif "linux" in system:
        run(["apt-get", "install", "git"])

@grouped
@task
def upgrade():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "upgrade", "Git.Git"])
    elif "darwin" in system:
        run(["brew", "upgrade", "git"])
    elif "linux" in system:
        run(["apt-get", "upgrade", "git"])

@named("install")
@depend(install)
@task
def defaultInstall(): pass


@named("upgrade")
@depend(upgrade)
@task
def defaultUpgrade(): pass
