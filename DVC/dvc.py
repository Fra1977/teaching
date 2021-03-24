#!/usr/bin/env python
# coding: utf-8

# # DVC - Repeatable Data Science

# # TOC
#   - What is DVC - a git for data Science - versioning of data 
#     - why we need it : CAG and determinism
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

# In[4]:


from IPython.display import HTML


# ## What is DVC?

# Some basics  
# 
#     - www.dvc.org , OSS, since 201x, high activity 
#     - idea: use git for code versioning, and augment git for data versioning via md5sum
#     - data is linked to dvc.yaml files which contains the data hash and is versioned in git 
#     - this concept allows to mirror the most important  git funciontality (versioning, branches, remotes) for data
#     - dvc also remembers the DAG (Directed acyclic graph) of execution, linking data input - code - data output in stages 
#     - this concept allows to replicate the main  functionality of SAS EG, ariflow, luigi, and Data Science platforms such as alteryx, dataiku etc.  

#  
# <center><img src="files/Img/model-sharing-digram.png" alt="DVC" style="width: 100%;"/></center>

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

# In[3]:


HTML("""<script id="asciicast-pSItHG2FBqiS1oim9Eul9d1qM" src="https://asciinema.org/a/pSItHG2FBqiS1oim9Eul9d1qM.js" async %></script>""")


# ### setup  dvc

# - dvc copies most of the behaviour of git. Therefore, run:
#   - git init 
#   - dvc init 
# - dvc init creates a .dvc directory structure 
# - most importantly, the .dvc/cache contains copies of all files checked into dvs whose name==checksum

# In[7]:


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




