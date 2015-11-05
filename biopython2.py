# -*- coding: utf-8 -*-
# http://biopython.org/DIST/docs/tutorial/Tutorial.html
import Bio
print Bio.__version__

#a simple sequence
from Bio.Seq import Seq
myseq = Seq("AGTACACTGGT")    # Seq object is read-only immutable
print myseq
print myseq.alphabet    #doesn't have any specified alphabet
print myseq.complement()
print myseq.reverse_complement()
print

from Bio import SeqIO
for seq_record in SeqIO.parse("ls_orchid.fasta","fasta"):
    print seq_record.id
    print repr(seq_record.seq)    #still a generic SingleLetterAlphabet()
    print len(seq_record)

for seq_record in SeqIO.parse("ls_orchid.gbk","genbank"):
    print seq_record.id
    print repr(seq_record.seq)    #used IUPACAmbiguousDNA, DNA alphabet wo/ checking
    print len(seq_record)
print

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
myseq = Seq('AGTACACTGGTC',IUPAC.unambiguous_dna)
print myseq
print myseq.alphabet

myprot = Seq('AGTACACTGGTP',IUPAC.protein)
print myprot
print myprot.alphabet

print myseq[0], myseq[1:4], myseq[-1]
myseq = Seq('AGATA',IUPAC.unambiguous_dna)
for index, letter in enumerate(myseq):
    print("%i %s" % (index, letter))
print len(myseq)
print Seq('AAAA').count('AA')    #non overlapping search

from Bio.SeqUtils import GC
myseq = Seq('gagaaggaaattaaaggaaattaaacca',IUPAC.unambiguous_dna)
print myseq.count('aa')    #must use same capitalize, non overlapping
print GC(myseq)    # GC content

print myseq[2:10]    #the slice is a new Seq with same alphabet
myseq2 = myseq[::3]
print myseq2, myseq2.alphabet
print myseq[::-1]

print str(myseq), type(str(myseq))    # (automatic) convert to string
#Concatenating sequences
protseq = Seq('EVRNAK',IUPAC.protein)
dnaseq = Seq('ACGT',IUPAC.unambiguous_dna)
#print protseq+dnaseq    #can't concatenate seqs with different alphabets
print myseq+dnaseq
from Bio.Alphabet import generic_alphabet
protseq.alphabet = generic_alphabet    # in order to concatenate them
dnaseq.alphabet = generic_alphabet    # must use generic_alphabet
print protseq+dnaseq

from Bio.Alphabet import generic_nucleotide
nucseq = Seq('GATCGATGC',generic_nucleotide)
dnaseq = Seq('ACGT',IUPAC.unambiguous_dna)
print nucseq.alphabet, dnaseq.alphabet
print nucseq + dnaseq, (nucseq + dnaseq).alphabet    # parent + child = parent type

from Bio.Alphabet import generic_dna
list_seqs = [Seq('ACGT', generic_dna), Seq('CCGG', generic_dna), Seq('TTATT', generic_dna)]
concatenated = Seq('',generic_dna)
for seq in list_seqs:
    concatenated += seq
print concatenated
print sum(list_seqs, Seq('', generic_dna))    # function sum, the same as previous
# Seq shares many methods from string, except join method

print myseq.upper(), myseq.lower()
print 'AA' in myseq, 'AA' in myseq.upper()
myseq = myseq.upper()

print myseq.complement()
print myseq.reverse_complement()
#print myprot.complement()

#Transcription
myrna = myseq.transcribe()    # replace T for U
print myrna, myrna.alphabet
#real biological transcription
mytemplate = myseq.reverse_complement()
myrna = mytemplate.reverse_complement().transcribe()
print myrna
print myrna.back_transcribe()    # replace U for T (RNA->DNA)

#Translation
myrna = Seq('AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG',IUPAC.unambiguous_rna)
print myrna
print myrna.translate()        # translate from RNA to aminoacids, * = stop codon
#print myseq
#print myseq[:-1].translate()    # translate from DNA to aminoacids
print myrna.translate(table='Vertebrate Mitochondrial')    # with a specific table of codons
print myrna.translate(table=2)    # index of table
print myrna.translate(to_stop=True)    # stop translating in first stop codon, which is not translated
print myrna.translate(stop_symbol='@')    # change stop codon symbol

