# -*- coding: utf-8 -*-
import Bio
print Bio.__version__

import Bio.Alphabet
print Bio.Alphabet.ThreeLetterProtein.letters    # abreviaturas de las proteínas

from Bio.Alphabet import IUPAC
print IUPAC.IUPACProtein.letters    # letras de proteinas
print IUPAC.unambiguous_dna.letters    # letras de bases de adn
print IUPAC.unambiguous_rna.letters    # letras de bases de arn
print IUPAC.ambiguous_dna.letters    # letras IUPAC de bases de adn
print IUPAC.ExtendedIUPACProtein.letters    # letras de todas las proteínas existentes
print IUPAC.ExtendedIUPACDNA.letters    # letras de todas las bases existentes

from Bio.Seq import Seq
seq = Seq('CCGGTT',IUPAC.unambiguous_dna)
print seq
seq=seq.transcribe()	#must be DNA to transcribe to RNA
print seq
seq=seq.translate()		#must be DNA to translate to protein
print seq

#tipo de dato secuencia
seq=Seq('CCGGUU',IUPAC.IUPACUnambiguousRNA())	#constructor class IUPAC...RNA
print seq
print seq.back_transcribe()	#must be RNA to backtranscribe to DNA

seq=Seq('ATGGTCTTTCCAGACGCG',IUPAC.unambiguous_dna)
print Seq.transcribe(seq)	#as function, up is as method

print seq[:5]	#methods as string
print len(seq)
#seq[0]='C'	#aren't mutables
st=str(seq)		#toString
print st

#tipo de dato secuencia editable
from Bio.Seq import MutableSeq
mut_seq=seq.tomutable()	#convertirlo a tipo seq mutable
print mut_seq
mut_seq[0]='C'
print mut_seq
mut_seq=MutableSeq('ATGCCG',IUPAC.IUPACUnambiguousDNA())
#has methods as a list: append(), insert(), pop(), remove()
mut_seq[1:3]='TTT'
mut_seq.reverse()
mut_seq.complement()
print mut_seq
mut_seq.reverse_complement()
print mut_seq

#tipo de dato metadatos de secuencia
from Bio.SeqRecord import SeqRecord
seqrec=SeqRecord(seq,id='001', name='My Secuencia')
#2 main attributes:
#	id: string identifier, optional, recommended
#	seq: Seq object, required
#additional attributes
#	name, description: name and more info of sequence
#	dbxrefs: list of strings, each string an id of a DB
#	features: list of SeqFeature objects, those found in Genbank records
#	annotations: dictionary with further info, can't be set on initialization
seqrec=SeqRecord(Seq('mdstnvrsgmksrkkkpkttvidddddcmtcsacqsklvkisditkvsldyintmrgntlacaacgsslkllndfas',Bio.Alphabet.generic_protein), id='P20994.1', name='P20994', description='Protein A19', dbxrefs=['Pfam:PF05077', 'InterPro:IPR007769', 'DIP:2186N'])
seqrec.annotations['note']='A simple note'
print seqrec

#tipo de dato alineamiento de secuencias, guarda no procesa
from Bio.Align.Generic import Alignment
seq1='MHQAIFIYQIGYPLKSGYIQSIRSPEYDNW'
seq2='MH--IFIYQIGYALKSGYIQSIRSPEY-NW'
align=Alignment(Bio.Alphabet.Gapped(IUPAC.protein))	#instance of Alignment class
align.add_sequence('asp',seq1)
align.add_sequence('unk',seq2)
print align
#Alignment methods
#get_all_seqs:	return all sequences in the alignment as a list of SeqRecord
for s in align.get_all_seqs():	#in align: (the same)
	print '->',s.seq
#get_seq_by_num(n): return only the selected sequence by index
print str(align.get_seq_by_num(1))	#Seq object
print align[0]	#SeqRecord object
print str(align[0].seq)
#get_alignment_length(): get length of alignment
print align.get_alignment_length()
#get_column(n): return a string with all the letters in the n column
print align.get_column(0)
print align.get_column(2)

#AlignInfo module: to extract info from alignment objects
from Bio.Align import AlignInfo
#print_info_content function
#SummaryInfo,PSSM classes
summary=AlignInfo.SummaryInfo(align)
print summary.information_content()
print summary.dumb_consensus()
print summary.gap_consensus()
print summary.get_column(2)	#get column by index
print summary.alignment		#complete description

#Bio.SeqIO: interface to input & output sequence file formats
#passed to your program as SeqRecord objects
#can read alignment file formats and return each record as a SeqRecord
#to retrieve an alignment object, use Bio.AlignIO module

