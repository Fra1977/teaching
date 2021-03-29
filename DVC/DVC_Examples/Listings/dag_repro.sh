 . ~/Envs/teaching/bin/activate
 
 # let us setup things
 
 mkdir 04
 cd 04
 wget https://code.dvc.org/get-started/code.zip
 unzip code.zip
 rm code.zip
 cp -r  ../04_pipelines/data .
 git init

 dvc init
 ls
 cat params.yaml 
 # run a stage
 dvc run -n prepare           -p prepare.seed,prepare.split           -d src/prepare.py -d data/data.xml           -o data/prepared           python src/prepare.py data/data.xml [A[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[Kl
 cat dvc.yaml
 dvc dag
 dvc dag -o
 # add another stage
 dvc run -n featurize           -p featurize.max_features,featurize.ngrams           -d src/featurization.py -d data/prepared           -o data/features           python src/featurization.py data/prepared data/features
 cat dvc.yaml
 cat dvc.yamldvc run -n featurize           -p featurize.max_features,featurize.ngrams           -d src/featurization.py -d data/prepared           -o data/features           python src/featurization.py data/prepared data/features[A[A# add another stage[K
  dvc dag --full -o
 # add another stage
 dvc run -n train           -p train.seed,train.n_est,train.min_split           -d src/train.py -d data/features           -o model.pkl           python src/train.py data/features model.pkl
 dvc dag
 
 dvc run -n evaluate           -d src/evaluate.py -d model.pkl -d data/features           -M scores.json           --plots-no-cache prc.json           --plots-no-cache roc.json           python src/evaluate.py model.pkl                  data/features scores.json prc.json roc.json
 git add dvc.yaml  dvc.lock 
 git commit m"FR: experiment01"
 git commit m"FR: experiment01"[1@-
 dvc dag --full
 dvc dag --full -o
 # dvc repro reproduces the run for a given set of stages
 dvc repro
 # dvc metrics can be used to keep track of ML metrics between experiments or branches
 dvc metrics show
 # let us modify one of the inputs 8 parameters)
 vi params.yaml 
 dvc repro
 git add dvc.lock 
 git commit -m"FR: experiment02"
 dvc metrics show
 vi params.yaml 
 dvc repro
 dvc metri[K[K[K[K[K[K[K[K[Kdvc reprovi params.yaml dvc metrics showgit commit -m"FR: experiment02"[14Padd dvc.lock 
 [C[14Preverse-i-search)`':[C[18@c': git add dvc.locko': git commit -m"FR: experiment02"[C[12@teaching) [raischel@andromeda 04]
 [C[14Preverse-i-search)`':[Cm': git commit -m"FR: experiment03"[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[1@e[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[14Pt': dvc metrics show[C[11@teaching) [raischel@andromeda 04]
 # so, now dvc repro runs again to adapt to the changed  stage
 # end
 exit
