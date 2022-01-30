from pathlib import Path
from coxbuild.schema import task, precond, postcond, run, group, depend, named

grouped = group("rust")

from coxbuild.extensions.shell import existCommand

import platform
from urllib import request


def installed():
    return bool(run(["rustc", "--version"], fail=True, pipe=True))


@grouped
@precond(lambda: not installed())
@postcond(lambda: installed())
@task
def install():
    system = platform.system().lower()
    if "windows" in system:
        rustupinit = Path("./rustup-init.exe")
        with request.urlopen("https://win.rustup.rs/x86_64") as f:
            rustupinit.write_bytes(f.read())
        run([str(rustupinit)])
    elif "darwin" in system:
        run(["sh", "-c", "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"])
    elif "linux" in system:
        run(["sh", "-c", "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"])


@grouped
@task
def upgrade():
    run(["rustup", "update", "stable"])

@named("install")
@depend(install)
@task
def defaultInstall(): pass


@named("upgrade")
@depend(upgrade)
@task
def defaultUpgrade(): pass
