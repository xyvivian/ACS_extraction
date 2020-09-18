#!/usr/bin/env python
# coding: utf-8

# In[1]:


import censusdata
import pandas as pd


# In[2]:


pd.set_option('display.expand_frame_repr',False)
pd.set_option('display.precision' ,2)


# In[3]:


#From the observations above, all county codes are:
county_list = ['091','123','133','031','007','009','019','067','069','089','103','105','111','043','051','061','063','099','109','117',
'086','005','035','037','047','077','119','039','059','071','083','021','095','101','055','121','027','013','023','029',
'107','125','081','075','003','127','073','079','033','053','129','057','045','097','131','065','049','093','041','001',
'015','085','115','017','113','011','087']


# In[4]:


#download the census data for percentage of age
age_sex_data = censusdata.download('acs5', 2018,
           censusdata.censusgeo([('state', '12'),
                                 ('county', '091'),
                                 ('block group', '*')]),['B01001_006E','B01001_007E',
                                                         'B01001_008E','B01001_009E',
                                                         'B01001_010E','B01001_011E',
                                                         'B01001_012E','B01001_013E',
                                                        'B01001_014E','B01001_015E',
                                                        'B01001_016E','B01001_017E',
                                                        'B01001_018E','B01001_019E',
                                                        'B01001_020E','B01001_021E',
                                                        'B01001_022E','B01001_023E',
                                                        'B01001_024E','B01001_025E',
                                                        'B01001_030E','B01001_031E',
                                                         'B01001_032E','B01001_033E',
                                                         'B01001_034E','B01001_035E',
                                                         'B01001_036E','B01001_037E',
                                                        'B01001_038E','B01001_039E',
                                                        'B01001_040E','B01001_041E',
                                                        'B01001_042E','B01001_043E',
                                                        'B01001_044E','B01001_045E',
                                                        'B01001_046E','B01001_047E',
                                                        'B01001_048E','B01001_049E'])


# In[5]:


for i in county_list[1:]:
    age_sex_data_new = censusdata.download('acs5', 2018,
           censusdata.censusgeo([('state', '12'),
                                 ('county', i),
                                 ('block group', '*')]),['B01001_006E','B01001_007E',
                                                         'B01001_008E','B01001_009E',
                                                         'B01001_010E','B01001_011E',
                                                         'B01001_012E','B01001_013E',
                                                        'B01001_014E','B01001_015E',
                                                        'B01001_016E','B01001_017E',
                                                        'B01001_018E','B01001_019E',
                                                        'B01001_020E','B01001_021E',
                                                        'B01001_022E','B01001_023E',
                                                        'B01001_024E','B01001_025E',
                                                        'B01001_030E','B01001_031E',
                                                         'B01001_032E','B01001_033E',
                                                         'B01001_034E','B01001_035E',
                                                         'B01001_036E','B01001_037E',
                                                        'B01001_038E','B01001_039E',
                                                        'B01001_040E','B01001_041E',
                                                        'B01001_042E','B01001_043E',
                                                        'B01001_044E','B01001_045E',
                                                        'B01001_046E','B01001_047E',
                                                        'B01001_048E','B01001_049E'])
    age_sex_data = age_sex_data.append(age_sex_data_new)


# In[ ]:


#here I divide the data into several categories
#20-30, 30-45, 45-60, 60+, because we do not need too much details about sex and age
age_sex_data['Age: 20-30'] = (age_sex_data.B01001_006E + age_sex_data.B01001_007E + age_sex_data.B01001_008E
                             +age_sex_data.B01001_009E + age_sex_data.B01001_010E  +age_sex_data.B01001_011E
                             + age_sex_data.B01001_030E + age_sex_data.B01001_031E + age_sex_data.B01001_032E
                             +age_sex_data.B01001_033E + age_sex_data.B01001_034E  +age_sex_data.B01001_035E)

age_sex_data['Age: 30-45'] = (age_sex_data.B01001_012E + age_sex_data.B01001_013E + age_sex_data.B01001_014E
                             +age_sex_data.B01001_036E + age_sex_data.B01001_037E  +age_sex_data.B01001_038E)

