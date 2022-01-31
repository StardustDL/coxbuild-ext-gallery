from coxbuild.schema import depend, ext, postcond, precond, run, task

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
def install():
    pass


@depend(dotnet.upgrade, python.upgrade, go.upgrade, pandoc.upgrade, pwsh.upgrade, rust.upgrade, vim.upgrade, vscode.upgrade, git.upgrade)
@task
def upgrade():
    pass