#Read sequence files
#parse(file_handle, format['fasta','genbank'...])
#	return a generator for SeqRecords
from Bio import SeqIO
leo=open('archivo.gnk')
print SeqIO.parse(leo,'genbank').next()
leo.close()
#when only one sequence in the file, use SeqIO.read() instead
leo=open('archivo.gnk')
print SeqIO.read(leo,'genbank')
leo.close()
leo=open('myprots.fas')
for record in SeqIO.parse(leo,'fasta'):
	id=record.id
	seq=record.seq
	print 'name:',id,'size:',len(seq)
leo.close()

#Write sequence files
#write(iterable, file_handle, format)
#	iterable of SeqRecord objects
scribo=open('NC2033.fasta','w')
#record=['CGTTA','GCGCGCGCGCGC']
record=[]
for seq in ['CGTTA','GCGCGCGCGCGC']:
	newRecord=SeqRecord(Seq(seq,IUPAC.unambiguous_dna))
	record.append(newRecord)
SeqIO.write(record,scribo,'fasta')
scribo.close()
#Sequence Formats:
#	ace: read the contig seqs from an ACE assembly file
#	embl: EMBL flat file format
#	fasta: simple format, each record starts with an id starting with '>'
#	genbank: GenBank or GenPept flat file format
#	ig: IntelliGenetics file format, used by MASE
#	phd: output from PHRED
#	swiss: Swiss-Prot (UniProt) format
#	tab: simple two column tab separated sequence files

#Bio.AlignIO: interface to I/O alignments
#similar to SeqIO, instead return Alignment objects
#Input: read, parse. Output: write
#	read(handle,format[,sec_count]): file handle, alignment format
#	sec_count: optional, the number of sequences per alignment
#	return an Alignment object
from Bio import AlignIO
leo=open('secu3.aln','r')
align=AlignIO.read(leo,'clustal')
leo.close()
print align

#	parse(handle,format): parsing alignments from a file with more than one alignment.
#	return an iterator with all the Alignment objects
aligns=[]
leo=open('secu3.aln','r')
for align in AlignIO.parse(leo,'clustal'):
	print align.get_alignment_length()
	aligns.append(align)
leo.close()

#	write(iterable,handle,format): set of Alignment objects, file handle, file format.
leo=open('aligns.phy','w')
AlignIO.write(aligns,leo,'phylip')
leo.close()

#BLAST
#blastall(blast exe, program name, DB, input file, [align_view=7], [params])
#	returns a tuple of two file objects.
#	1: result, 2: BLAST error message (if any)
#from Bio.Blast import NCBIStandalone as BLAST

#Data. Biopython isn't just tools, it's also useful Data
from Bio.Data import IUPACData
#by IUPAC an M stands for any base that is:
print IUPACData.ambiguous_dna_values['M']
print IUPACData.ambiguous_dna_values['H']
print IUPACData.ambiguous_dna_values['X']
#protein_weights is a dictionary of IUPACaminoacid: weight
print IUPACData.protein_weights
#all possible characters
print IUPACData.protein_letters
print IUPACData.extended_protein_letters
print IUPACData.ambiguous_dna_letters
print IUPACData.unambiguous_dna_letters
print IUPACData.ambiguous_rna_letters
print IUPACData.unambiguous_rna_letters
print IUPACData.ambiguous_dna_complement	#dictionary of complements
#and a lot more
from Bio.Data import CodonTable
print CodonTable.generic_by_id[2]

#SeqUtils. Several functions to deal with DNA and protein sequences.
#DNA utils
import Bio.SeqUtils as SeqUtils
print SeqUtils.GC('gacgatcggtattcgtag')	#GC content
from Bio.SeqUtils import MeltingTemp
print MeltingTemp.Tm_staluc('tgcagtacgtatcgt')	#DNA/RNA melting temperature
#checksum functions: short alphanumeric string signature of a file or sequence
#usually written in description of sequence
#cgc is a easy, weak, very used checksum (better crc32, crc64)
from Bio.SeqUtils import CheckSum
myseq='acaagatgccattgtcccccggcctcctgctgctgct'
print CheckSum.gcg(myseq)
print CheckSum.crc32(myseq)
print CheckSum.crc64(myseq)
print CheckSum.seguid(myseq)
#Protein utils
from Bio.SeqUtils import ProtParam
myprot=ProtParam.ProteinAnalysis('MLTNK')
print myprot.count_amino_acids()
print myprot.get_amino_acids_percent()
print myprot.molecular_weight()
print myprot.aromaticity()
print myprot.instability_index()
print myprot.flexibility()
print myprot.isoelectric_point()
print myprot.secondary_structure_fraction()