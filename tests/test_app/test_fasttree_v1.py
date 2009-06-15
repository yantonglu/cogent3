#!/usr/bin/env python
"""Tests for FastTree v1.0.0 application controller"""

from shutil import rmtree
from os import getcwd
from cogent.util.unit_test import TestCase, main
from cogent.app.fasttree_v1 import FastTree, build_tree_from_alignment
from cogent.core.alignment import Alignment
from cogent.parse.fasta import MinimalFastaParser
from cogent.parse.tree import DndParser
from cogent.core.moltype import DNA

__author__ = "Daniel McDonald"
__copyright__ = "Copyright 2007-2008, The Cogent Project"
__credits__ = ["Daniel McDonald"]
__license__ = "GPL"
__version__ = "1.4.0.dev"
__maintainer__ = "Daniel McDonald"
__email__ = "mcdonadt@colorado.edu"
__status__ = "Development"

class FastTreeTests(TestCase):
    def setUp(self):
        self.seqs = Alignment(dict(MinimalFastaParser(test_seqs.split())))
    
    def test_base_command(self):
        app = FastTree()
        self.assertEqual(app.BaseCommand, \
                         ''.join(['cd "',getcwd(),'/"; ','FastTree']))
        app.Parameters['-nt'].on()
        self.assertEqual(app.BaseCommand, \
                         ''.join(['cd "',getcwd(),'/"; ','FastTree -nt']))

    def test_change_working_dir(self):
        app = FastTree(WorkingDir='/tmp/FastTreeTest')
        self.assertEqual(app.BaseCommand, \
                       ''.join(['cd "','/tmp/FastTreeTest','/"; ','FastTree']))
        rmtree('/tmp/FastTreeTest')

    def test_build_tree_from_alignment(self):
        tree = build_tree_from_alignment(self.seqs, DNA)
        for o,e in zip(tree.traverse(), DndParser(exp_tree).traverse()):
            self.assertEqual(o.Name,e.Name)
            self.assertFloatEqual(o.Length,e.Length)

