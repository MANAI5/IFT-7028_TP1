import numpy as np
import pandas as pd 

class Simulation:
    def __init__(self):
        self.nb_in_system = 0
        self.clock = 0.0
        self.t_arrival = self.generate_interarrival()
        self.t_depart = float('inf')

        self.nb_arrivals = 0
        self.nb_departs = 0
        self.t_wait = 0.0

        self.num_in_q=0
        self.number_in_queue=0

        
    def advance_time(self):

        next_event=min(self.t_arrival,self.t_depart)
        self.t_wait = self.nb_in_system*(next_event - self.clock)

        self.clock = next_event

        if self.t_arrival <= self.t_depart:
            self.arrival_event()
        else:
            self.depart_event()


    def arrival_event(self):
        self.nb_in_system += 1
        self.nb_arrivals += 1
        self.num_in_q += 1
        self.number_in_queue += 1

        if self.nb_in_system <= 1:
            self.t_depart = self.clock + self.generate_service()
            self.t_arrival = self.clock + self.generate_interarrival()


        
    def depart_event(self):
        self.nb_in_system -= 1
        self.nb_departs += 1
        self.num_in_q -= 1
        self.number_in_queue -= 1
        if self.nb_in_system > 0:
            self.t_depart = self.clock + self.generate_service()
        else:
            self.t_depart=float('inf')
        pass
    def generate_interarrival(self):
        return np.random.exponential(12*3600)
    def generate_service(self):
        return np.random.exponential(9.5*3600)


np.random.seed(2022)


s=Simulation()
df=pd.DataFrame(columns=['Average interarrival time','Utilization','Total average wait time'])

#100 replications
for i in range(100):
    np.random.seed(i)
    s.__init__()
    while s.clock <= 40000*60 :
        s.advance_time()
    a=pd.Series([s.clock/s.nb_arrivals,s.number_in_queue,s.t_wait],index=df.columns)
    df=df.append(a,ignore_index=True)


#utilization=nb de bateaux dans la quai

#TO BE CONTINUED ..
