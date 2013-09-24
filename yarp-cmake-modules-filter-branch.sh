#!/bin/sh

base_dir=`pwd`


# Create YARP CMake Modules repository
cd $base_dir
git clone github:robotology/yarp.git yarp-cmake-modules
cd yarp-cmake-modules
git remote remove origin
for tag in `git tag`; do
    git tag -d $tag;
done
git gc
git gc --aggressive
git prune

git filter-branch --tree-filter $base_dir/yarp-cmake-modules-move-files.py -- --all
git filter-branch -f --tree-filter $base_dir/yarp-cmake-modules-dos2unix.sh -- --all
git filter-branch -f --subdirectory-filter keep -- --all
git filter-branch -f --prune-empty -- --all

git gc
git gc --aggressive
git prune

git filter-branch -f --msg-filter 'sed -e "/^svn path=/d"' -- --all
git filter-branch -f --msg-filter 'sed -e "s/^\[CMake\] //"' -- --all
git filter-branch -f --msg-filter 'sed -e "/^Fixes /d"' -- --all
git filter-branch -f --msg-filter 'sed -e "/^Conflicts:/d"' -- --all
git filter-branch -f --msg-filter 'sed -e "/src\//d"' -- --all
git filter-branch -f --msg-filter 'sed -e "/scripts\//d"' -- --all
git filter-branch -f --msg-filter 'sed -e "/conf\//d"' -- --all
git filter-branch -f --msg-filter 'sed -e "/^\*\*\* empty log message \*\*\*/d"' -- --all
git filter-branch -f --msg-filter 'sed -e "/^no message/d"' -- --all

git checkout --orphan newroot
git rm -rf .
# then you apply the same steps
git commit --allow-empty -m 'Initial empty commit'
initial_commit=`git rev-parse HEAD`
git rebase --onto newroot --root master
git branch -d newroot

git gc
git gc --aggressive
git prune



# Create iCub CMake Modules repository
cd $base_dir
git clone --no-hardlinks file:///opt/iit/src/iCub icub-cmake-modules
cd icub-cmake-modules
git filter-branch --tree-filter $base_dir/icub-cmake-modules-move-files.py -- --all
git filter-branch -f --tree-filter $base_dir/yarp-cmake-modules/dos2unix -- --all
git filter-branch -f --subdirectory-filter keep -- --all

git gc
git gc --aggressive
git prune

git filter-branch -f --msg-filter 'sed -e "/^git-svn-id: /d"' -- --all

git gc
git gc --aggressive
git prune



# Create repo for merging
cd $base_dir
git clone --no-hardlinks --origin yarp-cmake-modules file://$base_dir/yarp-cmake-modules cmake-modules
cd $base_dir/cmake-modules
git remote add icub-cmake-modules file://$base_dir/icub-cmake-modules
git fetch --all
git checkout -b icub icub-cmake-modules/master
git rebase $initial_commit
git checkout master
git merge icub -m "Merge branch 'icub'"

git remote remove yarp-cmake-modules
git remote remove icub-cmake-modules
git remote add drdanz github:drdanz/yarp-cmake-modules.git

git branch -d icub

git gc
git gc --aggressive
git prune




git filter-branch -f --env-filter '
if [ "$GIT_AUTHOR_EMAIL" = "ddomenichelli@kde.org" ]; then
  export GIT_AUTHOR_EMAIL="daniele.domenichelli@iit.it";
  export GIT_COMMITTER_EMAIL="daniele.domenichelli@iit.it";
elif [ "$GIT_AUTHOR_EMAIL" = "reafrancesco@users.sourceforge.net" ]; then
  export GIT_AUTHOR_EMAIL="francesco.rea@iit.it";
  export GIT_COMMITTER_EMAIL="francesco.rea@iit.it";
elif [ "$GIT_AUTHOR_EMAIL" = "paul@robotrebuilt.com" ]; then
  export GIT_AUTHOR_EMAIL="paulfitz@alum.mit.edu";
  export GIT_COMMITTER_EMAIL="daniele.domenichelli@iit.it";
fi' -- --all


git update-ref -d refs/original/refs/heads/master

git reflog expire --expire=now --all
git gc --prune=now

git gc
git gc --aggressive
git prune

