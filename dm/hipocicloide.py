import subprocess
import sys
import time

plot = subprocess.Popen('/usr/bin/gnuplot', stdin = subprocess.PIPE, stdout = subprocess.PIPE)

plot.stdin.write("""
set term x11
k = 5.5 
k1 = k - 1
x(t) = k1*cos(t) + cos(t*k1)
y(t) = k1*sin(t) - sin(t*k1)

set parametric
unset key
set size ratio - 1
set xrange [-6:6]
set yrange [-6:6]
set trange [0:0]
plot x(t), y(t) with lines lw 2
""")

delta = 'pi/10'
i = 1
try:
	while 1 :
		v = str(i) + '*' + delta
		plot.stdin.write( ' set trange[0:' + v + ']\n' )
		plot.stdin.write( 'rep\n')
		i = i + 1
		time.sleep(0.2)
		if i == 42 :
			time.sleep(2)
			i = 0
except KeyboardInterrupt:
	plot.terminate()
	print "Bye!"
	sys.exit(0)
