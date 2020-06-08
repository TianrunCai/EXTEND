# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:01:16 2020

@author: AustinMain
"""
from ExtEND import cleanreport
from ExtEND import report_process
variablelist=['EF','Sat','BP',]

def test():
    res=[]
    rpt = """
              =857-307-1300       Name:        PAUL CLOUTIER      Sex: M         12/14/2011  MRN:         23919103        
                  ecog: zero
                Diagnosis: Congestive heart failure-428.0     Indications: CHF.          Location: Shapiro Outpatient Lab.       
                Study Details:Complete Echo (2D, Color, Doppler) - 93306. The patient was   awake.     2D:    Measurements:    
                    IVS, d 0.9 cm        RWT         
                    EF: 54%
                    BP:154/89 ef: 34-54
                    Sat: 98% on RA
                    98 23 81 98% on ra 
                    0.4  LV, d  6.4 cm        LV Mass (AL)   302 g  LV, s  4.8 cm        
                    LV Mass (BSA)  116 g/m?  LVPW   1.2 cm        Aortic Root, d 3.3 cm  LA, s  5.0 cm     
                   

"""            
                #filteredreport = filter_content(row[3])
    tokenizednote=cleanreport.get_report_by_list(rpt)
    value=report_process.process(tokenizednote,variablelist)
    if value !=[]:#
        value1='|'.join(['|'.join(line) for line in value])
        print (value)
        res.append(value1)
    #print (res)
test()
    