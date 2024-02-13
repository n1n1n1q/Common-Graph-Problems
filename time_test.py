"""
Time test and graph drawer
"""
import time
import tqdm
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

    def time_test(self, ITERATIONS, values = [],is_dir=False) -> None:
        """
        Finds how much time the function executes
        """
        for value in tqdm(values):
            tmp_time=0
            tmp_time_2=0
            for _ in range(ITERATIONS):
                tmp_graph=gnp_random_connected_graph(value, 100, is_dir)
                start_time=time.time()
                self.function(tmp_graph)
                tmp_time+=(time.time()-start_time)

                start_time=time.time()
                self.function_nx(tmp_graph,algorithm=self.algorithm) if self.algorithm else self.function_nx(tmp_graph)
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
        ax=plt.subplot()
        ax.plot(self.value_list,self.own_time_list,label=self.function.__name__+\
", own implementation")
        ax.set_ylabel('Runtime')
        ax.set_xlabel('Values')
        ax.plot(self.value_list,self.algo_time_list,label=self.function.__name__+\
", nx implementation")
        ax.legend()
        plt.show()

    @staticmethod
    def test_multiple(functions,VALS,ITERATIONS,is_dir=False):
        time_list=[[0] for _ in range(len(functions))]
        for value in tqdm(VALS):
            tmp_time=[0 for _ in range(len(functions))]
            for _ in range(ITERATIONS):
                tmp_graph=gnp_random_connected_graph(value, 100, is_dir)
                for func in functions:
                    start=time.time()
                    func(tmp_graph)
                    tmp_time[functions.index(func)]+=time.time()-start
            for i, val in enumerate(tmp_time):
                time_list[i].append(val/ITERATIONS)

        lines=[]
        VALS=[0]+VALS
        plt.xlabel('Values')
        plt.ylabel('Runtime')
        print(time_list[0])
        print(VALS)
        for i in range(len(functions)):
            plt.plot(VALS,time_list[i],label=functions[i].__name__)
        plt.legend()
        plt.show()
