#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Kütüphaneleri import edelim
import requests
from bs4 import BeautifulSoup


# In[3]:


headers_param = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"}
#web sitesinden veri çekme
glassdor = requests.get("https://www.glassdoor.com/List/Best-Jobs-in-America-2019-LST_KQ0,25.htm",headers=headers_param)


# In[4]:


print(glassdor.status_code)
#Bunun sonucunun 200 olması gerekir. Kodları çekebilmek için


# In[5]:


print(glassdor.content)
#web sitesindeki içerik ekrana gelecek.


# Web sitesinde bulunan content alındı şimdi onu parse etme işlemi yapılması gerekir. Ben meslek başlıklarını ve istatistiklerini çekeceğim.

# In[6]:


jobs = glassdor.content
#contenti jobs isminde değişkene atayalım. 
soup = BeautifulSoup(jobs,"html.parser")
#soup isminde obje tanımlayalım ve içeriğini parse edelim. 


# In[7]:


print(soup.title)


# In[10]:


all_jobs = soup.find_all("p",{"class":"h2 m-0 entryWinner pb-std pb-md-0"})
#p etiketi içerisin olan ve class":"h2 m-0 entryWinner pb-std pb-md-0" olan kısmını bul
for job in all_jobs:
    print(job.a.text)
#meslekleri almış olduk.


# In[11]:


all_data = soup.find_all("div",{"class":"col-6 col-lg-4 dataPoint"})

for data in all_data:
    print(data.text)
#verilerin istatistik bilgilerini almış olduk.


# In[ ]:




