import platform
from pathlib import Path
from urllib import request

from coxbuild.extensions.shell import existCommand
from coxbuild.schema import depend, group, named, postcond, precond, run, task


def installed():
    return bool(run(["rustc", "--version"], fail=True, pipe=True))


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
