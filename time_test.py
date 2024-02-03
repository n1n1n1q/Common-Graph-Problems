"""
Time test and graph drawer
"""
import time
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

class Tester():
    """
    Time test and graph drawer class
    """
    def __init__(self, function: callable) -> None:
        self.function=function
        self.time_list=[0]
        self.value_list=[0]

    def time_test(self, values = None) -> None:
        """
        Finds how much time the function executes
        """
        start_time=time.time()
        values.sort()
        if not values:
            self.function()
            self.time_list.append(time.time()-start_time)
            self.value_list.append(None)
        for value in values:
            self.function(value)
            self.time_list.append(time.time()-start_time)
            self.value_list.append(value)

    def draw_graph(self, other=None):
        """
        Draws time graph
        """
        lines=[]
        lines.append(plt.plot(self.time_list,self.value_list))
        lines[-1][0].set_label(self.function.__name__)
        plt.xlabel('Runtime')
        plt.ylabel('Values')
        if other:
            for func in other:
                lines.append(plt.plot(func.time_list,func.value_list))
                lines[-1][0].set_label(func.function.__name__)
        plt.legend()
        plt.show()

if __name__=='__main__':
    def print_test(arg):
        """
        test function
        """
        print(arg)

    tester=Tester(print_test)
    tester.time_test([1,2,34])
    tester2=Tester(print)
    tester2.time_test([4,6,100,99,19,3,5,7])
    tester.draw_graph([tester2])
