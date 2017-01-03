from os import getenv
import pymssql
from bokeh.plotting import figure, output_file, show

server = "instance1.cy2x1syxxkbe.us-west-2.rds.amazonaws.com"
user = "master"
password = "passwordGoesHere"

conn = pymssql.connect(
    host = server, 
    port = "1433", 
    user = user, 
    password = password, 
    database = "test"
)

cursor = conn.cursor(as_dict=True)


# prepare some data
x = []
y = []


cursor.execute('SELECT * FROM persons')
for row in cursor:
    print row['id']
    x.append(row['id']) 
    y.append(row['id'])


# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)

# show the results
show(p)

conn.close()
