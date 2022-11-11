from data import *



def verificateDNA(dna):
    tmp = dna.upper()
    for nuc in dna:
        if nuc not in Nucleotides:
            return quit()
    return tmp

def structure(dna):
    foo = str.maketrans('ATCG', 'TAGC')
    return dna.translate(foo)[::-1]

def show_dna(dna):
    print(f'5- {dna} -3')
    print(f'3- {structure(dna)[::-1]} -5')
    print('~OR~')
    print(f'3- {dna} -5')
    print(f'5- {structure(dna)[::-1]} -3')

def transcription(dna):
    return dna.replace('T', 'U')

def countNuc(dna):
    Dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nuc in dna:
        Dict[nuc] += 1
    return Dict

def gc_content(dna):
    return ((dna.count('C') + dna.count('G')) / len(dna) * 100)











