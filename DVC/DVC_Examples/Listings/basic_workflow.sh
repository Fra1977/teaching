(teaching) [raischel@andromeda 01_setup]$ chmod u+x step01.sh 
]777;preexec\(teaching) [raischel@andromeda 01_setup]$ dvc run \
>   -d new-labels.zip \
>   -o wc01.txt \
>   -d step01.sh \
>   -n step01\
>   ./step01.sh

[0m(teaching) [raischel@andromeda 01_setup]$ ls
(teaching) [raischel@andromeda 01_setup]$ cat wc01.txt 
(teaching) [raischel@andromeda 01_setup]$ cat dvc.yaml 
(teaching) [raischel@andromeda 01_setup]$ cat dvc.lock 
(teaching) [raischel@andromeda 01_setup]$ git add dvc.lock dvc.yaml
]777;preexec\(teaching) [raischel@andromeda 01_setup]$ #end
(teaching) [raischel@andromeda 01_setup]$ exit
