#!/usr/bin/env python
# coding: utf-8

# In[128]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter


# In[129]:


data = pd.read_csv('movie_bd_v5.csv')
data.sample(5)


# In[134]:


data.describe()


# # Предобработка

# In[135]:


answers = {} # создадим словарь для ответов

# тут другие ваши предобработки колонок например:

#the time given in the dataset is in string format.
#So we need to change this in datetime format
# ...
# добавим в датасет колонку profit это прибыль = сборы - бюджет
data['profit'] = data.revenue - data.budget


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[136]:


# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа
answers['1'] = '5. Pirates of the Caribbean: On Stranger Tides (tt1298650)'
# если ответили верно, можете добавить комментарий со значком "+"


# In[137]:


# тут пишем ваш код для решения данного вопроса:
data[data.budget == data.budget.max()].original_title


# ВАРИАНТ 2

# In[5]:


# можно добавлять разные варианты решения


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[138]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = '2. Gods and Generals (tt0279111)'
#+


# In[139]:


data[data.runtime == data.runtime.max()].original_title


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[140]:


answers['3'] = '3. Winnie the Pooh (tt1449283)'
#+
data[data.runtime == data.runtime.min()].original_title


# # 4. Какова средняя длительность фильмов?
# 

# In[141]:


answers['4'] = '2. 110'
#+
round(data.runtime.mean())


# # 5. Каково медианное значение длительности фильмов? 

# In[142]:


answers['5'] = '1. 107'
#+
round(data['runtime'].median())


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[143]:


# лучше код получения столбца profit вынести в Предобработку что в начале
answers['6'] = '5. Avatar (tt0499549)'
#+
data[data.profit == data.profit.max()].original_title


# # 7. Какой фильм самый убыточный? 

# In[144]:


answers['7'] = '5. The Lone Ranger (tt1210819)'
#+
data[data.profit == data.profit.min()].original_title


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[145]:


answers['8'] = '1. 1478'
#+
len(data[data.profit > 0])


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[146]:


answers['9'] = '4. The Dark Knight (tt0468569)'
#+
data[data.revenue == data[(data.release_year == 2008)].revenue.max()].original_title


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[147]:


answers['10'] = '5. The Lone Ranger (tt1210819)'
#+
data[data.profit == data[(data.release_year >= 2008) & (data.release_year <= 2014)].profit.min()].original_title


# # 11. Какого жанра фильмов больше всего?

# In[185]:


# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале
answers['11'] = '3. Drama'
#+
df_genres = data.genres.str.split('|',expand=True).stack().value_counts()
df_genres.index[0]


# ВАРИАНТ 2

# In[ ]:





# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[183]:


answers['12'] = '1. Drama'
#+
#Отбираем только прибыльные фильмы 
df_pr=data[data.profit>0]
#Получаем все жанры, подсчитываем результат
s_genres=df_pr.genres.str.split('|',expand=True).stack().value_counts()
#выводим результат
s_genres.index[0]


# # 13. У какого режиссера самые большие суммарные кассовые сбооры?

# In[186]:


answers['13'] = '5. Peter Jackson'
#+
#Получаем список всех режиссеров
s_director = data['director'].str.split('|',expand=True).stack().unique()
#Создаем промежуточный словарь
a_dict = {}

#Накапливеам суммы сборов по каждому режиссеру
for director in s_director:
    if(director not in a_dict):        
        a_dict[director] = data[data['director'].str.contains(director,False)]['revenue'].agg('sum')        
    else:
        sum = a_dict[director] 
        a_dict[director] = sum+data[data['director'].str.contains(director,False)]['revenue'].agg('sum')

#Выбираем максимумальный сбор
max_val = max(a_dict.values())
max_value = max(a_dict.values())
final_dict = {k: v for k, v in a_dict.items() if v == max_value}
#Выводим результат
final_dict


# In[187]:


#13 вариант 2
# Получаем всех режисеров
s_director = data['director'].str.split('|',expand=True).stack().unique()
#Создаем результирующий датафрейм
new_df = pd.DataFrame(columns = ['director', 'revenue'])
s = []  # Пустой список

#Накапливеам суммы сборов по каждому режиссеру
for director in s_director:
    new_df.loc[len(new_df),'director'] = director 
    new_df.loc[len(new_df)-1,'revenue']  = data[data['director'].str.contains(director,False)]['revenue'].agg('sum')   
           
#Группируемся по режиссеру         
new_df.groupby('director').agg('sum').sort_values('revenue',ascending=False).head(1)


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[151]:


answers['14'] = '5. Peter Jackson'
#+
#установим отбор только для фильмов Action
df_action = data[data['genres'].str.contains('Action',False)]
#выберем всех режисеров и посчитаем их
df_action['director'].str.split('|',expand=True).stack().value_counts().index[0]


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[152]:


answers['15'] = '3. Chris Hemsworth'
#+
#установим отбор по фильмам за 2012 год
df_2012_release_year = data[(data.release_year == 2012)]
# выберем всех актеров в этих фильмах
list_cast = data['cast'].str.split('|',expand=True).stack().unique()
#создадим DataFrame в который будем аккумулировать результат
new_df = pd.DataFrame(columns = ['cast', 'revenue'])

for cast in list_cast:
    new_df.loc[len(new_df),'cast'] = cast 
    new_df.loc[len(new_df)-1,'revenue']  = df_2012_release_year[df_2012_release_year['cast'].str.contains(cast,False)]['revenue'].agg('sum') 
                
new_df.groupby('cast').agg('sum').sort_values('revenue',ascending=False).head(1)


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[153]:


answers['16'] = '3. Matt Damon'
#+
#посчитаем средний бюджет в датасете
mean_budget = data['budget'].mean()
#отберем фильмы которые являются высокобюджетными 
df_large_mean_budget = data[data['budget'] > mean_budget]
# выберем всех актеров
list_cast = df_large_mean_budget['cast'].str.split('|',expand=True).stack().unique()
#создадим DataFrame в который будем аккумулировать результат
df_result = pd.DataFrame(columns = ['cast', 'count'])

for cast in list_cast:
    df_result.loc[len(df_result),'cast'] = cast 
    df_result.loc[len(df_result)-1,'count']  = df_large_mean_budget[df_large_mean_budget['cast'].str.contains(cast,False)]['imdb_id'].agg('count')
    
df_result.sort_values('count',ascending=False).head(1)


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[154]:


answers['17'] = '2. Action'
#+
#отбираем все фильмы в которых снимался Nicolas Cage
df_nicolas_cage = data[data['cast'].str.contains('Nicolas Cage',False)]
#отбираем эти фильмы по жанрам 
s_genres = df_nicolas_cage['genres'].str.split('|',expand=True).stack()
#Подсчитываем результат
s_genres.value_counts().index[0]


# # 18. Самый убыточный фильм от Paramount Pictures

# In[155]:


answers['18'] = '1. K-19: The Widowmaker (tt0267626)'
#+
#Отберем убыточные фильмы студии Paramount Pictures
df_paramount_pictures = data[(data.profit < 0) & (data['production_companies'].str.contains('Paramount Pictures',False))]
#Сотрируем результат
df_paramount_pictures.sort_values('profit').head(1).original_title


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[156]:


answers['19'] = '5. 2015'
#+
data.groupby('release_year')['revenue'].sum().sort_values(ascending=False).head(1)


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[157]:


answers['20'] = '1. 2014'
#+
#Отбираем фильмы студии Warner Bros
df_warner_bros = data[(data['production_companies'].str.contains('Warner Bros',False))]
#Группируемся по году получаем сумму и сортируем результат 
df_warner_bros.groupby('release_year')['profit'].sum().sort_values(ascending=False).head(1)


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[176]:


answers['21'] = '4. Сентябрь'
#+
#Преобразовываем колонку в datetime 
data['release_date']=pd.to_datetime(data['release_date'])
#Копируем исходный датафрейм
df2 = data.copy(deep=True)
#Создаем колонку месяц и заполняем ее значениями
df2['month_year'] = df2.release_date.dt.month
#Группируемся по созданной колонке и пдсчитываем и сотрируем резутльтат 
df2.groupby('month_year')['imdb_id'].count().sort_values(ascending=False).head(1)


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[178]:


answers['22'] = '2. 450'
#+
df2[(df2['month_year'] >= 6) & (df2['month_year'] <= 8)].count().sort_values(ascending=False).head(1)


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[188]:


answers['23'] = '5. Peter Jackson'
#+
#Преобразовываем колонку к типу датавремя
data['release_date']=pd.to_datetime(data['release_date'])
#Создаем новый датафрейм копией из основного 
df_month = data.copy(deep=True)
#Создаем колонку месяц и заполняем ее значениями
df_month['month_year'] = df_month.release_date.dt.month
#Создаем новый датафрейм отбором по зиминим месяцам из промежуточного 
df_winter_month = df_month[(df_month['month_year'] == 1) | (df_month['month_year'] == 12) | (df_month['month_year'] == 2)]
#Выводим результат
df_winter_month['director'].str.split('|',expand=True).stack().value_counts().index[0]


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[180]:


answers['24'] = '5. Four By Two Productions'
#+
#Получаем серию содержащую все студии
s_companies = data['production_companies'].str.split('|',expand=True).stack().unique()
#Создаем новый датафрейм
df_result = pd.DataFrame(columns = ['production_companies', 'length'])

#Перебираем все студии и помещаем информацию о длине названий в новый датафрейм 
for company in s_companies:
    df_company = data[data['production_companies'].str.contains(company,False)]['original_title']
    for original_title in df_company:          
        df_result.loc[len(df_result),'production_companies'] = company 
        df_result.loc[len(df_result)-1,'length']  = len(original_title)
        
#Преобразовываем тип колонки к числовому
df_result['length'] = df_result['length'].apply(pd.to_numeric)

