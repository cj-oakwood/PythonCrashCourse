from die import Die

import pygal

die = Die()

results = []

for roll_num in range(10000):
    result = die.roll()
    results.append(result)

freqencies = []
for value in range(1, die.num_sides+1):
    freqency = results.count(value)
    freqencies.append(freqency)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_lables = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6', freqencies)
hist.render_to_file('die_visual.svg')

#print(freqencies)