gene = Seq("GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA" + \
    "GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT" + \
    "AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT" + \
    "TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT" + \
    "AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA",
    generic_dna)
print gene.translate()
print gene.translate(table='Bacterial', cds=True)    # cds tells translator to make M first codon whatever it is

#Translation Tables
from Bio.Data import CodonTable
print CodonTable.unambiguous_dna_by_name['Standard']
#print CodonTable.unambiguous_dna_by_id[1]
print CodonTable.unambiguous_dna_by_name['Vertebrate Mitochondrial']
#print CodonTable.unambiguous_dna_by_id[2]
print CodonTable.unambiguous_dna_by_id[1].stop_codons
print CodonTable.unambiguous_dna_by_id[2].start_codons
print CodonTable.unambiguous_dna_by_id[1].forward_table['ACG']    # which aminoacid for this codon

#Comparing Sequences
seq1 = Seq('ACGT',IUPAC.unambiguous_dna)
seq2 = Seq('ACGT',IUPAC.unambiguous_dna)
seq3 = Seq('ACGT',IUPAC.protein)
print id(seq1) == id(seq2)    # seq1 == seq2 look for the same object
print str(seq1) == str(seq2)    # convert to string
print str(seq1) == str(seq3)    # dna similar enought to protein

#MutableSeq
from Bio.Seq import MutableSeq
mutseq = seq1.tomutable()    # convert to MutableSeq
print mutseq, type(mutseq)
mutSeq = MutableSeq('CGTTTAAGCTGC',IUPAC.unambiguous_dna)
print mutSeq, type(mutSeq)
mutseq[1]='T'    # imposible on simple Seq
print mutseq
seq1 = mutseq.toseq()    # convert to Seq
mutSeq.remove('A')    # remove first A
mutSeq[2:-5]='TTTT'
mutSeq.reverse()    # reverse() and reverse_complement() change object itself
print mutSeq
#MutableSeq can't be a dictionary key, Seq and string can

#UnknownSeq
# Subclass of Seq when you know length but not the characters to save memory
from Bio.Seq import UnknownSeq
unk = UnknownSeq(25)
print unk, len(unk), type(unk)
unkDNA = UnknownSeq(20, alphabet=IUPAC.ambiguous_dna)
print unkDNA    # N = any base
unkProt = UnknownSeq(10, alphabet=IUPAC.protein)
print unkProt    # X = any aminoacid

print unkDNA.complement(), unkDNA.reverse_complement()
print unkDNA.transcribe(), unkDNA.translate()
unkProt = unkDNA.translate()
print unkProt, len(unkProt)

#Directly on strings
from Bio.Seq import reverse_complement, transcribe, back_transcribe, translate
noseq = 'GCTGTTATGGGTCGTTGGAAGGGTGGTCGTGCTGCTGGTTAG'
print reverse_complement(noseq)    # these functions
print transcribe(noseq)            # receive either strings
print back_transcribe(noseq)       # Seq, MutableSeq, UnknownSeq
print translate(noseq)

#SeqRecord object
#.seq    A Seq object
#.id    a string ID identifier of the sequence
#.name    a string common name for the sequence
#.description    a string readable description or complete name
#.letter_annotations    a dictionary of adittional info about the letters in the sequence.
#    The values for the keys are (list, tuple, string) with the same length of the sequence.
#.annotations    a dictionary of additional info about the sequence
#.features    a list of SeqFeature objects
#.dbxrefs    a list of string DB cross-references
from Bio.SeqRecord import SeqRecord
seq = Seq('GATC')
seqRec = SeqRecord(seq)
seqRec.id = 'AC12345'
seqRec.name = 'My Personal Sequence'
seqRec.description = 'Made up sequence I wish'
print seqRec

seqRec = SeqRecord(seq, id='AC12345')
seqRec.annotations['evidence']='None. I invented it'
seqRec.letter_annotations['phred_quality']=[40, 40, 38, 30]
print seqRec
print seqRec.letter_annotations

#FASTA file to SeqRecord
record = SeqIO.read('NC_005816.fna','fasta')    # extract an only one sequence from a file
print record
print record.id    # >the_first_word
print record.name    # >the_first_word
print record.description    # >the first line
#none of the others attributes gets filled

