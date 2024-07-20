from privte_python_projects.UniversalPlotter.UniversalPlotter import UniversalPlotter
import asyncio
from time import sleep
def main()->None:
    plotter = UniversalPlotter('test.csv',['A,D','B,C','A,D','A,D'],coll_num=3)
    plotter.startPlot()
if __name__ == "__main__":
    main()