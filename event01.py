def maximum(a, x):
    ''' Returns the maximum '''
    a = a if a else 0
    return max(a, x)

gb = GearsBuilder()
gb.map(lambda x: int(x['value']['age']))
gb.accumulate(maximum)
gb.register('person:*')


