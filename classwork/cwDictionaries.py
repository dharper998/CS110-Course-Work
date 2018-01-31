states = {'Oregon': 'OR', 'Florida': 'FL', 'California': 'CA', 'New York': 'NY', 'Michigan': 'MI'}
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}
cities['NY'] = 'Rochester'
cities['OR'] = 'Salem'
print(cities[states['New York']])
for k in states:
    print(states[k])
print(states.get('Texas', 'TX'))