#GenBank file to SeqRecord
record = SeqIO.read('NC_005816.gb','genbank')
print record.seq.alphabet    # more specific
print record.id    # locus with version
print record.name    # locus
print record.description    # definition
print record.letter_annotations    # don't have any
print record.annotations['source']    # have many annotations
print record.dbxrefs    # dblink
print len(record.features)    # all fields in Features become SeqFeatures objects
print record.annotations['references']    # all articles quoting the seq

#SeqFeature object
#.type    a string description of the type of feature
#.location    of the SeqFeature on the sequence
#    .ref    any different reference sequence the location is referring to. Usually None
#    .ref_db    the DB any identifier in .ref refers to. Usually None
#    .strand    strand on the sequence the feature is located on.
#                For double stranded nucleotide sequence:
#                1 top strand, -1 bottom strand, 0 important but unknown,
#                None doesn't matter, protein, single stranded
#.qualifiers    dictionary of additional info about the feature.
#.sub_features    for features with complicated locations. Deprecated for CompoundLocation object.
#FeatureLocation object: point to a location in a seq
#    .ExactPosition: a number position
#    .BeforePosition: one position previous to a given number '<13'
#    .AfterPosition: one position after a given number '>30'
#    .WithinPosition: position between two nucleotides '(1.5)' in this way: position 1 is lower boundary, extension 4 is range to higher boundary
#    .OneOfPosition: any of a list of several numbers
#    .UnknownPosition: position of unknown location.
from Bio import SeqFeature
start_pos = SeqFeature.AfterPosition(5)
end_pos = SeqFeature.BetweenPosition(9, left=8, right=9)
mylocation = SeqFeature.FeatureLocation(start_pos, end_pos)
print mylocation, mylocation.start, mylocation.end, int(mylocation.end)

for feature in record.features:
    if 4350 in feature:    # if position 4350 is in any feature
        print feature.type, feature.qualifiers.get('db_xref')

from Bio.SeqFeature import SeqFeature, FeatureLocation
seqParent = Seq('ACCGAGACGGCAAAGGCTAGCATAGGTATGAGACTTCCTTCCTGCCAGTGCTGAGGAACTGGGAGCCTAC')
featu = SeqFeature(FeatureLocation(5, 18), type='gene', strand=-1)    # location [5:18] in reverse_complement
print featu
featureSeq = seqParent[featu.location.start:featu.location.end].reverse_complement()
print featureSeq
print featu.extract(seqParent), len(featu.extract(seqParent)), len(featu), len(featu.location)
# extract gets the subseq in location featu from seqParent

# References publications that mention it
# Bio.SeqFeature.Reference
#    journal: book, magazine, journal name
#    title, authors: of the paper
#    medline_id, pubmed_id: ID en Medline y PubMed
#    comment: about the reference
#    location: to specify location in the sequence mentioned in the paper

# format: method to output as fasta or genbank formatted seq
from Bio.Alphabet import generic_protein
record = SeqRecord( Seq('MMYQQCFASSAC',generic_protein), id='gi|14150838|gb|AAK54648.1|AF376133_1', description='chalcone synthase [Cucumis sativus]')
print record    # normal Seq output
print record.format('fasta')    # fasta output ready for saving in a file

#slicing a SeqRecord
#    preserve id, name, features, description
#    adjust new locations, new features index
#    remove annotations, dbxrefs
record = SeqIO.read('NC_005816.gb', 'genbank')
print len(record), len(record.features)
print record.features[20], record.features[21]    # gene to slice
subRecord = record[4300:4800]    #sliced subseq
print subRecord
print len(subRecord), len(subRecord.features)
print subRecord.features[0], subRecord.features[1]
# index adjusted, location adjusted
print subRecord.annotations, subRecord.dbxrefs
print subRecord.id, subRecord.name, subRecord.description
subRecord.description = 'Yersinia pestis biovar [...] plasmid pPCP1, partial.'
print subRecord.format('genbank')