test_seqs = """>test_set1_0
GGTAGATGGGACTACCTCATGACATGAAACTGCAGTCTGTTCTTTTATAGAAGCTTCATACTTGGAGATGTATACTATTA
CTTAGGACTATGGAGGTATA
>test_set1_1
GGTTGATGGGACTACGTAGTGACATGAAATTGCAGTCTGTGCTTTTATAGAAGTTTGATACTTGGAGCTCTCTACTATTA
CTTAGGACTATGGAGGTATA
>test_set1_2
GGTTGATGGGCCTACCTCATGACAATAAACTGAAGTCTGTGCTTTTATAGAGGCTTGATACTTGGAGCTCTATACTATTA
CTTAGGATTATGGAGGTCTA
>test_set1_3
GGTTGATGGGACTACCTCATGACATGAAACTGCAGTCTGTGCTTTTATAGAAGCTTGATACTTGGAGATCTATACTATTA
CTTAGGACTATGGAGGTCAC
>test_set1_4
GGTTGGTGGGACTACCTCATGACATGAAGATGCAGTCTGTGCTTGTATAGAAGCTTGAAACTTGGATATCTATACTATTA
CTTAAGACTATGGAGGTCTA
>test_set1_5
GGTTGATGCGACTACCTCATGACATGAGACTGCAGTCTGTGCTTTTACTGAAGCTTGATACTTGGAGATCTATACTATTA
CTTAGGACTATGGAGGTTTA
>test_set1_6
GGTTGATGGGACTACCTCATGACATGAAAATGCAGTCTGTCCTTTTATAGAAGCTTGATACTTGTAGATCTATACTGTTA
CTTAGGACTATGGAGGTCTA
>test_set1_7
GGTTGATGGGACTCCCTCATGACATAAAACTGCAGTCTGTGCTTTTACAGAAGCTTGATACTTGGAGATCTATACTATTA
CATAGGACTATGGAGGTCTA
>test_set1_8
GGTTGATGGCACTACCTCATGAGATGAAACTGCAGTCTGTGCTTTTATAGAAGCTTGATACTTGGATATCTATACTATAA
CTTAGTACTATGGAGGCCTA
>test_set1_9
GGTTTATGTTACTACCTCATGACATGAAACGGCAGCATGTGCTTTTATAGAAGCTTGATACTTGGAGATCTAAACTATTA
CTTAGGACTATGGAGGTCTA
>test_set2_0
AGCGAATCATACTCTGGAAAGAAAAGGACGACTCCTTTGCTCGCGGTCTAGCTGCTACAGCTTCACCGAGTACATCTGAA
TGATGGTTGAACCGGGTTCA
>test_set2_1
AGAGAATAGTACTCTGGAAAGACAAGGACGACTCCTTTGATCGCGGTCTAGCTGCTACAGCTTCACCGAGTACATCTGAA
TGATGGTTGAACCGGATTCA
>test_set2_2
AGAGTATAATACTCTGGAAAGAAAAGGACGACTCCTTTGATCGCGGTCTAGCTGCTACAGCTTCACCGAGTACATCTTAA
TGATGGTTGAACCGGGGTCA
>test_set2_3
AGAGAATCATACTCTGGAAAGAAATGGACGACTCCTTTGATCGCGGTCCAGCTGCTACAGCTTCACCGAGTACATCTGAA
TGATGGTTGGACCGGGTTCA
>test_set2_4
AGAGAATAATAGTCTGGAAAGAAAAGGACGACTCCTTTGTTCCCGGTCTAGCTGCTACAGCTTCCCCGAGTACATCTGAA
TGATGGTTGAACCGGGTTCA
>test_set2_5
ACAGAATACTACTCTGGAAAGAAAAGGCCGACTCCTTTGATCGCTGTCTAGCTGCGACAGCTGCACGGAGTCCATCCGAA
TGATGGTTGAACCGGGTTCA
>test_set2_6
AGAGAATAATACTCTGGACAGAAATGGACGACTCCTTTGATCGCGGTCTAGCTGCTACAGCTTCACCGAGTACATCTGAA
TGATGGCTGAACCGGGTTCA
>test_set2_7
AGAGAATATTACTCTGGAAAGAAAAGGACGACTCCTTGGATCGCGGTCTAGCTGCTACAGCTTCAGCGAGTACATCGGAA
TGATGGTTTAACCGGGTTCA
>test_set2_8
AGTGAATAATACTCTGGAAAGAAAAGGACGACTCCTTTGATCGCGGTCTAGCTGCTAGAGCTTCACCGAGTACATCTGAA
TGATGGTTGAACCGGGTTCA
>test_set2_9
AGAGATTAATACTCTGGATAGAAAATGACGACTCCTTTGATCGCGGTCTAGCTGCTACAGATTGACCTATTACATCTGAA
TGATGGTTGAACCGGGTTCA
>test_set3_0
TTGTCTCCATTGAGCACTCTAATCTTGCCGTGTATTCAGGAAAGGAGGATAGAACTCGGACAGTATTCTGAACATTACAG
AATCGCCGTATTTACGGTGT
>test_set3_1
TTGTCTCCATTGAGCACTCTAATCATGCCGTGTATTCAGGAACGGAGGAGAGGACTCGGTCAGTATTCGGAACATTACAG
AATGGCGTTATTTACGGTGT
>test_set3_2
TTGTCTCCATTGAGCACTCTAATCTTGCCGTGTATTCAGGAACGGAGGATAGAACTCGGACAGAATCCTGAATATTACAA
AATCGGGTTATTTACGGTGT
>test_set3_3
TTGTCTCCATTGAGCACTCTAATCTTGCCGTGTTTTCAGGAACGGAGGATAGAACTCGGACAGTAGCCTGAACATTACAG
AATCCCGTTATTTACGGTGT
>test_set3_4
TTGTCTCCATCGAGCACTCTAATCTTGCCGTGTATTCAGGAACGGAGGATTGAACTCGGACAGTATCCTGAACATTACAG
AATCGCGTTATTTACGGTGT
>test_set3_5
TTGTCTCCATTGAGCACGCTAAGCTTGCCGTGTATTCAGGAACGGAGGATAGAACTCGGACAGTATCCTGAACATTACAG
AATCGCGTTATTTACGGTGT
>test_set3_6
TTGTCGTCATTGAGCACTCTAATCTTGCCGTGTATTCAGGAACGAAGGATAGAACTCGGACAGTATCCTGAACTTTGCAA
AATCGCGTTATTTACGGTGT
>test_set3_7
TTGTCTCCATTGAGCACTCTAATCTAGCCGTGTAGTCAGGAACGGAGGATGGAACGCGCACAGTATCCTGAACATAACAG
AATCGCGTTATTTACGGTGT
>test_set3_8
TTGTCTCCATTGAGCACTCTAATCTTGCCGTATATTCCCGAACGGAGGATAGAACTCGGACAGTAGCCTGAACAGTACAG
AATCGCGTTATTTACGGTGT
>test_set3_9
TTGTCTCCCTTGAGCACTCTAATCTTGCCGTGTATTCAGGAACGGAGGATAGAACTCGGACAGTATCCTGAACATTACAG
AATCGCGTTATTTACGGTGT
>test_set4_0
CTTTTACCGGGCTGCCCGAGAGCACTATCTGCGTCGTGCCCTGCTTCGATGCCCACACTACCATCATACTATTCGTGAAT
TTGCGGCCGCTAAGATCCGA
>test_set4_1
CTTTTATCGGGGTGCCTGATAGCACCATCTGCGTCGTGCCCTGCTTCGATGCCTAAACCACCGTCATGCTATTTGTGAAT
TTGAGGTCGCTAAGAGCCCA
>test_set4_2
CTTTTATCGGGGTGCCCGAGAGCACCATCTGCGTCGTGCCCTGCTTCGATGCCCAGGCCACCATCATACTATTTGTGGCT
TAGGGGTCGCTAAGAGCCGA
>test_set4_3
CTTTTATCGGGGGGCCCGAGAGCACCACCTGCGTCGTGCCCTGCTTCGATGCCCAAACCACCATCATACTATTTGTGAAT
TTGGGGTCGCTAAGAGCCGA
>test_set4_4
CTTTTATAGGGGTGCCCGAGAGCACCATCTGCGTCGTGCCCAGCTTCGATTTCCAAACCACCATCATACTATTTGTGAAC
TTGGGGACGTTAAGAGCCGA
>test_set4_5
CTTTTCGCGGGGTGCCCGAGAGCACCATCTGCGTCGCGCCCTGCTTCGGTGCCCATACCACCATCATAATATTTGGGAAA
TTGGGATCGCTAAGAGTCGA
>test_set4_6
CTTTTCTCGGGGTGCCCGAGAGCCCCATCTGCGTTGTGCCCTGCTACTATGCCCAAACCACCATCATACTATTTGTGAAT
GTGGCGTCGCTCAGAGCCGA
>test_set4_7
CTTTTATCGGGGTGCCCGAGAGCACCATCTGCGTCGTGCCCTGCTTCGATGCCCACGTCACCATACTACTATTTGTGAAT
TTGGGGTCGCTAATAGCCGA
>test_set4_8
CTTTTATCGGGGGGCCCGAGAGCATCATCTGCGTCGTGCCCTGCTTCGATGCCCAAACTACCATCATACTATTTGTGAAT
TTGGGGTTTCTAAGAGCCGA
>test_set4_9
CTTTTACCGGGGTGACCGAGAGCACCATCTGCGCCGTGCCCTGCTTCGAGGCCCAAACCACCATCATACTGTTTGTGAAT
CAGGGGTTGCTAAGAGCCGA"""

