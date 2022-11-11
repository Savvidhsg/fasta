from function import *
DNA = 'AGGCCCTTTTAAAAATTCCGGG'

print('valid:\n',verificateDNA(DNA), '\n')

show_dna(DNA)
print('')

print(countNuc(DNA))
print(f'{gc_content(DNA)}%')
print(f'round result: {round(gc_content(DNA))}%')

