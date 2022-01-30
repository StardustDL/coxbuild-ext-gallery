from coxbuild.schema import task, precond, postcond, run, ext, depend

dotnet = ext("ext://dotnet/app").module
python = ext("ext://python/app").module
go = ext("ext://go/app").module
pandoc = ext("ext://pandoc/app").module
pwsh = ext("ext://pwsh/app").module
rust = ext("ext://rust/app").module
vim = ext("ext://vim/app").module
vscode = ext("ext://vscode/app").module
git = ext("ext://git/app").module


@depend(dotnet.install, python.install, go.install, pandoc.install, pwsh.install, rust.install, vim.install, vscode.install, git.install)
@task
def default():
    pass
