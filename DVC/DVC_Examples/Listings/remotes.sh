
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
