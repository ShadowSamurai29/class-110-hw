import statistics
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random
import statistics
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()

dataset = []
for i in range (0, 100) :
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)

print("Mean of reading_time:-", mean)
print ("std_deviation of reading_time:-", std_deviation)

def random_set_of_mean(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode = "lines", name = "MEAN"))
    fig.show()

def setup():
    mean_list = []
    for i in range (0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    print("Mean of reading_time distribution:-", mean)

setup()

reading_time = statistics.mean(data)
print("reading_time mean:-", reading_time)

