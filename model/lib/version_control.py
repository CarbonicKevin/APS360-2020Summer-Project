import os

#list of usernames and corresponding working directories.
working_dir = {"nikoog"          : "/content/drive/My Drive/ENGSCI/Year 3/SUMMER 2020/APS360/",
               "CarbonicKevin"   : "/content/drive/My Drive/Colab Notebooks/APS360/",
               "DriftingCloudII" : "/content/drive/My Drive/Colab Notebooks/Project5/",
               "chanhyukyang"    : "/content/drive/My Drive/Colab Notebooks/"
               }

uEmails     = {"nikoog"          : "nikoo.givehchian@gmail.com",
               "CarbonicKevin"   : "kevinmj99@gmail.com"
               "DriftingCloudII" : "gerrychen117@gmail.com"
               "chanhyukyang"    : "chanhyukyang@hotmail.com"
               }


class git_commands:
  def __init__(self, uname, clone=True, repo_link="https://github.com/CarbonicKevin/APS360-2020Summer-Project.git"):
    self.email = uEmails[uname]
    self.uname = uname
    self.repo  = repo_link
    self.repo_name = repo_link.split('/')[-1][:-4]
    self.dir = working_dir[uname]
    print("setting ")
    %cd $self.dir

    !git config --global user.email $email --quiet
    !git config --global user.name $uname --quiet

    if clone: !git clone $self.repo

    self.branch = "master"

  def pull(self):
    dir = !pwd
    if dir[0] != self.dir:
      %cd $self.dir$self.repo_name
    !git pull

  def commit(self, commit_msg, add_files='all'):
    # add_files: string containing the filenames to be staged for commit, if not all changed files are going to be commited. <file1> <file2> ...
    if add_files == 'all':
      !git add -A
    else:
      !git add add_files

    if len(commit_msg) > 50:
      print("ERR: commit message too long.")
      return -1

    passwd = getpass()

    !git commit -m commit_msg
    !git remote add origin "https://{uname}:{passwd}github@github.com/{repo}.git"

    !git push -u origin $self.branch

    return 1

   def status(self):
     !git status

   def checkout(self, branch, isNew=False):
     if isNew:
        !git checkout -b $branch
     else:
        !git checkout $branch
     self.branch = branch

   def get_curr_branch(self):
     print(self.branch)

   def get_user_info(self):
     print("user: %s \nemail: %s \nworking directory: %s" 
                     % (self.uname, self.email, self.dir))