#Joining Adding seqRecords
#    gives a new SeqRecord
#    adds common id, name, description, annotations, per-letter annotations
#    preserves features
#    adjust locations
#    remember to change ID because it is a new modified version
record = next(SeqIO.parse('SRR020192.fastq','fastq'))
print len(record), record.seq
print record.letter_annotations['phred_quality']
#make a new  without the extra 'T'
left = record[:20]
print left.seq, left.letter_annotations['phred_quality']
right = record[121:]
print right.seq, right.letter_annotations['phred_quality']
# add the parts together
edited = left + right
print len(edited), edited.seq, edited.letter_annotations['phred_quality']
#all this is equal to
edited = record[:20] + record[121:]
#to preserve all dbxrefs and annotations explicitly
# shifted.dbxrefs = record.dbxrefs[:]
# shifted.annotations = record.annotations.copy()

# Reverse-complement of SeqRecord
#    features are transferred
#    recalculated location and strand
#    reversed per letter annotations
#    not transferred id, name, description, annotations, references
#    argument 'True' copy old values, 'False' drop old values, use default or given
record = SeqIO.read('NC_005816.gb','genbank')
print record.id, len(record), len(record.features), len(record.dbxrefs), len(record.annotations)
revcompRec = record.reverse_complement(id='Testing')
print revcompRec, len(revcompRec), len(revcompRec.features), len(revcompRec.dbxrefs), len(revcompRec.annotations)

# Sequence Input/Output
#from Bio import SeqIO
#help(SeqIO) go to the manual of the package

# Reading Sequence Files
# parse method to read sequences as SeqRecord iterator
# iter = Bio.SeqIO.parse(handle, format, alphabet)
# read method to read a sequence as SeqRecord
# seqRec = Bio.SeqIO.read(handle, format, alphabet)
#    handle: a filename or a variable with the data
#    format: of the sequence in the file
#    alphabet: optional, specify alphabet to be used, default: generic alphabet
#    iter: an iterator over SeqRecord objects
#    seqRec: reads only a single seqRecord file
for seq_record in SeqIO.parse('ls_orchid.fasta','fasta'):
    print seq_record.id, len(seq_record)
#for seq_record in SeqIO.parse('ls_orchid.gbk','genbank'):
#    print seq_record.id, len(seq_record)
identifiers = [seq_record.id for seq_record in SeqIO.parse('ls_orchid.gbk','genbank')]
print identifiers    #comprehension lists, generators
#iterators and next()
recIterator = SeqIO.parse('ls_orchid.fasta','fasta')
f1stRec = next(recIterator)
print f1stRec.id, len(f1stRec)
s2ndRec = next(recIterator)
print s2ndRec.id, len(s2ndRec)

# next(parse()) takes the first, read() takes the first and check there musn't be more
f1stRec = next(SeqIO.parse('ls_orchid.gbk','genbank'))

#takes parsing iterator as list
# sort doesn't matter, holds all seqs in immediate memory
records = list(SeqIO.parse('ls_orchid.gbk','genbank'))
print 'Found',len(records),'sequences'
print records[0].id, records[-1].id
#Extracting annotations
for seq_record in SeqIO.parse('ls_orchid.gbk','genbank'):
    print seq_record.annotations['organism'],
print
for seq_record in SeqIO.parse('ls_orchid.fasta','fasta'):
    print seq_record.description.split()[1],
print

#using a file handler
with open('ls_orchid.gbk') as handle:    #with as
    print sum(len(r) for r in SeqIO.parse(handle,'gb'))
#with as = handle=open() TODO handle.close()

#Parsing sequences from Web
# nucleotide seqs from Entrez EFetch interface from NCBI
# not for much a good idea, better download first
from Bio import Entrez
Entrez.email = 'A.N.Other@example.com'
handle = Entrez.efetch(db='nucleotide', rettype='fasta', retmode='text', id='6273291')
seq_record = SeqIO.read(handle, 'fasta')    #fasta
handle.close()

print seq_record.id, len(seq_record.features), 'features'
handle = Entrez.efetch(db='nucleotide', rettype='gb', retmode='text', id='6273291,6273290,6273289')
for seq_record in SeqIO.parse(handle, 'gb'):    #genbank
    print seq_record.id, len(seq_record), seq_record.annotations['organism']
