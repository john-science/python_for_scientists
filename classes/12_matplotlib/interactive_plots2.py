
import os
import numpy
from matplotlib import pyplot

def main():
    InteractivePlot()


class InteractivePlot(object):

    def __init__(self):

        ###  initializing figure
        self.fig = pyplot.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(range(10), range(100,110))

        ###  connecting figure to interactive method(s)
        cid = self.fig.canvas.mpl_connect('button_press_event', self.onClick_saveToFile)

        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(100, 110)

        pyplot.show()


    def onClick_saveToFile(self, event):

        xdata = event.xdata
        ydata = event.ydata

        ###  initialize/open the output text file
        if not os.path.exists('./output_data.csv'):
            fopen = open('./output_data.csv', 'w')
            fopen.write('xdata,ydata\n')
        else:
            fopen = open('./output_data.csv', 'a')

        ###  plot an 'x' at each location and refresh plot window
        x = self.ax.plot(xdata, ydata, marker='x', ms=10, color='k')
        pyplot.draw()

        ###  write to output file
        fopen.write('%.2f,%.2f' % (xdata, ydata))
        fopen.write('\n')
        fopen.close()



if __name__ == '__main__':
    main()

