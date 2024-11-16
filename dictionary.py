Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
names={1:"raina",2:"kohil",3:"dhoni",4:"prasanth"}
print(names)
{1: 'raina', 2: 'kohil', 3: 'dhoni', 4: 'prasanth'}
names
{1: 'raina', 2: 'kohil', 3: 'dhoni', 4: 'prasanth'}
best_teachers={1:"God",2:"Mother",3:"Father",4:"Friends"}
best_teachers
{1: 'God', 2: 'Mother', 3: 'Father', 4: 'Friends'}
fav_hero={'hero':'prabhas',2011:['1st class']}
fav_hero
{'hero': 'prabhas', 2011: ['1st class']}
best_stud={'csevib':'neha','CSEVIB':'prasanth'}
best_stud[0]

bets_stud['csevib']

best_stud['csevib']
'neha'
best_stud['CSEVIB']
'prasanth'
sports{}

sports={}
print(sports)
{}
print("empty dictionary",sports)
empty dictionary {}
students=dict(1: 'raina', 2: 'kohil', 3: 'dhoni', 4: 'prasanth'})

students=dict({1: 'raina', 2: 'kohil', 3: 'dhoni', 4: 'prasanth'})
print("dictionary using dict():")
dictionary using dict():
print(students)
{1: 'raina', 2: 'kohil', 3: 'dhoni', 4: 'prasanth'}
cricket=dict([03,"raina"),(07,"dhoni")])

cricket=dict([33,"raina"),(07,"dhoni")])

cricket=dict([(33,"raina"),(07,"dhoni")])

cricket=dict([(33,"raina"),(7,"dhoni")])
print(cricket)
{33: 'raina', 7: 'dhoni'}
aidsb={"+ve":"decent",
                    "-ve":{1:"late comes",2:"low attendance"},
                    "best":{1:will work hard",2:"shows improvement"}
                            

aidsb={"+ve":"decent",
                    "-ve":{1:"late comes",2:"low attendance"},
                    "best":{1:will work hard",2:"shows improvement"}}
                            

aidsb={"+ve":"decent",
            "-ve":{1:"late comes",2:"low attendance"},
            "best":{1:will work hard",2:"shows improvement"}}
                    

pplab={"sec":AIDS",
       

pplab={"sec":AIDS",
       

pplab={"sec":"AIDS",
             "Labno":10,
             "Batch2":{
                    "day"':"saturday",
                    

pplab={"sec":"AIDS",
             "Labno":10,
             "Batch1":{"day":"saturday","rnorange":"57-89"}
             "batch2":{"day":"thursday","rnorange:"90-112"}
                       

pplab={"sec":"AIDS",
             "Labno":10,
             "Batch1":{"day":"saturday","rnorange":"57-89"}
             "batch2":{"day":"thursday","rnorange:"90-112"}}
                       

pplab={"sec":"AIDS",
             "Labno":10,
             "Batch1":{"day":"saturday","rnorange":"57-89"}
             "batch2":{"day":"thursday","rnorange":"90-112"}
       

pplab={"sec":"AIDS",
             "Labno":10,
             "Batch1":{"day":"saturday","rnorange":"57-89"}
             "batch2":{"day":"thursday","rnorange":"90-112"}}
       

pplab={"sec":"AIDS",
             "Labno":10,
             "Batch1":{"day":"saturday","rnorange":"57-89"}
             "Batch2":{"day":"thursday","rnorange":"90-112"}
       

pplab={"sec":"AIDS",
             "Labno":10,
             "Batch1":{"day":"saturday","rnorange":"57-89"}
             "Batch2":{"day":"thursday","rnorange":"90-112"}}
       

pplab={"sec":"AIDS",
             "Labno":10,
             "Batch1":{"day":"saturday","rnorange":"57-89"},
             "Batch2":{"day":"thursday","rnorange":"90-112"}}
       
print(pplab)
       
{'sec': 'AIDS', 'Labno': 10, 'Batch1': {'day': 'saturday', 'rnorange': '57-89'}, 'Batch2': {'day': 'thursday', 'rnorange': '90-112'}}
sports={}
       
sports["first"]="crircket"
       
sports[2]="kabbadi"
       
sports["three"]="football"
       
sports
       
{'first': 'crircket', 2: 'kabbadi', 'three': 'football'}
sports['first']
       
'crircket'
sports['three']
       
'football'
sports.get(1)
       
sports.get(2)
       
'kabbadi'
sports[0]
       

sports
       
{'first': 'crircket', 2: 'kabbadi', 'three': 'football'}
del(sports[3])
       

del(sports['three'])
       
sports
       
{'first': 'crircket', 2: 'kabbadi'}
del(pplab[batch'1']['rnorange'])
       

del(pplab['batch1']['rnorange'])
       

del(pplab['Batch1']['rnorange'])
       
pplab
       
{'sec': 'AIDS', 'Labno': 10, 'Batch1': {'day': 'saturday'}, 'Batch2': {'day': 'thursday', 'rnorange': '90-112'}}
del(pplab["Batch1"]['rnorange'])
       

del(pplab["Batch1"]["rnorange"])
       

pplab.clear()
       
aidsb
       

pplab.clear()
       
pplab
       
{}
expsports=sports.copy()
       
exp
       

expsports
       
{'first': 'crircket', 2: 'kabbadi'}
sports
       
{'first': 'crircket', 2: 'kabbadi'}
sports.update({"three":"khokho"})
       
sports
       
{'first': 'crircket', 2: 'kabbadi', 'three': 'khokho'}
gsports={1:"hockey",2;"basketball",3:"tennis"}
       

gsports={1:"hockey",2:"basketball",3:"tennis"}
       
sports
       
{'first': 'crircket', 2: 'kabbadi', 'three': 'khokho'}
sports.update(gsports0
              sports
              

sports.update(gsports)
              
sports
              
{'first': 'crircket', 2: 'basketball', 'three': 'khokho', 1: 'hockey', 3: 'tennis'}
sports.item()
              

>>> sports.items()
...               
dict_items([('first', 'crircket'), (2, 'basketball'), ('three', 'khokho'), (1, 'hockey'), (3, 'tennis')])
>>> sports.values()
...               
dict_values(['crircket', 'basketball', 'khokho', 'hockey', 'tennis'])
>>> sports.pop(2)
...               
'basketball'
>>> sports
...               
{'first': 'crircket', 'three': 'khokho', 1: 'hockey', 3: 'tennis'}
>>> sports.key()
...               

>>> sports.keys()
...               
dict_keys(['first', 'three', 1, 3])
>>> sports.popitem()
...               
(3, 'tennis')
