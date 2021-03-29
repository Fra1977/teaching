 . ~/Envs/teaching/bin/activate
 which dvc

 dvc --help[K[K[K[Kversion

 git init

 dvc init
 ls -al

 dvc get https://github.com/iterative/dataset-registry tutorial/ver/new-labels.zip  # dvc has a download function
 ls
 dvc add new-labels.zip
 git add new-labels.zip.dvc .gitignore
 ls -al
 cat new-labels.zip.dvc
 md5sum new-labels.zip

 ll .dvc/cache/2e/aa473159443e75e6fb7b29e56c0787 

 ll .dvc/cache/2e/aa473159443e75e6fb7b29e56c0787 [C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[1P[1P[1@m[1@d[1@5[1@s[2@um

 # which is equal d[K[Kto the d[K.dvc checksum
 exit
