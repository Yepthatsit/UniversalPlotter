import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animate
import math
import pandas as pd

class UniversalPlotter:
    """_summary_
    class made to create n live plots out of a csv file wich will alway be in n columns
    """
    figure = plt.figure()
    filename:str = ''
    plots_to_make:list = []
    axes:list = []
    lines:list = []
    sep = ""
    def __init__(self,file:str,plots:list,coll_num:int = 2,separator:str = ',') -> None:
        """_summary_
        initialazes class with all necessery data. To start plot use startPlot method.
        Args:
            file (str): a string with filename or file location
            plots (list): list of values written in format x,y representing x and y axis for a new plot
            coll_num (int): number of collumns (default value is 2)
            separator (str): separator used in file
        """
        self.filename = file
        self.plots_to_make = plots
        self.sep = separator
        columns = coll_num
        rows = math.ceil(len(self.plots_to_make)/columns)
        for i in range(len(self.plots_to_make)):
            subplot = self.figure.add_subplot(rows,columns,i+1)
            line, = subplot.plot([],[],marker = 'o')
            self.axes.append(subplot)
            self.lines.append(line)
    def startPlot(self)-> None:
        """_summary_
        Starts  plot
        """
        try:
            live_plot = animate.FuncAnimation(self.figure,self.__HAndle_Plots,cache_frame_data=False,interval=1000)
            plt.show()
        except KeyboardInterrupt:
            print('Plotting stopped by user.')
    def __HAndle_Plots(self,i)->None:
        data = pd.read_csv(self.filename,sep=self.sep)
        for i in range(len(self.plots_to_make)):
            plot_parameters = self.plots_to_make[i].split(',')
            self.lines[i].set_data(data.loc[:,plot_parameters[0]],data.loc[:,plot_parameters[1]])
            self.axes[i].relim()
            self.axes[i].autoscale_view()
            self.axes[i].set_xlabel(plot_parameters[0])
            self.axes[i].set_ylabel(plot_parameters[1])
        self.figure.tight_layout()
def main() -> None:
    plot = UniversalPlotter(sys.argv[1],sys.argv[2:])
    plot.startPlot()


if __name__ == "__main__":
    main()