handle.close()
# protein seqs from ExPASy from SwissProt
from Bio import ExPASy
handle = ExPASy.get_sprot_raw('O23729')    #es una 'o'
seq_record = SeqIO.read(handle, 'swiss')
handle.close()
print seq_record.id, seq_record.name, seq_record.seq[:25], seq_record.annotations['organism']

#takes parsing iterator as dictionary DB
#useful for large files where you'll access only some seqs
# Bio.SeqIO.to_dict(iterator): most flexible and memory demanding. A normal dictionary with entries of SeqRecord modificables
# SeqRecords can be changed, added, removed at will. Indexing can take longer
#in-memory dictionary DB key=id value=SeqRecord exception on duplicates
orchid_dict = SeqIO.to_dict(SeqIO.parse('ls_orchid.gbk','genbank'))
print len(orchid_dict), orchid_dict['Z78442.1']
#key_function to change key from seqRecord
def get_accession(record):
    return record.id.split('|')[0]+record.id.split('|')[3]
orchid_dict = SeqIO.to_dict(SeqIO.parse('ls_orchid.fasta','fasta'), key_function=get_accession)
print orchid_dict.keys()[:5]
# new SEGUID checksum
from Bio.SeqUtils.CheckSum import seguid
#for record in SeqIO.parse('ls_orchid.gbk','genbank'):
#    print record.id, seguid(record.seq)
seguid_dict = SeqIO.to_dict(SeqIO.parse('ls_orchid.gbk','genbank'), lambda rec: seguid(rec.seq))
print seguid_dict.keys()[:3]
# Bio.SeqIO.index(filename,format): read only dictionary parsing SeqRecord on demand
# faster to build, faster access, immutable seqRecords
#    alphabet, key function optionals
# saves where the seqRecord is in the file, when needed parses it
# indexed dictionary DB key=id value=file position
orchid_dict = SeqIO.index('ls_orchid.gbk','genbank')
print len(orchid_dict), orchid_dict['Z78475.1'].description
# key_function to change key from id
def get_seguid(identifier):
    return identifier.split('|')[2]+identifier.split('|')[3]
seguid_dict = SeqIO.index('ls_orchid.fasta','fasta', key_function=get_seguid)
print [key for key in seguid_dict.keys()]
# Bio.SeqIO.index_db(): read only dictionary that stores identifiers and files on disk (SQLite3), low memory needs and slow.
# not memory limited, fast get_raw(), indexes multiple files, slowest
#    index filename: '__.idx'
#    seq filename or list of seq filenames to index
#    file format
# database dictionary key=id value= db position
orchid_dict = SeqIO.index_db('ls_orchid.idx', 'ls_orchid.gbk', 'genbank')
print len(orchid_dict), orchid_dict['Z78530.1'].description
print orchid_dict.get_raw('Z78530.1')    # original raw data
#filename on index and index_db can be compressed .bgz
#when not knowing use index, to_dict when not much memory needs

# Writing Sequence Files
# Bio.SeqIO.write() for output
#    SeqRecords objects
#    handle or filename to write to
#    sequence format
rec1 = SeqRecord(Seq('MMYQQGCFASSAC',generic_protein), id='gi|14150838|gb|AAK54648.1|', description='chalcone synthase [Cucumis sativus]')
rec2 = SeqRecord(Seq('YPDYYFRIEWGQ',generic_protein), id='gi|13919613|gb|AAK33142.1|', description='chalcone synthase [Fragaria vesca]')
rec3 = SeqRecord(Seq('MVTVEEFRRRVAT',generic_protein), id='gi|13925890|gb|AAK49457.1|', description='chalcone synthase [Nicotiana tabacum]')
myrecords = [rec1, rec2, rec3]
print SeqIO.write(myrecords, 'myrecords1.fasta','fasta')
# prints number of seqs written
# if exists, overwrite

# Convertion of formats
records = SeqIO.parse('ls_orchid.gbk','genbank')
print SeqIO.write(records, 'myrecords2.fasta','fasta')
#in 1 line: convert(origin file, origin format, destiny file, destiny format)
print SeqIO.convert('ls_orchid.gbk', 'genbank', 'myrecords3.fasta', 'fasta')
# if exists, overwrite

