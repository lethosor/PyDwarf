import pydwarf

@pydwarf.urist(
    name = 'pineapple.nograzers',
    version = 'alpha',
    author = 'Sophie Kirschner',
    description = 'Removes all [GRAZER] and [STANDARD_GRAZER] tokens.',
    compatibility = (pydwarf.df_0_34, pydwarf.df_0_40)
)
def nograzers(raws):
    grazers = raws.all(exact_value='GRAZER')
    standardgrazers = raws.all('STANDARD_GRAZER')
    for grazer in grazers: grazer.remove()
    for grazer in standardgrazers: grazer.remove()
    if len(grazers) or len(standardgrazers):
        return pydwarf.success('Removed %d GRAZER and %d STANDARD_GRAZER tokens.' % (len(grazers), len(standardgrazers)))
    else:
        return pydwarf.failure('I found no grazer tokens to replace.')

