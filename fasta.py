with open("dna.txt", "r") as f:
    
    
    max_gc_name, max_gc_content= '', 0
    fasta= f.readline().rstrip()
    while fasta:
        name, seq = fasta[1:], ''
        fasta = f.readline().rstrip()
        while not fasta.startswith(">") and fasta:
            seq += fasta
            fasta = f.readline().rstrip()
        seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
        if seq_gc_content > (max_gc_content):
            max_gc_content, max_gc_name =seq_gc_content, name
print(max_gc_name)
print(max_gc_content * 100)
