set term x11 
set size ratio - 1 
set parametric 
set xrange [0:400] 
set yrange [0:400] 
unset key 
set multiplot
x(t) = r*cos(t) + x0
y(t) = r*sin(t) + y0
r = 10
x0 = 381
y0 = 369
plot x(t),y(t) w l
r = 64
x0 = 277
y0 = 90
plot x(t),y(t) w l lt 2
r = 33
x0 = 206
y0 = 351
plot x(t),y(t) w l
r = 1
x0 = 9
y0 = 390
plot x(t),y(t) w l
r = 3
x0 = 213
y0 = 81
plot x(t),y(t) w l lt 2
r = 3
x0 = 376
y0 = 72
plot x(t),y(t) w l
r = 12
x0 = 167
y0 = 4
plot x(t),y(t) w l
unset multiplot
pause -1