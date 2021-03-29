asciinema rec -t "remotes"

. ~/Envs/teaching/bin/activate

cd 02_remote/

# init dvc and git
git init

dvc init

# make remotes
mkdir ../git_remote

cd ../git_remote

git init --bare

mkdir ../dvc_remote

# cd and copy files
cd ../02_remote/

cp ../01_setup/new-labels.zip .

cp ../01_setup/step01.sh .

cat step01.sh

# add the files
git add step01.sh
dvc add new-labels.zip
git add .gitignore new-labels.zip.dvc
git add step01.sh
git commit -m"FR: local commit"

# add origins
git remote add origin ../git_remote/
dvc remote add dvcorigin ../dvc_remote/

#push
git push --set-upstream origin master
dvc push  -r dvcorigin

# show dvc remote
cd ../
find dvc_remote/

# create a second workgin dir
mkdir wdir2
cd wdir2
git clone ../git_remote/
cd git_remote/

ls -al # no data files here !

# add dvc remote
dvc remote add -d dvcorigin ../../dvc_remote/

# now, get dvc files
dvc pull -r dvcorigin

dvc checkout

ls -al

# we have two linked data repositories!
# end



 5045  dvc push dvcorigin
 5046  cat .dvc/config
 5047  dvc push dvcorigin
 5048  dvc run   -d new-labels.zip   -o wc01.txt   -d step01.sh   -n step01 --force   ./step01.sh
 5049  git add .gitignore dvc.lock dvc.yaml
 5050  git commit -m"FR: with yaml"
 5051  git push
 5052  dvc push dvcorigin
 5053  dvc push
 5071  history





mkdir ../git_remote
cd ../git_remote
git init --bare
mkdir ../dvc_remote
cd ../02_remote
git init
dvc init
cp ../datafile .
echo 'wc datafile > wc01.txt' > step01.sh && chmod u+x step01.sh
dvc add  datafile
git add step01.sh
git commit -m"FR: data+code"
git remote add origin ../git_remote
dvc remote add dvcorigin ../dvc_remote
git push origin
dvc push dvcorigin
mkdir ../otherdir
cd ../otherdir
git clone ../git_remote
dvc init
dvc remote add dvcorigin ../dvc_remote
dvc pull
ls
dvc checkout
