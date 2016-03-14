from __future__ import with_statement
from fabric.api import *
from fabric.colors import *

#-- EDIT
remote_base_dir = ''  # edit remote base dir path
remote_err_file = ''  # edit path
remote_log_file = ''  # edit path

#-- EDIT
@hosts('')  # add remotes for deploy
def logs():
    puts(yellow("[Reading log-file]"))
    errout = run("cat %s"%remote_err_file)
    logout = run("cat %s"%remote_log_file)

#-- EDIT
@hosts('') # only for deploy
def deploy():
    module = 'bioinf-install'
    
    with settings(warn_only=True):
        if run("test -d %s/%s" %(remote_base_dir, module)).failed:
            puts(red("[Module does not exist: %s]"%module))
            with cd(remote_base_dir):
                run("git clone git@github.com:sschmeier/bioinf-install.git")
                run("git submodule init")  # initialise submodules
                
    puts(yellow("[Write logs]"))
    run("echo '-----------------------------' > %s"%remote_err_file)    
    run("echo `date` >> %s"%remote_err_file)
    run("echo '-----------------------------' >> %s"%remote_err_file)
    run("echo '-----------------------------' > %s"%remote_log_file)    
    run("echo `date` >> %s"%remote_log_file)
    run("echo '-----------------------------' >> %s"%remote_log_file)
                
    puts(yellow("[Update module: %s]"%module))
    with cd(remote_base_dir):
        run("git pull")
        run("git submodule update --remote --merge >> %s 2>> %s"%(remote_log_file, remote_err_file))

def deploy_local(dir='~/Dropbox/Public', repo='bioinf-install', name='bioinf-install'):
    with settings(warn_only=True):
        if local("test -d %s/%s" %(dir, name)).failed:
            puts(red("[Repo does not exist in %s/%s: %s]"%(dir, name, repo)))
            puts(yellow("[Cloning repo into %s/%s: %s]"%(dir, name, repo)))
            with lcd(dir):
                local('git clone git@github.com:sschmeier/%s.git %s'%(repo,name))
        else:
            puts(yellow("[Pulling newest changes into %s/%s: %s]"%(dir, name, repo)))
            with lcd(dir):
                local("git -C %s pull"%(name))                

def git_setup(dir='.', repo='bioinf-install', remote=False):
    # Setting up git repo
    with settings(warn_only=True):
        if local("test -d %s/.git" %(dir)).failed:
            puts(red("[Not a git repo]"))
            puts(yellow("[Initialise git.]"))
            local('git init')
            local('git add -f .gitignore; git commit -m "Init."')
            local('git co -b develop')
            if remote:
                local('git remote add origin git@github.com:sschmeier/%s.git'%(repo))
        else:
            puts(red("[Git repo already exists]"))
                
def git_mp(branch="develop", push=0, ghpages=0, version=None):
    # git merge push
    # branch: the branch that should be merged into master.

    with settings(warn_only=True):
        local("git add -u && git commit")

    local("git co master")
    local("git merge %s --no-ff" %branch)

    # add a new tag?
    if version:
        with settings(warn_only=True):
            local('git tag -a %s'%version)

    # push to origin?
    if push:
        with settings(warn_only=True):
            local("git push")

    # update gh-pages?
    if ghpages:
        with settings(warn_only=True):
            if not local("git co gh-pages").failed:
                with settings(warn_only=True):
                    local("git merge master")
                if push:
                    with settings(warn_only=True):
                        local("git push origin gh-pages")

    local("git co %s"%branch)

def git_update():
    with settings(warn_only=True):
        local("git pull")
    with settings(warn_only=True):
        local("git submodule update --remote --merge")
