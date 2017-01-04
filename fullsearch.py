#!/usr/bin/env python
import os,sys
import urllib.request
import xml.etree.ElementTree as ET
import shutil


def moveFiles():
    curdir = os.getcwd()   
    filename = '/' + 'textfiles_' + ligand
    newpath = curdir + filename 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    else:
        for f in os.listdir(newpath):
            os.remove(f)        
    for i in os.listdir(curdir):
        i = i.strip()
        end = '.txt'
        if i.endswith(end):
            shutil.move(i, newpath)
            continue
        else:
            continue

def fetchPMids(PDBlist, pmIDs):
    pdbfile = input('List of pdb ID file: ')
    f = open(pdbfile, 'r')
    for line in f:
        IDs = line.split(", ")
        for i in IDs:
            i = i.rstrip()
            PDBlist.append(i)
    for i in PDBlist:
        ID = i.strip()
        with urllib.request.urlopen('http://www.rcsb.org/pdb/rest/customReport.xml?pdbids=%s&customReportColumns=structureId,releaseDate,structureAuthor,pubmedId,doi&primaryOnly=1'%str(ID)) as response:
            tree = ET.parse(response)
            root = tree.getroot()
            try:
                pmID = root[0][3].text
            except IndexError:
                pmId = 'null'
            if pmID != 'null':            
                pmIDs.append(pmID)
                continue
            else:
                continue         
                
            
def getFile(pmIDs):
    for i in pmIDs:
        os.system("ruby pubmedid2pdf.rb %s" % (str(i))) 
    for f in os.listdir(os.getcwd() + '/pdf'):
        if f.endswith(".pdf"):
            f = f[:-4]
            os.system("python pdf2txt.py -o %s.txt -t text pdf/%s.pdf" % (str(f), str(f)))
    moveFiles()
    
def searchFiles(pdfdir, textdir, ligand):
    newFile = input('Save info to new file: ')
    fnew = open(newFile, 'w')
    curdir = os.getcwd()   
    filename = '/' + 'keyword_files_' + ligand
    newpath = curdir + filename 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    string_input = input('Keywords (Separate by ,): ')
    keywords = string_input.split(',') 
    keywords = [str(a) for a in keywords] 
    d = dict()
    for i in os.listdir(os.getcwd() + '/' + textdir):
        ID = i[:-4]
        f1 = open(textdir + "/%s.txt" % (str(ID)), 'r')
        for line in f1:
            for word in keywords:
                if word in line:
                    if ID not in d:
                        d[ID] = 1
                    else :
                        d[ID] = d[ID] + 1
        f1.close()
    inv_d = {v: k for k, v in d.items()}
    ordered = d.keys()
    ordered.sort(reverse=True)
    for txt in ordered:
        d[txt] = ID
        f1 = open(textdir + "/%s.txt" % (str(ID)), 'r')
        for line in f1:
            for word in keywords:
                if word in line:
                    if found:
                        fnew.write('Pubmed ID: ' + ID + os.linesep)                        
                        found = False
                    fnew.write('\t Keyword: ' + word  + os.linesep)
                    fnew.write('\t' + line + os.linesep) 
                    break
        fnew.write('\n' + os.linesep) 
        f1.close()
        if not found:
            i = i.strip()
            shutil.move(pdfdir + '/' + ID + '.pdf', newpath)
    print('Results in ' + newFile)

        
if __name__ == '__main__':
    pmIDs = []
    PDBlist = []
    ligand = input('Ligand name: ')
    fetchPMids(PDBlist, pmIDs)
    getFile(pmIDs)
    pdfdir = 'pdf'
    textdir = 'textfiles_' + ligand
    searchFiles(pdfdir, textdir, ligand)
   
    
    