# Convertion to reverse complements
records = (rec.reverse_complement(id='rc_'+rec.id, description='reverse complement') for rec in SeqIO.parse('ls_orchid.fasta','fasta') if len(rec)<700)
SeqIO.write(records, 'rev_comp.fasta', 'fasta')

# Output to formatted string
from StringIO import StringIO
records = SeqIO.parse('ls_orchid.gbk','genbank')
outHandle = StringIO()    # string handle
SeqIO.write(records.next(), outHandle, 'fasta')
fastaString = outHandle.getvalue()    # string variable
print fastaString

# Ch 14. Sequence motif analysis with Bio.motifs
# MOTIFS
from Bio import motifs
instances = [Seq('TACAA'),    Seq('TACGC'),    Seq('TACAC'),
             Seq('AACCC'),    Seq('AATGC'),    Seq('AATGC')]
mtf = motifs.create(instances)
# mtf is a motif object with
#    m.instances: a list of Seqs
#    len(m): length of motif the same of its instances
print mtf.alphabet, sorted(mtf.alphabet.letters)
print mtf, len(mtf)    # printing the motif prints its instances
# m.counts: matrix of count of base per position
# m.counts['base']: dictionary key:base, value: list of counts
# m.counts['base',:]: tuple of counts
# m.counts['base',pos]: count of base in position
# m.counts['base'][pos]: the same
# m.counts[:, pos]: dictionary of position key: base, value: count
#    instead of 'base' you can use alphabetical index
print mtf.counts
print mtf.counts['A'], mtf.counts['G']
print mtf.counts['T'][0], mtf.counts['T',0]    # the same
print mtf.counts[:,3]
print mtf.counts['A',:], mtf.counts[0,:]    # alphabetical index
# m.consensus: Seq of letters with largest value per position
print mtf.consensus
print mtf.anticonsensus    # opposite lowest values
print mtf.degenerate_consensus    # using IUPAC codes
# reverse complement consensus
rc = mtf.reverse_complement()    # revert complements all instantes
print rc
print rc.consensus, rc.degenerate_consensus    # reverse complement consensus
# reverse_complement() and degenerate_consensus only for DNA Seqs motifs
# Sequence logo: 2d graphic of freqs
mtf.weblogo('mymotif.png')    # PNG file path to save

# JASPAR motifs Bio.motifs.jaspar.Motif
#    matrix_id: JASPAR motif ID
#    name: of the transcription factor
#    collection: JASPAR collection of motif
#    tf_class, tf_family: structuras class & family of motif
#    species: as taxonomy IDs
#    tax_group: taxonomic supergroup of motif
#    acc: accesion number of transcription factor protein
#    data_type: type of data used to construct the motif
#    medline: Pubmed ID or literature supporting motif
#    pazar_id: reference ID to PAZAR DB
#    comment: text, notes about motif
# stores motifs in 3 main formats: 2 flat files & SQL DB

# JASPAR sites format
#>ID name count
#seqseqMOTIFMOTIFseqseq
# no added meta info
with open('Arnt.sites') as handle:
    arnt = motifs.read(handle, 'sites')    #motif format 'sites'
print len(arnt.instances), arnt.instances
print arnt.counts

# JASPAR pfm format
#2 9 0 1 32 4
#1 33 4 51 1 0
#9 3 10 0 0 0
#20 0 31 0 0 50
# only count profile matrix
with open('SRF.pfm') as handle:
    srf = motifs.read(handle, 'pfm')    # motif format 'pfm'
print srf.counts
print srf.instances    # direct matrix, it didn't save instances
print arnt.counts.consensus, srf.counts.consensus

# JASPAR jaspar format
## JASPAR website teaches to create a JASPAR SQL DB, which can store all meta info in Motif class
## retrieve from JASPAR DB using Bio.motifs.jaspar.db module
## connect to JASPAR DB using JASPAR5 class
#from Bio.motifs.jaspar.db import JASPAR5
#jdb = JASPAR5(host='hostname', name='dbname', user='user', password='psswrd')
## fetch_motif_by_id method: fetch a motif object by its JASPAR ID
## which consists of baseID.versionumber
## if only baseID used it retrieves the lastest version
#arnt = jdb.fetch_motif_by_id('MA0004')
## fetch_motif_by_name method: fetch it by its exact name
## as names aren't unique, it returns a list
#motfs = jdb.fetch_motif_by_name('Arnt')
#print mtfs[0]    # first of the list
## fetch_motifs method: fetch those which match some criteria
## any of the meta, min_ic (minimum information content), minimum length of matrix, minimum num of sites to construct it
#motfs = jdb.fetch_motifs( collection='CORE', tax_group=['vertebrates','insects'], min_ic=12)
#for motif in motfs:
    #print 'do something with the motif'

