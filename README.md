# EXTEND
EXTraction of EMR Numerical Data
EXTEND (Extraction of EMR Numerical Data) is a versatile, rule-based tool designed for efficient extraction of clinical numeric parameters with exceptional accuracy. Through the expansion of its dictionary and the creation of new rules, EXTEND can be readily adapted to extract additional numerical data crucial for clinical outcomes research. --

Publication: https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-019-0970-1

The installation procedures have been verified in a Python 3.7, 64-bit environment on both Windows 10 and Windows Server 2016. 

Installation steps:
1. Create a system environment variable "ENTEND_HOME", set a desired path of the EXTEND main folder as the value.
2. Download and unzip the EXTEND folder.
3. In a command line window, change the directory to folder 'EXTEND-master'.
4. run "python setup.py install".
5. In order to perform data extraction, please select some of variables below to run (Note: it's case sensitive)
6.   ['EF','BMI','H','W','RR','T','BP','HR','Sat']
7. E.g. for extracting EF and BMI, we can use ['EF', 'BMI']
7.      HR: Heart Rate
8.      EF: Ejection Fraction
9.      Sat: Oxygen Saturation
10.     H: Height                                     
11.     W: Weight                                     
12.     RR: Respiratory Rate
13.     T: Temperature
