# EXTEND
EXTraction of EMR Numerical Data
EXTEND is an efficient, flexible and rule-based tool to extract clinical numeric parameters with high accuracy. By expanding the dictionary and developing new rules, the usage of EXTEND can be easily expanded to extract additional numerical data important in clinical outcomes research. --

Publication: https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-019-0970-1

The installation steps have been tested in Python 3.7 environment on windows 10, windows server 2016. 

Installation steps:
1. Create a system environment variable "ENTEND_HOME", set a desired path of the EXTEND main folder as the value.
2. Download and unzip the EXTEND folder.
3. In a command line window, change the directory to folder 'EXTEND-master'.
4. run "python setup.py install".
5. In order to perform data extraction, please select some of variables below to run (Note: it's case sensitive)
6.   ['ECOG','EF','BMI','H','W','RR','T','BP','HR','Sat','PDL1','Crn','Hba1c']
7. E.g. for extracting EF and BMI, we can use ['EF', 'BMI']
7.      ECOG:Eastern Cooperative Oncology Group;      HR: Heart Rate
8.      EF: Ejection Fraction                         Sat: Oxygen Saturation
9.      BMI: Body Mass Index                          PDL1: Programmed death-ligand 1 
10.     H: Height                                     Crn: Creatinine
11.     W: Weight                                     Hba1c: Hemoglobin A1c
12.     RR: Respiratory Rate                          T: Temperature
