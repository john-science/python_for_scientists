
import os
import numpy
from matplotlib import pyplot

def main():

    ###  initializing figure
    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    ax.plot(range(10), range(100,110))

    ###  connecting figure to interactive functions
    cid1 = fig.canvas.mpl_connect('button_press_event', onClick)
    #cid2 = fig.canvas.mpl_connect('button_release_event', onClickRelease)
    #cid3 = fig.canvas.mpl_connect('key_press_event', onKeyPress)

    ax.set_xlim(0, 10)
    ax.set_ylim(100, 110)

    pyplot.show()



def onClick(event):

    button = event.button
    dblclick = event.dblclick
    x = event.x
    y = event.y
    xdata = event.xdata
    ydata = event.ydata

    print('\n')
    print('you pressed button ', button)
    print('was it a double-click? ...', dblclick)
    print('coordinates (x,y) = ', x, y)
    print('data coordinates (xd,yd) = ', xdata, ydata)


def onClickRelease(event):

    button = event.button
    dblclick = event.dblclick
    x = event.x
    y = event.y
    xdata = event.xdata
    ydata = event.ydata

    print('\n')
    print('you released button ', button)
    print('was it a double-click? ...', dblclick)
    print('coordinates (x,y) = ', x, y)
    print('data coordinates (xd,yd) = ', xdata, ydata)


def onKeyPress(event):

    key = event.key
    x = event.x
    y = event.y
    xdata = event.xdata
    ydata = event.ydata

    print('\n')
    print('you pressed key ', key)
    print('coordinates (x,y) = ', x, y)
    print('data coordinates (xd,yd) = ', xdata, ydata)



if __name__ == '__main__':
    main()