exp_tree = """(test_set1_3:0.02062,(test_set1_8:0.05983,test_set1_9:0.07093)0.652:0.00422,((test_set1_5:0.04140,test_set1_7:0.03208)0.634:0.00995,((test_set1_0:0.04748,(test_set1_1:0.07025,(test_set1_2:-0.00367,((((((test_set3_4:0.01485,test_set3_7:0.05863)0.862:0.00569,(test_set3_5:0.02048,(test_set3_3:0.02036,test_set3_8:0.04218)0.724:0.01088)0.397:0.00005)0.519:0.00018,((test_set3_0:0.03139,test_set3_1:0.06448)0.699:0.01095,test_set3_9:0.00940)0.505:0.00036)0.721:0.01080,test_set3_6:0.05333)0.808:0.16470,test_set3_2:-0.12547)1.000:1.42295,((test_set4_1:-0.24707,((test_set4_3:0.00903,test_set4_8:0.04272)0.650:0.00955,(test_set4_4:0.07633,((test_set4_5:0.09853,test_set4_6:0.08143)0.577:0.00748,((test_set4_0:0.08822,test_set4_9:0.07914)0.371:0.00130,(test_set4_2:0.03477,test_set4_7:0.04983)0.764:0.01228)0.665:0.00370)0.535:0.00147)0.633:0.00116)0.850:0.32065)0.998:1.45908,(((test_set2_2:0.03125,((test_set2_8:0.01770,(test_set2_0:0.02172,test_set2_4:0.04082)0.482:0.00228)0.575:0.00249,(test_set2_9:0.07291,(test_set2_3:0.03201,test_set2_6:0.01973)0.538:0.00746)0.690:0.00319)0.746:0.00073)0.788:0.00569,(test_set2_5:0.08827,test_set2_7:0.04250)0.717:0.00533)0.504:0.04532,test_set2_1:-0.01642)0.997:1.14023)0.625:0.41298)0.822:0.20836)0.783:0.07781)0.487:0.00591)0.469:0.00151,(test_set1_4:0.06606,test_set1_6:0.02981)0.703:0.00956)0.560:0.00216)0.468:0.00050);"""

if __name__ == '__main__':
    main()
