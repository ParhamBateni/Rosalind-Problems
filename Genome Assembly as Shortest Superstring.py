from Bio import SeqIO
from networkx import DiGraph
fasta_seqs=SeqIO.parse(open('rosalind_input.txt'),'fasta')
seqs=[fasta_seq.seq for fasta_seq in fasta_seqs]
graph=DiGraph()
graph_dict=dict()
min_overlap=len(seqs[0])//2
for seq1 in seqs:
    for seq2 in seqs:
        if seq1==seq2:continue
        for l in range(min(len(seq1),len(seq2))-1,min_overlap,-1):
            if seq1[-l:]==seq2[:l]:
                graph.add_edge(str(seq1),str(seq2))
                graph_dict[str(seq1)]=(str(seq2),l)
start_node=[x[0] for x in graph.in_degree if x[1]==0][0]
shortest_common_substring=''
overlap=0
while True:
    shortest_common_substring+=start_node[overlap:]
    if not graph_dict.get(start_node):
        break
    overlap = graph_dict.get(start_node)[1]
    start_node=graph_dict.get(start_node)[0]
print(shortest_common_substring)