print motifs.jaspar.calculate_pseudocounts(arnt)    # create new calculated pseudocounts
print arnt.pseudocounts    # usually zeros
arnt.pseudocounts = motifs.jaspar.calculate_pseudocounts(arnt)
print arnt.pseudocounts
print arnt.counts#, arnt.pssm()

#MEME
# input DNA or protein seqs, output number of motifs requested
with open('meme.txt','r') as handle:
    motfs = motifs.parse(handle,'meme')    # motif meme format
#motfs is an object of Bio.motifs.meme.Record class, list of Motif objects
#attributes
print motfs.version, motfs.datafile, motfs.command, motfs.alphabet
print motfs.sequences    #list of names
print len(motfs)    # number of motifs
for motif in motfs:
    #attributes
    print motif.name, motif.num_occurrences, motif.length, motif.evalue
    print motif.consensus
    print motif.degenerate_consensus
    print len(motif.instances), motif.instances[0], motif.instances[0].start
    print motif.instances[0].pvalue
print motfs[0]    # by index
print motfs['Motif 2']    # by name

#TRANSFAC
#ID motifname
#P0 A C G T
#01 1 2 2 1 S
#12 3 0 1 4 T
#//
# can contain multiple motifs
#with open('transfac.dat') as handle:
#    motfs = motifs.parse(handle,'TRANSFAC')    # motif transfac format
print motfs.version
#for motif in motfs:
    # same as MEME is a Motif object
    # same as dictionary attributes can be called motif['ID']
    # motif attributes use name codes from this table
    #http://biopython.org/DIST/docs/tutorial/Tutorial.html#table%3Atransfaccodes
    #motif attribute .references has its attributes labeled by name codes from the next table

# Output writing motifs by different formats
#one motif
print arnt.format('pfm')
print arnt.format('jaspar')
print arnt.format('transfac')
#multiple motifs
two_motifs = [arnt,srf]
print motifs.write(two_motifs, 'jaspar')
print motifs.write(two_motifs, 'transfac')
#or output in a file

#Position Weight Matrix
#normalized matrix dividing each count by number of instances
#    pseudocounts: new freq of bases in motif, used usually to normalize to prevent 0s by chance
print motif.counts.normalize(pseudocounts=0.5)
print motif.counts.normalize(pseudocounts={'A':0.6, 'C':0.4, 'G':0.4, 'T':0.6})    #    can be a dictionary of bases
pwm = motif.counts.normalize()
# PWM has its own methods to calculate consensus and the rest, affected also by pseudocounts
print pwm.consensus
print pwm.anticonsensus
print pwm.degenerate_consensus
print pwm.reverse_complement()    # PWM of reverse complement of instances

#Position Specific Scoring Matrix
# using log odds ratios, tells us how rare the freq of base per position is
# comparing freq in the motif against freq in the background
# negatives are more freq in the background, positives more freq in the motif
pwm = motif.counts.normalize(pseudocounts=0.2)    # if 0 pssm=-infinitum
pssm = pwm.log_odds()    #log use base 2
print pssm
# by default it assumes all bases are equally likely in background
# to change prob of bases in background use a dictionary parameter
print pwm.log_odds({'A':0.3, 'C':0.2, 'G':0.2, 'T':0.3})
#maximum and minimum scores obtainables are:
print pssm.max, pssm.min
#mean and standard deviation with respect to a background are:
background = {'A':0.3, 'C':0.2, 'G':0.2, 'T':0.3}
print pssm.mean(background), pssm.std(background)
#Mean is important, is equal to Kullback-Leibler divergence or relative entropy
# measures the information content of motif compared to the background
#PSSM objects can apply consensus,anticons, deg_cons, rev_comp

