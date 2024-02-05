"""
Time test and graph drawer
"""
import time
import matplotlib
import matplotlib.pyplot as plt
from graph import gnp_random_connected_graph
matplotlib.use('TkAgg')

class Tester():
    """
    Time test and graph drawer class
    """
    def __init__(self, function: callable, function_nx: callable, algorithm: str) -> None:
        self.function=function
        self.function_nx=function_nx
        self.algorithm=algorithm
        self.own_time_list=[0]
        self.value_list=[0]
        self.algo_time_list=[0]

    def time_test(self, ITERATIONS, values = []) -> None:
        """
        Finds how much time the function executes
        """
        for value in values:
            tmp_time=0
            tmp_time_2=0
            for _ in range(ITERATIONS):
                tmp_graph=gnp_random_connected_graph(value, 100)
                start_time=time.time()
                self.function(tmp_graph)
                tmp_time+=(time.time()-start_time)

                start_time=time.time()
                self.function_nx(tmp_graph,algorithm=self.algorithm)
                tmp_time_2+=(time.time()-start_time)
            
            self.value_list.append(value)
            self.own_time_list.append(tmp_time/ITERATIONS)
            self.algo_time_list.append(tmp_time_2/ITERATIONS)
            print(f'OWN IMPLEMENTATION\nmean time == {self.own_time_list[-1]} N={value}\n\n\
nx implementation\nmean time == {self.algo_time_list[-1]} N={value}')

    def draw_graph(self):
        """
        Draws time graph
        """
        lines=[]
        lines.append(plt.plot(self.own_time_list,self.value_list))
        lines[-1][0].set_label(self.function.__name__+", own implementation")
        plt.xlabel('Runtime')
        plt.ylabel('Values')
        lines.append(plt.plot(self.algo_time_list,self.value_list))
        lines[-1][0].set_label(self.function.__name__+", nx implementation")
        plt.legend()
        plt.show()

