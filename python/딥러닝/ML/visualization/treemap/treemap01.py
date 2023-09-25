import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {'labels': ["A","B","C","D","E","F","G"],
        'values':[10,20,25,35,10,25,45]}
df = pd.DataFrame(data)        
colors=['#fae588','#f79d65','#f9dc5c','#e8ac65','#e76f51','#ef233c','#b7094c'] #color palette

fig = px.treemap(df, path=['labels'], values='values', width=800, height=400)
fig.update_layout(
    treemapcolorway = colors, 
    margin = dict(t=50, l=25, r=25, b=25)
)

#fig.show()
fig.write_image('C:/Users/Kyeul/Desktop/pycode/언어_연습/practice_language/python/visualization/treemap/fig1.svg')