# Searching for instances
# most common use, given a seq find its instances of x motif
testSeq = Seq('TACACTGCATTACAACCCAAGCATTA', mtf.alphabet)
# look for exact matches
print mtf.consensus
for pos, seq in mtf.instances.search(testSeq):
    print pos, seq
for pos, seq in mtf.reverse_complement().instances.search(testSeq):
    print pos, seq    # in rev_comp
# matches using PSSM score
#    threshold: only bases with pssm freq pos above this, default0
for pos, score in pssm.search(testSeq, threshold=3.0):
    print pos, score
    # negative positions refer to motif found in reverse strand, following Python negative indexes
    # then all instances are in testSeq[pos:pos+len(m)]
#position score: get score of motif beginning at every position of the seq given
print pssm.calculate(testSeq)    # only forward scores
print pssm.reverse_complement().calculate(testSeq)    # scores for reverse complement
print background
distribution = pssm.distribution(background=background, precision=10**4)
# distribution object can be used to determine different thresholds
# specify false-positive rate (motif found in background)
print distribution.threshold_fpr(0.01)
# fase-negative rate (motif not found in instance)
print distribution.threshold_fnr(0.1)
# threshold satisfying a ratio between fpr and fnr (fnr/fpr=~t)
print distribution.threshold_balanced(1000)
# threshold satisfying equality between fpr and -log of information content (Hertz and Stormo)
print distribution.threshold_patser()
# getting instances using balanced threshold with rate 1000
threshold = distribution.threshold_fpr(0.01)
print threshold
for pos, score in pssm.search(testSeq, threshold=threshold):
    print pos, score

# Position Specific Scoring Matrix
# pssm attribute per motif object
print motif.pssm    # with pseudocounts 0 => min freq -inf
print [[letter, motif.pseudocounts[letter]] for letter in 'ACGT']
#if you change pseudocounts
motif.pseudocounts = 3.0
print [[letter, motif.pseudocounts[letter]] for letter in 'ACGT']
motif.pseudocounts = None
motif.pseudocounts = {'A':0.2, 'C':0.1, 'G':0.1, 'T':0.2}
print motif.pwm, motif.pssm    #automatically changed
# background distribution used for pssm
print [[letter, motif.background[letter]] for letter in 'ACGT']    # 0.25 for all by default
#if you change background distribution
motif.background = {'A':0.2, 'C':0.3, 'G':0.3, 'T':0.2}
print [[letter, motif.background[letter]] for letter in 'ACGT']
print motif.pssm    #changed automatically
motif.background = None    #default 0.25 for all
motif.background = 0.8    #interpreted as GC content c=g=0.8/2 a=t=1-0.8/2
print motif.pssm
#motif.pssm.distribution(background=motif.background)    # doesn't work or don't understand
print motif.background
print motif.pssm

#PWM and PSSM are recalculated on each call, to use them repeatedly use a variable
pssm = motif.pssm    #on every var call it's recalculated

#Comparing motifs
# motif boundaries are arbitrary, we can compare motifs of different lengths involving some alignment
# we must account:
#    alignment of motifs
#    function to compare aligned motifs
# for missing columns at the beginning and end of matrix we use the background distribution from the PSSM.
# Distance function returns the minimal distance between motifs, and offset alignment
#with open('REB1.pfm') as handle:
    #mtf_reb = motifs.read(handle, 'pfm')
##to be able to compare, both motifs must have the same pseudocounts and background distribution
#mtf_reb.counts = mtf.pseudocounts
#mtf_reb.pseudocounts = mtf.pseudocounts
## compare them using Pearson correlation
#distance, offset = motif.pssm.dist_pearson(mtf_reb.pssm)
#print distance, offset
##m:    bbTACGCbb    b:background distribution
##m_reb: GTTACCCGG

#De novo motif finding
#MEME
#to retrieve the motifs reported by MEME
with open('meme.txt') as handle:
    motifsM = motifs.parse(handle, 'meme')
#aditional info
print motifsM[0].consensus
instance0 = motifsM[0].instances[0]
print instance0.sequence_name, instance0.start, instance0.strand, instance0.pvalue

#AlignACE
#very similar with AlignACE program
#with open('alignace.out') as handle:
    #motifsA = motifs.parse(handle, 'alignace')    # motif format AlignACE
#print motifsA[0].consensus
