from coxbuild.schema import task, precond, postcond, run, ext, depend

dotnet = ext("extcn://dotnet/app").module
python = ext("extcn://python/app").module
go = ext("extcn://go/app").module
pandoc = ext("extcn://pandoc/app").module
pwsh = ext("extcn://pwsh/app").module
rust = ext("extcn://rust/app").module
vim = ext("extcn://vim/app").module
vscode = ext("extcn://vscode/app").module
git = ext("extcn://git/app").module


@depend(dotnet.install, python.install, go.install, pandoc.install, pwsh.install, rust.install, vim.install, vscode.install, git.install)
@task
def install():
    pass


@depend(dotnet.upgrade, python.upgrade, go.upgrade, pandoc.upgrade, pwsh.upgrade, rust.upgrade, vim.upgrade, vscode.upgrade, git.upgrade)
@task
def upgrade():
    pass
