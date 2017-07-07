set term x11
set parametric

x(t) = r * cos(t)
y(t) = r * sin(t)
r = 4
set yrange[0:pi/4]
set size ratio -1
plot x(t), y(t)
pause - 1
