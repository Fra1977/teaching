#!/usr/bin/env python
# coding: utf-8

# TODO:
# 
# [] cretae venv with dvc==2
# 
# [] rehearse
# 
# [] share this git 
# 
# 
# [] add remote 
# 
# [] add pipeline part
# 
# [] show dag commmand
# 
# [] prepare local demos 
# 
# [] show creation of notebook
#     
# [] reproducible: dvc repro    

# In[14]:


from IPython.display import HTML


# # DVC - Repeatable Data Science

# # TOC
#   - What is DVC - a git for data Science - versioning of data 
#     - why we need it : DAG and determinism
#     - description of basic workflow: code in git, data in dvc, remotes.
#     - repeat: what git allows us to do 
#   - How to use - together with git ( basic workflow) 
#     - install dvc via pip in venv 
#     - initializing dvc
#     - basic workflow: add infile, train a model, add outfile 
#     - add more outputs: models 
#     - add metrics
#   - How to share data and models with team members
#     - branching with git and dvc 
#     - adding a remote: types 
#     - adding a local FS remote.
#   - Conclusion

# ## Deterministic Data Science

# - Principal features of Data Science;
#   - Experimental
#   - Result of experiments depends on code *and* data
# - Standard Code Vrsioning Systems (CVS) cannot handle data - simply because of size

# 
# <center><img src="files/Img/Rosenblattperceptron.png" alt="DVC" style="width: 100%;"/></center>
# 
# [src: https://nl.wikipedia.org/wiki/Perceptron]

# Data science is an inter-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data
#     
#     [https://en.wikipedia.org/wiki/Data_science]

# ## What is DVC?

# Basics  
# 
# - http://dvc.org , OSS, since 2019, high activity 
# - idea: use git for code versioning, and augment git for data versioning via md5sum
# - metadata of data objects is kept in ascii text files which contain the data hash, and which are versioned in git 
# - this concept allows to mirror the most important  git funciontality (versioning, branches, remotes) for data 

#  
# <center><img src="files/Img/model-sharing-digram.png" alt="DVC" style="width: 100%;"/></center>
# 
# [src: http://dvc.org]

# ## What else is DVC?

# DAG
# 
#   - dvc also remembers the DAG (directed acyclic graph) of execution, linking all stages 
#   
#       data input - code - data output
#   
#   
#   - this concept allows to replicate a principal   functionality of SAS EG, Airflow, Luigi, and Data Science platforms such as Alteryx, Dataiku etc.  

#  
# 
# <center><img src="files/Img/dependency-graph.png" alt="JPG" style="width: 40%;"/></center>
# 
# [src: https://dvc.org/blog/r-code-and-reproducible-model-development-with-dvc]

# <center><img src="files/Img/enterprise-guide_full.jpg" alt="JPG" style="width: 50%;"/></center>
# 
# [src: https://www.analyticsvidhya.com/blog/2013/07/productivity-boosting-tips-sas-enterprise-guide/]

# ### Install dvc

# - DVC is open source
# - install via pip ( or conda), preferably in a venv:
#     - . \<path_to_venv\>/bin/activate 
#     - pip install dvc

# In[34]:


HTML("""<script id="asciicast-pSItHG2FBqiS1oim9Eul9d1qM" src="https://asciinema.org/a/pSItHG2FBqiS1oim9Eul9d1qM.js" async %></script>""")


# ### setup  dvc

# - dvc copies most of the behaviour of git. 
# - Therefore, run:
#   - git init 
#   - dvc init 
# - dvc init creates a .dvc directory structure 
# - most importantly, the .dvc/cache contains copies of all files checked into dvc with  name==checksum

# In[33]:


HTML("""<script id="asciicast-w89eeSIK0O9RvUOIp2Aagj1Dz" src="https://asciinema.org/a/w89eeSIK0O9RvUOIp2Aagj1Dz.js" async></script>""")


# ### Adding files to   dvc

# - "dvc add" adds a file to dvc control and creates a .dvc metadata file
# - the .dvc file can be added to git 
# - the .dvc file identifies the data file through a checksum
# - dvc also creates a copy of the file in the local .dvc/cache

