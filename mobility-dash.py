#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import panel as pn
pn.extension('vega')


# In[1]:


get_ipython().run_line_magic('run', '../cleaning.ipynb')
get_ipython().run_line_magic('run', '../cleaning-jhu.ipynb')


# In[2]:


get_ipython().run_line_magic('run', 'panel-country.ipynb')


# In[3]:


get_ipython().run_line_magic('run', 'panel-county.ipynb')


# In[4]:


get_ipython().run_line_magic('run', 'panel-state.ipynb')


# In[5]:


get_ipython().run_line_magic('run', 'panel-state-comp.ipynb')


# In[6]:





# In[ ]:


dashboard = pn.Tabs(
    ("Country", pn.Column("## United States", "*Drag to select specific Apple data*", us_plot_set)),
    ("County", pn.Column("## County-level data", state_county_dash)),
    ("State", pn.Column("## State data", single_state_plots)),
    ("State Comparison", pn.Column("Compare states", state_comparison))
)

dashboard.servable()    


# In[ ]:




