from coxbuild.schema import task, precond, postcond, run, ext, depend

dotnet = ext("ext://dotnet/app")
python = ext("ext://python/app")
go = ext("ext://go/app")
pandoc = ext("ext://pandoc/app")
pwsh = ext("ext://pwsh/app")
rust = ext("ext://rust/app")
vim = ext("ext://vim/app")
vscode = ext("ext://vscode/app")
git = ext("ext://git/app")


@depend(dotnet.install, python.install, go.install, pandoc.install, pwsh.install, rust.install, vim.install, vscode.install, git.install)
@task
def default():
    pass