# In[35]:


HTML("""<script id="asciicast-T3SEPUjyFF68O87MN2Fk2DNVZ" src="https://asciinema.org/a/T3SEPUjyFF68O87MN2Fk2DNVZ.js" async></script>""")


# ### Basic Workflow

# - let us run a basic pipeline with dvc run
# - pipeline is a sequence of processing stages on data 
# - again, this  means a DAG of 
#   
#       input data - processing - output data
#   
# - structure: "dvc run" -d \<input data files\> -o \<output data files \> -n \<name\> \<cmd \>
# 
#         dvc run \
#           -d new-labels.zip \
#           -o checksum.txt \
#           -d step01.sh \
#           -n step01\
#           ./step01.sh
# 
# 
# - The  dvc.yaml file contains the DAG
# - The dvc.lock file now contains the checksums

# In[37]:


HTML("""<script id="asciicast-hK33qkfoafLk2Nm0SpLfqIY49" src="https://asciinema.org/a/hK33qkfoafLk2Nm0SpLfqIY49.js" async></script>""")


# ### data branching

# ### data  branching
# 
# - since we keep all metadata in git, we can use branching or tagging
# - when we change branches, git will automatically checkout the code files and the dvc.yaml/dvc.lock files
# -  however, we must manually run a dvc checkout to switch also the data files (they are in the cache) 
# - always run : 
# 
#         git checkout
#         dvc checkout

# In[38]:


HTML("""<script id="asciicast-4O4aN6ftwXVE7OinigsE5sd6t" src="https://asciinema.org/a/4O4aN6ftwXVE7OinigsE5sd6t.js" async></script>""")


# ### Data remotes

# - just as git, dvc can have remotes:
#     - local dir
#     - remote dir (NFS/ssh)
#     - S3/Azure/Google Drive
# - just as git, you can use 
#     - dvc push 
#     - dvc pull 
# - remember to run dvc checkout
#   
# <div class="alert alert-block alert-warning"><b>the workflow shown is a bit more complex, but universal:</b>
# 
#   - setup local git and dvc 
#   - setup remote git and dvc 
#   - push to remotes 
#   - create second workingdir as git clone
#   - setup code and data connections 
# 
# </div>  
#   
# 

# In[39]:


HTML("""<script id="asciicast-P8o728hJc5uXA6BiG2Kinqc3x" src="https://asciinema.org/a/P8o728hJc5uXA6BiG2Kinqc3x.js" async></script>""")


# ### Meaning of Data Remotes

# <div class="alert alert-block alert-info"><b>Data remotes allow to:</b> 
#     
#   - copy  code and data  between working dirs  and remote
#   - sync code and data between working dirs 
#   - create  branches 
#   - have a complete data science shared workflow 
#     
# </div> 
# 

# 
# <center><img src="files/Img/centralized_workflow.png" alt="JPG" style="width: 85%;"/></center>
# 
# 
# [src: https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows]

# ### Conclusion

# How to create deterministic and reusable Data Science workflows:
# 
#   - Your experiments are only reproducible and deterministic if you control data provenance.
#     - Use dvc to track input data, output data, models and metrics
#     - Become used to git and dvc workflows
#     - Establish fixed remotes 
#     - Keep methods agile and simple, but at the same time prepare for substituting data  
#  - Think in DAGs 
#     - dvc repro allows to exactly reproduce DAGs
#     - Branches allow to test and switch between models, track metrics, and to "undo"
#   - Colaborate and deploy
#     - Branches and remotes enable colaborative workflows
#     - Remotes also enable mlops
#     - Think about audience and security
#     - Other considerations: storage space, personal or anonymized data    
#   - Other solutions: mlflow, git-lfs, ...
#   - This presentation:
# https://github.com/Fra1977/teaching

# 
# 
# <center><img src="files/Img/graphic.png" alt="JPG" style="width: 85%;"/></center>
# 
# [src: http://dvc.org]

# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:




