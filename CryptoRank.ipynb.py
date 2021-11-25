#!/usr/bin/env python
# coding: utf-8

# # 虛擬幣市值排行10

# In[81]:


import requests
from bs4 import BeautifulSoup
header = {
    'authority':'coinmarketcap.com',
    'method':'GET',
    'path':'/zh-tw/',
    'scheme':'https',
    'accept':'text/html',
    'accept-encoding':'gzip',
    'accept-language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control':'max-age=0',
    'cookie':'__cfduid=d86ed7dcbfcca1b80543922246419f7f41544784350; dcsrd=__5CLfVZWHMd0cEQ93AhFXdL; dcsrd.sig=LJe073xLsrKp7tCCypSXgRUbAQM; _ga=GA1.2.1361240220.1544784354; _gid=GA1.2.340690097.1544784354; _fbp=fb.1.1544784354452.2065822470; __auc=6ac4d46c167ac529c9b360ee315; __gads=ID=7a5fe5be7154b6ef:T=1544784360:S=ALNI_MYe66WBVzwryJAU19d34Klew9AR3g',
    'referer':'https://www.google.com.tw/',
    'upgrade-insecure-requests':'1',
    'user-agent':'Chrome/68.0.3440.84'
}
res = requests.get("https://coinmarketcap.com/zh-tw/currencies/bitcoin/",headers = header)
soup = BeautifulSoup(res.text,"html5lib")


# In[82]:


soup


# In[83]:


soup.select(".priceHeading___2GB9O")


# In[84]:


soup.select(".priceValue___11gHJ")


# In[86]:


soup.select(".priceTitle___1cXUG")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


for i in range(5):
    print('作者:',soup.select(".PostAuthor_root_3vAJfe")[i].text)
    print('Date:',soup.select(".PostEntry_published_229om7")[i].text)
    print('Title:',soup.select(".PostEntry_title_H5o4dj.PostEntry_unread_2U217-")[i].text)
    print('心情數:',soup.select(".PostEntry__LikeCount-sc-140l15m-0.hlvyVg")[i].text)
    print('回應數:',soup.select(".PostEntry_comments_2iY8V3")[i].text)
    print('簡單內文:',soup.select(".PostEntry_excerpt_2eHlNn")[i].text)
    print('--------------------------------------------------------------------------------')


# In[ ]:




