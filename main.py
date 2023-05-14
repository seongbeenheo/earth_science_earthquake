
import pandas as pd
import folium

earthquake=pd.read_csv('earthquake.csv',encoding='cp949',delimiter=',')
earthquake_x=earthquake['latitude']
earthquake_y=earthquake['longitude']
earthquake_time=earthquake['time']
earthquake_level=earthquake['level_of_depth']

m = folium.Map(zoom_start=0,max_bounds=True,min_lat=-85 ,max_lat=85 ,min_lon=-175,max_lon=187)


level_1 = []
level_2 = []
level_3 = []
time_1 = []
time_2 = []
time_3 = []

for i in range(len(earthquake)-1):
    x = earthquake_x[i]
    y = earthquake_y[i]
    level=earthquake_level[i]
    time=earthquake_time[i]
    
    if level == 1:
        level_1.append([x,y])
        time_1.append(time)
    if level == 2:
        level_2.append([x,y])
        time_2.append(time)
    if level == 3:
        level_3.append([x,y])
        time_3.append(time)
    
print(len(level_1))
print(len(level_2))
print(len(level_3))
    
for i in range(8000): #len(level_1)
    folium.Circle(
        location = level_1[i],
        radius = 50,
        color = '#FF0000',
        fill = 'crimson',
        popup = time_1[i],
    ).add_to(m)
    
for i in range(8000): #len(level_2)
    folium.Circle(
        location = level_2[i],
        radius = 50,
        color = '#0000FF',
        fill = 'crimson',
        popup = time_2[i],
    ).add_to(m)

for i in range(len(level_3)):
    folium.Circle(
        location = level_3[i],
        radius = 50,
        color = '#000000',
        fill = 'crimson',
        popup = time_3[i],
    ).add_to(m)
    
m.save('earthquake2.html')
print('finish')