#!/usr/bin/env python
# coding: utf-8

# TODO:
# 
# [] cretae venv with dvc==2
# 
# [] rehearse
# 
# [] add remote 
# 
# [] add pipeline part
#     
#     

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
#     - considerations: storage space, personal or anonymized data 
#   - How to create repeatable, deterministic and  reusable Data Science workflows
#     - think in DAGs 
#     - thnk about audience and security
#     - keep things agile, but at the same time prepare for substituting data
#     - Oss . Other solutions

# ## What is DVC?

# Basics  
# 
# - www.dvc.org , OSS, since 2019, high activity 
# - idea: use git for code versioning, and augment git for data versioning via md5sum
# - metadata of data objects is kept in dvc.yaml files which contain the data hash, and which is versioned in git 
# - this concept allows to mirror the most important  git funciontality (versioning, branches, remotes) for data 

#  
# <center><img src="files/Img/model-sharing-digram.png" alt="DVC" style="width: 100%;"/></center>

# ## What else is DVC?

# DAG
# 
#   - dvc also remembers the DAG (directed acyclic graph) of execution, linking all stages 
#   
#       data input - code - data output
#   
#   
#   - this concept allows to replicate the main  functionality of SAS EG, ariflow, luigi, and Data Science platforms such as alteryx, dataiku etc.  

#  
# 
# <center><img src="files/Img/dependency-graph.png" alt="JPG" style="width: 40%;"/></center>
# 

# <center><img src="files/Img/enterprise-guide_full.jpg" alt="JPG" style="width: 50%;"/></center>

# ### Install dvc

# - DVC is open source
# - install via pip ( or conda), preferably in a venv:
#     - . \<path_to_venv\>/bin/activate 
#     - pip install dvc

# In[15]:


HTML("""<script id="asciicast-pSItHG2FBqiS1oim9Eul9d1qM" src="https://asciinema.org/a/pSItHG2FBqiS1oim9Eul9d1qM.js" async %></script>""")


# ### setup  dvc

# - dvc copies most of the behaviour of git. Therefore, run:
#   - git init 
#   - dvc init 
# - dvc init creates a .dvc directory structure 
# - most importantly, the .dvc/cache contains copies of all files checked into dvc with  name==checksum

# In[16]:


HTML("""<script id="asciicast-w89eeSIK0O9RvUOIp2Aagj1Dz" src="https://asciinema.org/a/w89eeSIK0O9RvUOIp2Aagj1Dz.js" async></script>""")


# ### add files 

# - add a data file 
# - show data.dvc fiel 
# - verify checksum 

# In[18]:


HTML("""<script id="asciicast-w89eeSIK0O9RvUOIp2Aagj1Dz" src="https://asciinema.org/a/w89eeSIK0O9RvUOIp2Aagj1Dz.js" async></script>""")


# ### Adding files to   dvc

# - "dvc add" adds a file to dvc control and creates a .yaml metadata file
# - the .yaml file can be added to git 
# - the .yaml file identifies the data file through a checksum
# - dvc also creates a copy of the file in the local .dvc/cache

# In[17]:


HTML("""<script id="asciicast-T3SEPUjyFF68O87MN2Fk2DNVZ" src="https://asciinema.org/a/T3SEPUjyFF68O87MN2Fk2DNVZ.js" async></script>""")


# ### basic workflow

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

# In[10]:


HTML("""""")


# ###  the simplest pipeline

# - dvc copies most of the behaviour of git. Therefore, run:
#   - git init 
#   - dvc init 
# - dvc init creates a .dvc directory structure 
# - most importantly, the .dvc/cache contains copies of all files checked into dvc with  name==checksum

# In[19]:


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

# In[21]:


HTML("""<script id="asciicast-4O4aN6ftwXVE7OinigsE5sd6t" src="https://asciinema.org/a/4O4aN6ftwXVE7OinigsE5sd6t.js" async></script>""")


# ### Data remotes

# - just as git, dvc can have remotes:
#     - local dir
#     - remote dir (NFS/ssh)
#     - S3
# - just as git, you can use 
#     - dvc push 
#     - dvc pull 
# - remember to run dvc checkout

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





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:





# ### Install dvc

# In[ ]:





# In[ ]:




