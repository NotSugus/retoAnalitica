import pandas as pd
import plotly.express as px

df = pd.read_csv('covid19_tweets.csv')

# Usuarios unicos
ds = df['user_name'].value_counts().reset_index()
ds.columns = ['user_name', 'tweets_count']
ds = ds.sort_values(['tweets_count'], ascending=False)
# DataFrame para obtener indice de relevancia
dfr = df.drop(columns=['user_location', 'user_description', 'user_created', 'user_followers',
                       'user_friends', 'user_favourites', 'user_verified', 'date', 'hashtags', 'source',
               'is_retweet']).sort_values(by='user_name', ascending=False).reset_index()
#DataFrame del texto
tc = df['text']

counter = 0
count = 0
count_top = 0
count_user = 0
for i in ds['tweets_count']:
    count = count + int(i)
    counter += 1
    if counter <= 40:
        count_top = count_top + int(i)
for i in ds['user_name']:
    count_user += 1
#print('\ntotal de tweets es: '+ str(count))
#print('total de tweets top 40: ' + str(count_top))
#print('Cantidad de usuarios unicos: ' + str(count_user))
#print(ds)

fig = px.bar(
    ds.head(40),
    x="tweets_count",
    y="user_name",
    orientation='h',
    title='Top 40 users by number of tweets',
    width=800,
    height=800
)
#fig.show()

tc = tc.str.lower()
tc = tc.str.split(' ')
#print(tc)
totalwords = 0
totaluwords = 0
s = pd.DataFrame()
uwords = []
commonwords = ['the', 'of', 'and', 'a', 'to', 'in', 'is', 'you', 'that', 'it',
             'he', 'was', 'for', 'on', 'are', 'as', 'with', 'his', 'they', 'at']
columna = {'Palabra':uwords}
for i in tc:
   for word in i:
       if word not in commonwords:
           uwords.append(word)
           totaluwords+=1
       totalwords+=1
s['palabras']=uwords
s = s.value_counts().reset_index()
s.columns = ['palabras', 'repeticiones']
#print(s.head(40))
#print ('total de palabras (incluyendo commonwords): ' + str(totalwords))
#print ('total de palabras (no incluyendo commonwords): ' + str(totaluwords))

fig2 = px.bar(s.head(40),
              x="repeticiones",
              y="palabras",
              orientation='h',
              title='Palabras mas repetidas en los tweets (sin considerar las palabras mas comunes)',
              width=800, height=800)
# fig2.show()

def obt_text(n):
    selection = dfr.iloc[n]
    section = selection['text']
    section = section.lower().split(" ")
    return section
def obt_user(n):
    selection =dfr.iloc[n]
    current_user = selection["user_name"]
    return current_user
# 74435
n = 0
ind_score = 0
checklist = ['#covid19', 'pandemic', 'coronavirus', 'sick', 'virus', 'cure', 'vaccine', 'lockdown', 'china']
user = []
score_user = []
ciclo = True
analisis = True

while ciclo == True:
    X = obt_text(n)
    Y = obt_user(n)
    N = n+1
    if N > 74434:
        ciclo = False
    else:
        print(N)
        Y2=obt_user(N)
    while analisis == True:
        for i in X:
            if i in checklist:
                ind_score+=1
        if Y == Y2:
            analisis=True
        elif Y != Y2:
            user.append(Y)
            score_user.append(ind_score)
            analisis = False
        else:
            analisis = True
    n += 1

print(user)
print(score_user)