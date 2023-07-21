def age(x):
    ''' Extracts the age from a person's record '''
    return int(x['value']['age'])

def cas(x):
    ''' Checks and sets the current maximum '''
    k = 'age:maximum'
    v = execute('GET', k)
    v = int(v) if v else 0
    if x > v:
        execute('SET', k, v)

gb = GearsBuilder()
gb.map(age)
gb.foreach(cas)
gb.register('person:*')


