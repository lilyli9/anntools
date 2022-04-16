# driver.py
#
# Original code by: Vlad Makarov, Chris Yoon
# Original copyright (c) 2011, The Mount Sinai School of Medicine
# Available under BSD licence
#
# Modified code copyright (C) 2011-2019 Vas Vasiliadis
# University of Chicago
#
##
__author__ = 'Vas Vasiliadis <vas@uchicago.edu>'

import sys
import os
import file_utils as fu
import annotate as ann

def run(infile, job_id, format):

    print("Running . . .")

    ann.getSnpsFromDbSnp(vcf=infile, job_id=job_id, format='vcf', tmpextin='', 
        tmpextout='.1')
    print("dbSNP - done.")
    tmpextin = 1
    tmpextout = 2

    ann.getBigRefGene(vcf=infile, job_id=job_id, format='vcf', tmpextin='.' + str(tmpextin),
        tmpextout='.' + str(tmpextout))
    print("BigRefGene - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.getGenes(vcf=infile, job_id=job_id, format='vcf', table='refGene', 
        promoter_offset=500, tmpextin='.' + str(tmpextin), 
        tmpextout='.' + str(tmpextout))
    print("BigRefGene - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithCytoband(vcf=infile, job_id=job_id, format='vcf', table='cytoBand', 
        tmpextin='.' + str(tmpextin), tmpextout='.' + str(tmpextout))
    print("Cytoband - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithGadAll(vcf=infile, job_id=job_id, format='vcf', table='gadAll', 
        tmpextin='.' + str(tmpextin), tmpextout='.' + str(tmpextout))
    print("gadAll - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithGwasCatalog(vcf=infile, job_id=job_id, format='vcf', 
        table='gwasCatalog', tmpextin='.' + str(tmpextin), 
        tmpextout='.' + str(tmpextout))
    print("GwasCatalog - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithMiRNA(vcf=infile, job_id=job_id, format='vcf', table='targetScanS', 
        tmpextin='.' + str(tmpextin), tmpextout='.' + str(tmpextout))
    print("miRNA - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWitHUGOGeneNomenclature(vcf=infile, job_id=job_id, format='vcf', 
        table='hugo', tmpextin='.' + str(tmpextin), 
        tmpextout='.' + str(tmpextout))
    print("HUGO Gene Nomenclature Committee - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithCnvDatabase(vcf=infile, job_id=job_id, format='vcf', table='dgv_Cnv', 
        tmpextin='.' + str(tmpextin), tmpextout='.' + str(tmpextout))
    print("dgv_Cnv - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithCnvDatabase(vcf=infile, job_id=job_id, format='vcf', 
        table='abParts_IG_T_CelReceptors', tmpextin='.' + str(tmpextin), 
        tmpextout='.' + str(tmpextout))
    print("abParts_IG_T_CelReceptors - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithCnvDatabase(vcf=infile, job_id=job_id, format='vcf', 
        table='mcCarroll_Cnv', tmpextin='.' + str(tmpextin), 
        tmpextout='.' + str(tmpextout))
    print("mcCarroll_Cnv - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithCnvDatabase(vcf=infile, job_id=job_id, format='vcf', 
        table='conrad_Cnv', tmpextin='.' + str(tmpextin), 
        tmpextout='.' + str(tmpextout))
    print("conrad_Cnv - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithGenomicSuperDups(vcf=infile, job_id=job_id, format='vcf', 
        table='genomicSuperDups', tmpextin='.' + str(tmpextin),
        tmpextout='.' + str(tmpextout))
    print("genomicSuperDups - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ann.addOverlapWithTfbsConsSites(vcf=infile, job_id=job_id, table='tfbsConsSites',
        tmpextin='.' + str(tmpextin), tmpextout='.' + str(tmpextout))
    print("addOverlapWithTfbsConsSites - done.")
    tmpextin = tmpextin + 1
    tmpextout = tmpextout + 1

    ## Cleanup
    for i in range(1, tmpextin):
        fu.delete(infile + '.' + job_id + '.' + str(i))

    os.rename(infile + '.' + job_id + '.' + str(tmpextin), infile + '.' + job_id + '.annot')
    tempout=(infile + '.' + job_id + '.annot').replace(f'.vcf.{job_id}', f'.{job_id}.vcf').replace('.vcf.annot', '.annot.vcf')
    os.rename(infile + '.' + job_id + '.annot', tempout)

    templogout=(infile + '.' + job_id + '.count.log').replace(f'.vcf.{job_id}', f'.{job_id}.vcf')
    os.rename(infile + '.' + job_id + '.count.log', templogout)

### EOF