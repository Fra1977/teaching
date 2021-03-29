#####
. ~/Envs/teaching/bin/activate
git add step01.sh
git commit -m"FR: This was the first trial"
tail  dvc.lock
git checkout -b new_branch
tail  dvc.lock # unchanged
cat wc01.txt
ls
vi step01.sh
dvc run   -d new-labels.zip   -o wc01.txt   -d step01.sh   -n step01 --force   ./step01.sh
cat wc01.txt # changed
tail  dvc.lock # changed
md5sum wc01.txt  # bcs. this is a new file
t
git add -u
git commit -m"FR: 2nd version"
git checkout master # switch back to master
cat wc01.txt
tail dvc.lock
md5sum wc01.txt # not matching!
dvc checkout ### this is very importantant!
md5sum wc01.txt  # now it matches
cat wc01.txt
#end

