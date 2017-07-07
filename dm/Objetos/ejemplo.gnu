set term x11
set size ratio - 1
set parametric
set xrange [0:400]
set yrange [0:400]
unset key
set multiplot

x(t) = r*cos(t) + x0
y(t) = r*sin(t) + y0

r = 20
x0 = 100
y0 = 50
plot x(t),y(t) w l

r = 30
x0 = 50
y0 = 200
plot x(t), y(t) w l lt 2

unset multiplot
pause -1