age_sex_data['Age: 45-60'] = (age_sex_data.B01001_015E + age_sex_data.B01001_016E + age_sex_data.B01001_017E
                             +age_sex_data.B01001_039E + age_sex_data.B01001_040E  +age_sex_data.B01001_041E)

age_sex_data['Age: 60+'] = (age_sex_data.B01001_018E + age_sex_data.B01001_019E + age_sex_data.B01001_020E
                             +age_sex_data.B01001_021E + age_sex_data.B01001_022E  +age_sex_data.B01001_023E
                           + age_sex_data.B01001_024E  +age_sex_data.B01001_025E
                             + age_sex_data.B01001_042E + age_sex_data.B01001_043E + age_sex_data.B01001_044E
                             +age_sex_data.B01001_045E + age_sex_data.B01001_046E  +age_sex_data.B01001_047E
                           + age_sex_data.B01001_048E  +age_sex_data.B01001_049E)


# In[ ]:


age_data = age_sex_data[['Age: 20-30','Age: 30-45','Age: 45-60',"Age: 60+"]]


# In[ ]:


race_data = censusdata.download('acs5', 2018,
           censusdata.censusgeo([('state', '12'),
                                 ('county', '091'),
                                 ('block group', '*')]),['B02001_002E','B02001_003E','B02001_004E','B02001_005E',
                                                         'B02001_006E'])


# In[ ]:


for i in county_list[1:]:
    race_data_new = censusdata.download('acs5', 2018,
            censusdata.censusgeo([('state', '12'),
                                 ('county', i),
                                 ('block group', '*')]),['B02001_002E','B02001_003E','B02001_004E','B02001_005E',
                                                         'B02001_006E'])
    race_data = race_data.append(race_data_new)


# In[ ]:


race_data["Race: White"] = race_data.B02001_002E
race_data["Race: Black/African American"] = race_data.B02001_003E
race_data["Race: American Indian and Alaska Native"] = race_data.B02001_004E
race_data["Race: Asian"] = race_data.B02001_005E
race_data["Race: Hawaiian and Pacific Islander"] = race_data.B02001_006E
race_data= race_data[["Race: White","Race: Black/African American","Race: American Indian and Alaska Native",
                      "Race: Asian","Race: Hawaiian and Pacific Islander"]]


# In[ ]:


education_data = censusdata.download('acs5', 2018,
           censusdata.censusgeo([('state', '12'),
                                 ('county', '091'),
                                 ('block group', '*')]),['B29002_002E','B29002_003E','B29002_004E','B29002_005E',
                                                         'B29002_006E','B29002_007E','B29002_008E'])


# In[ ]:


for i in county_list[1:]:
    edu_data_new =  censusdata.download('acs5', 2018,
           censusdata.censusgeo([('state', '12'),
                                 ('county', i),
                                 ('block group', '*')]),['B29002_002E','B29002_003E','B29002_004E','B29002_005E',
                                                         'B29002_006E','B29002_007E','B29002_008E'])
    education_data = education_data.append(edu_data_new)


# In[ ]:


education_data["Education: Below Middle School"] = (education_data.B29002_002E)


education_data["Educatiohn: High School"] =  (education_data.B29002_003E + education_data.B29002_004E)


education_data["Education: College"] = (education_data.B29002_005E + education_data.B29002_006E + 
                                        education_data.B29002_007E)

education_data['Education: Graduate and Above'] = (education_data.B29002_008E) 

education_data= education_data[["Education: Below Middle School","Educatiohn: High School","Education: College", 'Education: Graduate and Above']]


# In[ ]:


employment_data = censusdata.download('acs5', 2018,
           censusdata.censusgeo([('state', '12'),
                                 ('county', '091'),
                                 ('block group', '*')]),['B23025_001E','B23025_002E','B23025_003E','B23025_004E',
                                                         'B23025_005E','B23025_006E','B23025_007E'])


# In[ ]:


