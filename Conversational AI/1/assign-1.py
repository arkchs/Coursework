#!/usr/bin/env python
# coding: utf-8

# In[7]:





# In[10]:





# In[10]:


headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'} 
cookies =   {'bcookie="v=2&26d76da1-31ff-49b2-8a80-7d24c33e4512"; li_sugr=41a6712a-5853-4939-b1de-89793b420faf; bscookie="v=1&20240408161105927e37aa-36db-4696-87f7-b6ebdd11b475AQGkgOsFXQxMJTfGGJb8B1VzsxrLC8GI"; li_rm=AQFs335vsPW2qwAAAY7E2mL32VOnG3W2yEvAhAA8DbvYvLnBa499hBPO2hb1yP9XdzOB3pNaTHUqtfyV-8SJzQJUBquK3dgprxU4B6j3XL3JJP-gpfcy5mil; _gcl_au=1.1.1863305466.1712699632; g_state={"i_l":0}; liap=true; JSESSIONID="ajax:5320624760842353457"; li_theme=light; li_theme_set=app; dfpfpt=2fd7b0209ee34db99bbae58f2d0b1adb; timezone=Asia/Calcutta; aam_uuid=27786487756113348632281033698695966263; _guid=b56529fb-5e92-4087-b4f0-00a161a1cb74; lms_ads=AQGnf9nYQIXPSQAAAZFwQ14VuwiTLL5oF4sudetKRkYP4c5E6jp_-ObsSt3VHhuA6QBmsonhUXSKMPTBLlbKtW_c5zWbGLiC; lms_analytics=AQGnf9nYQIXPSQAAAZFwQ14VuwiTLL5oF4sudetKRkYP4c5E6jp_-ObsSt3VHhuA6QBmsonhUXSKMPTBLlbKtW_c5zWbGLiC; AnalyticsSyncHistory=AQLLVS2-vH4L8QAAAZGUaI-XgVPTQ_TJSQp6QFkGAkKgVZeEf4IX4sj_8q9fdpaN44X6d8YspScoYzNUdG8OIQ; li_at=AQEDAT4O640DVxZeAAABj3a-gekAAAGRvGxr1lYAXnce0LYRPMDrsbrdllPmE6vrXlALtHeiXNc7Tk73U_CC9P3O_FSLgK9SNOc7FPplWWGmXulHdK7R9jl03jDBDi__tZJeB2yawdpJQkQZCgQiUc7D; fid=AQGbJAllxBa9qAAAAZGYiRC9u5D_HijXELnFg3ExgnXxjvTZTl8M7OUyNMU29NT4eZh3Bn3K197S3A; lang=v=2&lang=en-us; fptctx2=taBcrIH61PuCVH7eNCyH0MJojnuUODHcZ6x9WoxhgCnaQ9GdrpTC%252filuddN2J1zgqUbBsQLje8aV1Px8u0OIZ%252bj4ra5WrigYhWdgYiLc1Y4lo6WoMkNIkXYqe8ylNODZyrKvzy%252b1g%252fOFL2vd1Vf%252bunIUkP9%252fmMiH1K%252fJZExWwkF3AzjeD%252fdxcouxav5gKMt7nHCeYZ7XS2PU3ddjRz6QPy7BGhBqAI3HgXIvxVyYep%252bwruWi93i2K83FnSVnAhIjRgh%252bE8dQ%252fuvUHg5dPe1YdFg22hQmaTEmC3ccaMTHIDifudV4oZ75SjC2Z1Sr5Kk2tEqfdHYydcbqR4Tb1H%252fBGZErHmgCdFb58dRt%252bK1RPUQ%253d; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19964%7CMCMID%7C27563628578305277482263326187344698876%7CMCAAMLH-1725529559%7C12%7CMCAAMB-1725529559%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1724931959s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1835203406; UserMatchHistory=AQLuaeXQoaaqgAAAAZGdiBgIzddlyIpwmtA2OPffLKWRoxDVfSt7YRyUPiIqXSHoBHj-ly0hJjg6nSRZYa90VdK5Yl25pjhk7GOUFzQFJZ_GNI4Azw2YxMhG0mSs93MWAWuw9KbpX4XqEdLTzTDO_8sWmoc0s5sjj9dQfKcZdG-N1C2AhuS-IWZ0XwJuM81nArqprIStGbvqbAAgME7Ntx666X5sHJTmNGx4dEvPSq1-M68Kp6DcYdRTtc62-9cEdqM7pGzQX9sYzWhGGuuoMh-B4_silEambJEpG92L324huatK6S2vkDrjTDuLMPbeWdFOvteyjnHEiW1LeRULYJSO660sBeKdsjOlUz62AsDYCvRGMA; lidc="b=OB97:s=O:r=O:a=O:p=O:g=2879:u=399:x=1:i=1724924829:t=1724997916:v=2:sig=AQFjGvuEoBiTUi9FsZHX0j9w33FyJvuB"'}


# In[11]:


url = "https://www.linkedin.com/jobs/search?keywords="+mod_query+"&location="+mod_loc+"&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
req = requests.get(url)
print(url)
if(req.status_code==200):
    print('we can go ahead')
html_content = req.content
soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify)


# In[13]:


job_listings = soup.find_all('span',attrs ={'class':'sr-only'})
print(job_listings)

