import graphing
import pandas as pd

df = pd.read_csv('./data/data.csv')

# print(df['x_variable']) 
red_points = df[df['red'] == 1]
blue_points = df[df['red'] == 0]

red_x_points = red_points['x_variable']
red_y_points = red_points['y_variable']
blue_x_points = blue_points['x_variable']
blue_y_points = blue_points['y_variable']

graphing.graphData(red_x_points=red_x_points, red_y_points=red_y_points,
                   blue_x_points=blue_x_points, blue_y_points=blue_y_points,
                   training_red = red_points, training_blue = blue_points
                   )


