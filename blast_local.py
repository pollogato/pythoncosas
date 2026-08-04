# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 19:33:14 2023

@author: Pablo
"""
#para windows tuve que usar subprocess
import subprocess
from Bio.Blast.Applications import NcbiblastnCommandline


#Ubicación blastn o ejecutable de la consola para blastn
PATH_BLASTn = r""

### query quiero ver si está en subject ###
NOMBRES_SUBJECT = ['']
NOMBRES_QUERY = ['']

e_value = 1e-50
perc_iden = 1
perc_cover = 90

def blastn(SUBJECT,QUERY,salida):
    blastn_path = PATH_BLASTn
    result = salida 
    sub = SUBJECT
    q = QUERY

    blastn_cline = NcbiblastnCommandline(
        cmd=blastn_path, query=q, subject=sub, evalue=e_value, 
        perc_identity=perc_iden, qcov_hsp_perc=perc_cover,
        outfmt=6, out=result)
    
    # blastn_cline
    # print(blastn_cline)

    subprocess.run(str(blastn_cline))

for i in NOMBRES_SUBJECT:    
    for j in NOMBRES_QUERY:       
        s = "Resultado_"+j+"_in_"+i+".xml"
        blastn(i,j,s)




