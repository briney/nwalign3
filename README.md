# nwalign3  
  
Updated version of [nwalign](https://pypi.python.org/pypi/nwalign/?) with Python 3.x compatibility.  
  
### install  
`pip install nwalign3`  
  
### command-line usage  

Usage is essentially the same as the original nwalign package, with a few minor exceptions. As with the original package, a standard alignment can be accomplished with:  
```
$ nwalign3 alphabet alpet  
alphabet  
alp---et  
```  
  
Scoring matrices can be specified in one of two ways. First, by providing the full path to a matrix file:  
```
$ nwalign3 --matrix /path/to/matrices/BLOSUM62 EEAEE EEEEG  
EEAEE-  
EE-EEG  
```  
  
You can also provide the name of a built-in matrix (currently just PAM250 and BLOSUM62):  
```
$ nwalign3 --matrix BLOSUM62 EEAEE EEEG
EEAEE-
EE-EEG  
```  
  
As with the original package, match, gap_open and gap_extend scores can be provided:  
```
$ nwalign3 --gap_open -10 --gap_extend -4 --match 12 ASDFF ASFF  
ASDFF  
AS-FF  
```  
  
### python usage  
  
#### alignment
  
nwalign3 serves as essentially a drop-in replacement for nwalign:  
```
>>> import nwalign3 as nw  
>>> nw.global_align("CEELECANTH", "PELICAN", matrix='PAM250')  
('CEELE-CANTH', '-PEL-ICAN--')  
  
# with a specified penalty for open and extend.  
>>> nw.global_align("CEELECANTH", "PELICAN", gap_open=-10, gap_extend=-4, matrix='PAM250')  
('CEELECANTH', '-PELICAN--')  
```  
  
As with command-line usage, `matrix` may be either the full path to a matrix file or the name of a built-in matrix.  
  
#### scoring  
  
To get the score of an alignment (where the first two arguments are a pair of aligned sequences):  
```
>>> nw.score_alignment('CEELECANTH', '-PELICAN--', gap_open=-5,  
...                     gap_extend=-2, matrix='PAM250')  
11  
  
>>> nw.score_alignment('CEELE-CANTH', '-PEL-ICAN--', gap_open=-5,  
...                     gap_extend=-2, matrix='PAM250')  
6  
```  
  
