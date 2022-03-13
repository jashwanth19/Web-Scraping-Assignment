#!/usr/bin/env python
# coding: utf-8

# # Install packages

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install requests')
get_ipython().system('pip install bs4')


# # Imports

# In[87]:


import pandas as pd 
import requests
from bs4 import BeautifulSoup
import urllib.parse


# # HTTP Request
# 

# store website in variable

# In[3]:


website='https://www.flipkart.com/search?q=redmi+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=redmi+mobile%7CMobiles&requestId=8c64f91a-3aa6-4275-8f26-2eb18df45fb6&as-backfill=on&page=1'


# # Get Request

# In[4]:


response=requests.get(website)


# Status Code

# In[5]:


response.status_code


# # Soup Object

# In[6]:


soup=BeautifulSoup(response.content,'html.parser')


# In[ ]:


soup


# # Results

# In[39]:


results=soup.find_all('div',{'class':'_2kHMtA'})


# In[40]:


len(results)


# In[10]:


results[0]


# # Necessary Data

# In[11]:


#Name
#Price
#Rating 
#Review
#Product Link
#Product Details


# # Name

# In[67]:


results[0].find('div',{'class':'_4rR01T'}).get_text()


# # Price

# In[24]:


results[0].find('div',{'class':'_30jeq3 _1_WHN1'}).get_text()


# # Rating

# In[25]:


results[0].find('div',{'class':'_3LWZlK'}).get_text()


# # Rating and Review Counts

# In[30]:


results[0].find('span',{'class':'_2_R_DZ'}).get_text().replace('\xa0&\xa0','|')


# # Relative URL

# In[44]:


relative_url=results[0].find('a',{'class':'_1fQZEK'}).get('href')


# In[57]:


root_url='https://www.flipkart.com'


# In[58]:


url_combine=root_url+relative_url


# In[59]:


url_combine


# # Product Details

# In[63]:


results[0].find('ul',{'class':'_1xgFaf'}).get_text()


# # Put Everything Together inside for a loop

# In[83]:


product_name=[]
product_price=[]
rating=[]
rating_review_count=[]
relative_url=[]
product_details=[]




for result in results:
    try:
        product_name.append(result.find('div',{'class':'_4rR01T'}).get_text())
    except:
        product.name.append('n/a')
        
    #price
    try:
        product_price.append(result.find('div',{'class':'_30jeq3 _1_WHN1'}).get_text())
    except:
        product.price.append('n/a')
        
    #Rating
    try:
        rating.append(result.find('div',{'class':'_3LWZlK'}).get_text())
    except:
        rating.append('n/a')
        
    #Rating and Review Count
    try:
        rating_review_count.append(result.find('span',{'class':'_2_R_DZ'}).get_text().replace('\xa0&\xa0','|'))
    except:
        rating_review_count.append('n/a')
        
    #Relative Url
    try:
        relative_url.append(result.find('a',{'class':'_1fQZEK'}).get('href'))
    except:
        relative_url.append('n/a')
        
    #Product Details
    try:
        product_details.append(result.find('ul',{'class':'_1xgFaf'}).get_text())
    except:
        product_details.append('n/a')
        
        
        


# In[85]:


product_name


# In[77]:


product_price


# In[79]:


rating


# In[80]:


rating_review_count


# In[81]:


relative_url


# In[84]:


product_details


# # Combine URL's

# In[88]:


url_combined=[]

for link in relative_url:
    url_combined.append(urllib.parse.urljoin(root_url,link))
    


# In[89]:


url_combined


# # Create Pandas Dataframe

# In[92]:


product_overview=pd.DataFrame({'Name':product_name,'Price':product_price,'Rating':rating,'Rating & Review Count':rating_review_count,'Link':url_combined,'Details':product_details})


# In[93]:


product_overview


# # Output in EXCEL 

# In[95]:


product_overview.to_excel('single_page.xlsx',index=False)


# # 2. Pagination Scaping all Pages

# In[96]:


product_name=[]
product_price=[]
rating=[]
rating_review_count=[]
relative_url=[]
product_details=[]


for i in range(1,24):
    #website
    website='https://www.flipkart.com/search?q=redmi+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=redmi+mobile%7CMobiles&requestId=8c64f91a-3aa6-4275-8f26-2eb18df45fb6&as-backfill=on&page='+str(i)
    
    #requests
    response=requests.get(website)
    
    #soup
    soup=BeautifulSoup(response.content,'html.parser')
    
    #results
    results=soup.find_all('div',{'class':'_2kHMtA'})
    
    #loop through results
    for result in results:
        
        #product
        try:
            product_name.append(result.find('div',{'class':'_4rR01T'}).get_text())
        except:
            product.name.append('n/a')

        #price
        try:
            product_price.append(result.find('div',{'class':'_30jeq3 _1_WHN1'}).get_text())
        except:
            product.price.append('n/a')

        #Rating
        try:
            rating.append(result.find('div',{'class':'_3LWZlK'}).get_text())
        except:
            rating.append('n/a')

        #Rating and Review Count
        try:
            rating_review_count.append(result.find('span',{'class':'_2_R_DZ'}).get_text().replace('\xa0&\xa0','|'))
        except:
            rating_review_count.append('n/a')

        #Relative Url
        try:
            relative_url.append(result.find('a',{'class':'_1fQZEK'}).get('href'))
        except:
            relative_url.append('n/a')

        #Product Details
        try:
            product_details.append(result.find('ul',{'class':'_1xgFaf'}).get_text())
        except:
            product_details.append('n/a')

        
    
    


# In[97]:


url_combined=[]

for link in relative_url:
    url_combined.append(urllib.parse.urljoin(root_url,link))
    


# In[98]:


product_overview=pd.DataFrame({'Name':product_name,'Price':product_price,'Rating':rating,'Rating & Review Count':rating_review_count,'Link':url_combined,'Details':product_details})


# In[99]:


product_overview


# # All Pages to Excel

# In[100]:


product_overview.to_excel('All pages results.xlsx',index=False)


# # END
