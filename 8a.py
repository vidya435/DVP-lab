import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure,show
X=np.linspace(0,10,100)
Y=np.sin(X)
TOOLS="pan,wheel_zoom,box_zoom,reset,save,box_select"
p1=figure(title="vidya-1KI23CS178",tools=TOOLS)
p1.line(X,Y,line_width=2,legend_label="sin(X)",color="red")
p1.line(X,2*Y,line_width=2,legend_label="2sin(X)",color="blue")
p1.line(X,3*Y,line_width=2,legend_label="3sin(X)",color="green")
p1.legend.title="Markers"
show(gridplot([p1],ncols=1,width=400,height=400))

