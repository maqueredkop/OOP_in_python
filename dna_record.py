#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 21:15:37 2017

@author: maque
"""
####################################################################################
# Please note that all the demo code is from the book 'Advanced python for biologists'
# by Martin Jones
####################################################################################


class DNARecord(object):
    sequence = 'ACGCGTAGTCGT'
    gene_name = 'ABC1'
    species_name = 'Drosophila'
    
    def complement(self):
        replacement1 = self.sequence.replace('A','t')
        replacement2 = replacement1.replace('T','a')
        replacement3 = replacement2.replace('C','g')
        replacement4 = replacement3.replace('G','c')
        return replacement4.upper()
    
    def get_AT(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_content = (a_count + t_count) / length
        return at_content
    
d = DNARecord()
print('Created a record for ' + d.gene_name + ' from ' + d.species_name)
print('AT is ' + str(d.get_AT()))
print('complement is ' + d.complement())


#########################################
## set variable

class DNARecord(object):
    #sequence = 'ACGCGTAGTCGT'
    #gene_name = 'ABC1'
    #species_name = 'Drosophila'
    
    def complement(self):
        replacement1 = self.sequence.replace('A','t')
        replacement2 = replacement1.replace('T','a')
        replacement3 = replacement2.replace('C','g')
        replacement4 = replacement3.replace('G','c')
        return replacement4.upper()
    
    def get_AT(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_content = (a_count + t_count) / length
        return at_content
    
    def set_variables(self,new_seq,new_gene_name,new_species_name):
        self.sequence = new_seq
        self.gene_name = new_gene_name
        self.species_name = new_species_name
        
d1 = DNARecord()
d1.set_variables('ATCGTAGT','COX1','Homo sapiens')

print(d1.sequence)
print(d1.gene_name)
print(d1.get_AT())
print(d1.complement())


###################################################################
## constructor

class DNARecord(object):

    def __init__(self,sequence,gene_name,species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name
        
    def complement(self):
        replacement1 = self.sequence.replace('A','t')
        replacement2 = replacement1.replace('T','a')
        replacement3 = replacement2.replace('C','g')
        replacement4 = replacement3.replace('G','c')
        return replacement4.upper()
    
    def get_AT(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_content = (a_count + t_count) / length
        return at_content
    
d1 = DNARecord('TCGAGGTACGT','COX1','Homo sapiens')
print(d1.complement())

#############################################################
## inhertance

class SequenceRecord(object):
    
    def __init__(self,sequence,gene_name,species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name   
        
    def get_fasta(self):
        safe_species_name = self.species_name.replace(' ','_')
        header = '>' + self.gene_name + '_' + safe_species_name
        return header + '\n' + self.sequence + '\n'
    

class ProteinRecord(SequenceRecord):
    
    def get_hydrophobic(self):
        aa_list = ['A','I','L','M','F','W','Y','V']
        protein_lenth = len(self.sequence)
        total = 0
        for aa in aa_list:
            aa = aa.upper()
            aa_count = self.sequence.count(aa)
            total =total + aa_count
        return total * 100 / protein_lenth
    
class DNARecord(SequenceRecord):
    
    def complement(self):
        replacement1 = self.sequence.replace('A','t')
        replacement2 = replacement1.replace('T','a')
        replacement3 = replacement2.replace('C','g')
        replacement4 = replacement3.replace('G','c')
        return replacement4.upper()
    
    def get_AT(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_content = (a_count + t_count) / length
        return at_content
    

p1 = ProteinRecord('MSRSLLLRFLLFLLLLPPLP', 'COX1', 'Homo sapiens') 
print(p1.get_fasta())
print(p1.gene_name)
print(p1.get_hydrophobic())

d1 = DNARecord('TCGAGGTACGT','COX1','Homo sapiens')
print(d1.get_fasta())
print(d1.complement())

##############################################################
## overriding 

class DNARecord(SequenceRecord):
    
    def __init__(self,sequence,gene_name,species_name,genetic_code):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name
        self.genetic_code = genetic_code
        
    def complement(self):
        replacement1 = self.sequence.replace('A','t')
        replacement2 = replacement1.replace('T','a')
        replacement3 = replacement2.replace('C','g')
        replacement4 = replacement3.replace('G','c')
        return replacement4.upper()
    
    def get_AT(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_content = (a_count + t_count) / length
        return at_content
    
d1 = DNARecord('ATCGCGTACGTGATCGTAG', 'COX1', 'Homo sapiens', 5) 


####################################################################
## calling superclass

class SequenceRecord(object):
    
    def __init__(self,sequence,gene_name,species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name   
        
    def get_fasta(self):
        safe_species_name = self.species_name.replace(' ','_')
        header = '>' + self.gene_name + '_' + safe_species_name
        return header + '\n' + self.sequence + '\n'
    

class DNARecord(SequenceRecord):
    
    def __init__(self,sequence,gene_name,species_name,genetic_code):
        SequenceRecord.__init__(self,sequence,gene_name,species_name)
        self.genetic_code = genetic_code
        
    def complement(self):
        replacement1 = self.sequence.replace('A','t')
        replacement2 = replacement1.replace('T','a')
        replacement3 = replacement2.replace('C','g')
        replacement4 = replacement3.replace('G','c')
        return replacement4.upper()
    
    def get_AT(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_content = (a_count + t_count) / length
        return at_content
    
d1 = DNARecord('ATCGCGTACGTGATCGTAG', 'COX1', 'Homo sapiens', 5) 

