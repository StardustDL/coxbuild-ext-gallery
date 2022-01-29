from pathlib import Path
from coxbuild.schema import task, run
import os


@task
def default():
    for item in Path(os.getcwd()).glob('**/*.py'):
        run(["cb", "-f", str(item), ":list"])
