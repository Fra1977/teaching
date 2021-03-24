#!/usr/bin/env python
# coding: utf-8

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

# Some more data 

# In[ ]:


#![](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)


# In[ ]:


# Screencast test 


# In[1]:


from IPython.display import HTML
HTML("""<script src="https://asciinema.org/a/kwwq0tFCKpbRvIu9pAwHT4G2q"  async></script>""")


# <a href="https://asciinema.org/a/kwwq0tFCKpbRvIu9pAwHT4G2q" target="_blank"><img src="https://asciinema.org/a/kwwq0tFCKpbRvIu9pAwHT4G2q.svg" /></a>

# ### Embedded Player

# In[3]:


from IPython.display import HTML
HTML("""<script id="asciicast-kwwq0tFCKpbRvIu9pAwHT4G2q" src="https://asciinema.org/a/kwwq0tFCKpbRvIu9pAwHT4G2q.js" async></script>""")


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

# In[10]:


HTML("""<script id="asciicast-w89eeSIK0O9RvUOIp2Aagj1Dz" src="https://asciinema.org/a/w89eeSIK0O9RvUOIp2Aagj1Dz.js" async></script>""")


# ### Adding files to   dvc

# - dvc add adds a file to dvc control and creates a .yaml metadata file
# - the .yaml file can be added to git 
# - the .yaml file identifies the data file through a checksum

# In[11]:


HTML("""<script id="asciicast-w89eeSIK0O9RvUOIp2Aagj1Dz" src="https://asciinema.org/a/w89eeSIK0O9RvUOIp2Aagj1Dz.js" async></script>""")


# ### basic workflow
- run pipeline 
- show dvc.yaml file
# In[10]:


HTML("""<script id="asciicast-w89eeSIK0O9RvUOIp2Aagj1Dz" src="https://asciinema.org/a/w89eeSIK0O9RvUOIp2Aagj1Dz.js" async></script>""")


# ###  the simplest pipeline

# - dvc copies most of the behaviour of git. Therefore, run:
#   - git init 
#   - dvc init 
# - dvc init creates a .dvc directory structure 
# - most importantly, the .dvc/cache contains copies of all files checked into dvc with  name==checksum

# In[10]:


HTML("""<script id="asciicast-w89eeSIK0O9RvUOIp2Aagj1Dz" src="https://asciinema.org/a/w89eeSIK0O9RvUOIp2Aagj1Dz.js" async></script>""")


# ### tutorial: import data 
# 
# then: run pipeline, show md5sum
# then  branch, change  code , run new pipeline, show new md5sum
# then switch back to master, show md5sum before and after dvc checkout
# 

# - dvc copies most of the behaviour of git. Therefore, run:
#   - git init 
#   - dvc init 
# - dvc init creates a .dvc directory structure 
# - most importantly, the .dvc/cache contains copies of all files checked into dvc with  name==checksum

# In[10]:


HTML("""<script id="asciicast-w89eeSIK0O9RvUOIp2Aagj1Dz" src="https://asciinema.org/a/w89eeSIK0O9RvUOIp2Aagj1Dz.js" async></script>""")


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





# ### Install dvc

# In[ ]:





# In[ ]:




