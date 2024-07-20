from UniversalPlotter import UniversalPlotter
def main()->None:
    plotter = UniversalPlotter('test.csv',['A,D','B,C','A,D','A,D'],coll_num=3)
    plotter.startPlot()
if __name__ == "__main__":
    main()