#Группируемся по студии считаем срежнее значение, сортируем и выводим результат
df_result.groupby('production_companies')['length'].mean().sort_values(axis=0,ascending=False).head(1)


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[181]:


answers['25'] = '3. Midnight Picture Show'
#+
#Получаем серию содержащую все студии
s_companies = data['production_companies'].str.split('|',expand=True).stack().unique()
#Создаем новый датафрейм
df_result = pd.DataFrame(columns = ['production_companies', 'length'])
df_result['length'] = df_result['length'].astype('int')

#Перебираем все студии и помещаем информацию о количестве слов
for company in s_companies:
    df_company = data[data['production_companies'].str.contains(company,False)]['overview']
    for overview in df_company:  
        index = len(df_result)
        df_result.loc[index,'production_companies'] = company         
        df_result.loc[index,'length']  = len(overview.split(' '))
    
#Преобразовываем тип колонки к числовому
df_result['length'] = df_result['length'].apply(pd.to_numeric)

#Группируемся по студии считаем срежнее значение, сортируем и выводим результат
df_result.groupby('production_companies')['length'].mean().sort_values(ascending=False).head(1)


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[173]:


answers['26'] = '1. Inside Out, The Dark Knight, 12 Years a Slave'
#+
#Получаем датафрейм с 1% необходимых фильмов
df_0_99 = data[data['vote_average']>data.quantile(0.99, numeric_only=True)['vote_average']]

#Создаем словарь с вариантами ответов
best_films_dict = { 'Inside Out, The Dark Knight, 12 Years a Slave' : 1
                   ,'BloodRayne, The Adventures of Rocky & Bullwinkle' : 2
                   ,'Batman Begins, The Lord of the Rings: The Return of the King, Upside Down' : 3
                   ,'300, Lucky Number Slevin, Kill Bill: Vol. 1' : 4
                   ,'Upside Down, Inside Out, Iron Man' : 5
                  }

#Создаем словарь для посчитанных вхождений
v_dict = {}

#Создаем функцию которая посчитает количество вхождений 
def get_count(original_titles):
        result = 0
        s_original_titles = original_titles.split(',')
        for original_title in  s_original_titles:
            result += df_0_99[(df_0_99['original_title'].str.contains(original_title.strip(),False))]['imdb_id'].count()
        return result
       
#Перебирая заданные варианты подсчитываем вхождения
for k,v in best_films_dict.items():            
    v_dict[k] = get_count(k)        
    
#Сортируем словарь с подсчитанными вхождениями
max_val = max(v_dict.values())
max_value = max(v_dict.values())
final_dict = {k: v for k, v in v_dict.items() if v == max_value}
#Выводим результат
final_dict


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# In[166]:


answers['27'] ='5. Daniel Radcliffe & Rupert Grint'
#+
#Johnny Depp & Helena Bonham Carter
#Ben Stiller & Owen Wilson
#Vin Diesel & Paul Walker
#Adam Sandler & Kevin James
#Daniel Radcliffe & Rupert Grint

result1 = data[(data['cast'].str.contains('Johnny Depp',False)) & (data['cast'].str.contains('Helena Bonham Carter',False))]['imdb_id'].count()
result2 = data[(data['cast'].str.contains('Ben Stiller',False)) & (data['cast'].str.contains('Owen Wilson',False))]['imdb_id'].count()
result3 = data[(data['cast'].str.contains('Vin Diesel',False)) & (data['cast'].str.contains('Paul Walker',False))]['imdb_id'].count()
result4 = data[(data['cast'].str.contains('Adam Sandler',False)) & (data['cast'].str.contains('Kevin James',False))]['imdb_id'].count()
result5 = data[(data['cast'].str.contains('Daniel Radcliffe',False)) & (data['cast'].str.contains('Rupert Grint',False))]['imdb_id'].count()


print(result1,result2,result3,result4,result5)


# ВАРИАНТ 2

# In[97]:


#Создаем словарь с возможными вариантами
a_dict = {'Johnny Depp & Helena Bonham Carter': 1, 'Ben Stiller & Owen Wilson': 2,'Vin Diesel & Paul Walker': 3
,'Adam Sandler & Kevin James': 4, 'Daniel Radcliffe & Rupert Grint': 5}

#Создаем словарь для посчитанных вхождений
v_dict = {}

#Создаем функцию которая посчитает количество вхождений 
def get_count(actors):
        s_actors = actors.split('&')        
        return data[(data['cast'].str.contains(s_actors[0].strip(),False)) & (data['cast'].str.contains(s_actors[1].strip(),False))]['imdb_id'].count()

#Перебирая заданные варианты подсчитываем вхождения
for k in a_dict.items():
    v_dict[k] = get_count(k)

#Сортируем словарь с подсчитанными вхождениями
max_val = max(v_dict.values())
max_value = max(v_dict.values())
final_dict = {k: v for k, v in v_dict.items() if v == max_value}
#Выводим результат
final_dict


# # Submission

# In[174]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[168]:


# и убедиться что ни чего не пропустил)
len(answers)


# In[ ]:





# In[ ]:




