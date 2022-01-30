from coxbuild.schema import task, precond, postcond, run

from coxbuild.extensions.shell import existCommand

import platform


def hasPython():
    return existCommand('python3') or existCommand('python')


@precond(lambda: not hasPython())
@postcond(lambda: hasPython())
@task
def install():
    system = platform.system().lower()
    if "windows" in system:
        run(["winget", "install", "Python.Python.3"])
    elif "darwin" in system:
        run(["brew", "install", "python3"])
    elif "linux" in system:
        run(["apt-get", "install", "python3"])