for i in county_list[1:]:
    employment_data_new = censusdata.download('acs5', 2018,
           censusdata.censusgeo([('state', '12'),
                                 ('county', i),
                                 ('block group', '*')]),['B23025_001E','B23025_002E','B23025_003E','B23025_004E',
                                                         'B23025_005E','B23025_006E','B23025_007E'])
    employment_data = employment_data.append(employment_data_new)


# In[ ]:


employment_data["Employment: Employed"] = employment_data.B23025_004E
employment_data["Employment: Unemployed"] = employment_data.B23025_005E
employment_data["Employment: Not In Labor Force"] = employment_data.B23025_007E
employment_data = employment_data[["Employment: Employed","Employment: Unemployed","Employment: Not In Labor Force"]]


# In[ ]:


health_ins_data = censusdata.download('acs5', 2018,
           censusdata.censusgeo([('state', '12'),
                                 ('county', '091'),
                                 ('block group', '*')]),['B27010_003E','B27010_010E','B27010_017E','B27010_019E',
                                                         'B27010_026E','B27010_033E','B27010_035E','B27010_042E',
                                                         'B27010_050E','B27010_052E','B27010_058E','B27010_066E'])


# In[ ]:


for i in county_list[1:]:
    health_data_new = censusdata.download('acs5', 2018,
           censusdata.censusgeo([('state', '12'),
                                 ('county', i),
                                 ('block group', '*')]),['B27010_003E','B27010_010E','B27010_017E','B27010_019E',
                                                         'B27010_026E','B27010_033E','B27010_035E','B27010_042E',
                                                         'B27010_050E','B27010_052E','B27010_058E','B27010_066E'])
    health_ins_data = health_ins_data.append(health_data_new)


# In[ ]:


health_ins_data["Insurance: 2 or More"] = health_ins_data.B27010_010E + health_ins_data.B27010_026E + health_ins_data.B27010_042E +health_ins_data.B27010_058E
health_ins_data["Insurance: One"] = health_ins_data.B27010_003E + health_ins_data.B27010_019E  +health_ins_data.B27010_035E +health_ins_data.B27010_052E
health_ins_data["Insurance: No"] = health_ins_data.B27010_017E + health_ins_data.B27010_033E   + health_ins_data.B27010_050E + health_ins_data.B27010_066E
health_ins_data = health_ins_data[["Insurance: 2 or More", "Insurance: One", "Insurance: No"]]


# In[ ]:


income_data = censusdata.download('acs5', 2018,
           censusdata.censusgeo([('state', '12'),
                                 ('county', '091'),
                                 ('block group', '*')]),['B28004_002E','B28004_006E','B28004_010E','B28004_014E',
                                                         'B28004_018E','B28004_022E'])


# In[ ]:


for i in county_list[1:]:
    income_data_new = censusdata.download('acs5', 2018,
           censusdata.censusgeo([('state', '12'),
                                 ('county', i), ('block group', '*')]),['B28004_002E','B28004_006E','B28004_010E','B28004_014E',
                                                         'B28004_018E','B28004_022E'])
    income_data = income_data.append(income_data_new)


# In[ ]:


income_data['Income: Less than 10,000'] = income_data.B28004_002E
income_data['Income: Between 10,000 to 19,999'] = income_data.B28004_006E
income_data['Income: Between 20,000 to 34,999'] = income_data.B28004_010E
income_data['Income: Between 35,000 to 49,999'] = income_data.B28004_014E
income_data['Income: Between 50,000 to 74,999'] = income_data.B28004_018E
income_data['Income: More than 75,000'] = income_data.B28004_022E
income_data = income_data[['Income: Less than 10,000','Income: Between 10,000 to 19,999',
                          'Income: Between 20,000 to 34,999','Income: Between 35,000 to 49,999',
                          'Income: Between 50,000 to 74,999','Income: More than 75,000']]


# In[ ]:


result = pd.concat([age_data,race_data,education_data,income_data,employment_data,health_ins_data],axis=1,sort=False)


# In[ ]:


result.to_csv("result.csv",index_label = "Block Group")


# In[ ]:




