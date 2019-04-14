from die import Die

import pygal

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

freqencies = []

max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    freqency = results.count(value)
    freqencies.append(freqency)

hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6 + D6', freqencies)
hist.render_to_file('die_visual.svg')

#print(freqencies)

