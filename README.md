# pubmed-search
Pubmed Fetch and Keyword Search

This program takes an input of Protein Data Bank ID's and finds their corresponding journal articles and searches these articles for user inputed keywords. Postive matches are outputted in a user-named new file with pubmed ID, keyword and the line the keyword was found. 

This program uses two programs from Github. 
1. Pubmed Batch Download
Batch download articles based on PMID (Pubmed ID)
2. PDF miner - specifically pdftotxt.py 
Converts PDF text content (though not images containing text) to plain text, html, xml or "tags".

INSTALLATION AND SETUP:

    Download the PDF Miner Program from https://github.com/euske/pdfminer and the Pubmed Fetch Program from https://github.com/billgreenwald/Pubmed-Batch-Download . Follow both program's instuctions for installation.         

 Files that must be in current directory:
  fullsearch.py - script that take PDB ids's and searches through corresponding journal articles for keywords
   
  pdfetch.rb: Ruby script that crawls the web using mechanize and downloads the pdf from the appropriate source
  pubmedid2pdf: Ruby script that acts as a wrapper for pdfetch.rb, calling it for each pubmed ID passed into the program from the terminal
  pdftotxt.py - Python script to convert pdf documents to text, html or xml format. Must be found in the pdfminer/tools directory and moved to your current working directory.        
  A list of pdb ID's - comma delimited.      
   
 Files created in search:
  pdf - Folder that the PDF's will be downloaded to
  textfiles_%s (ligand name) - Folder that text versions of journal articles will be downloaded to
  user named results file. 
   
USER EXPERIENCE:

The user is prompted for a ligand name and a list of pdbID's. The user must create a file within the pubmed fetch directory with the list of desired PDB id's comma separated. 

    EX: 1A0I, 1A48, 1A49, 1A4H, 1A5U, 1A6E, 1A82, 1A91, 1ABV, 1ACM, 1AGW, 1AH6

The program will parse these ID's, use the PDB database to find corresponding pubmed ID's, if available. Using pubmed ID's, the Pubmed Batch Download program will search various databases for available corresponding journal pdfs. These pdfs will be saved in a newly created folder "pdf". 

The program coverts these pdfs to textfiles and saves the texts in a new file "textfiles_('ligand name'). The user will be alerted to any text that was unable to be coverting - including pictures and graphics. 

The user is prompted to enter keywords separated by comma.
Ex: if desired keywords are 'binding affinity' 'binding pocket' 'alpha helix'
The input should be 
    $ Keywords: binding affinity, binding pocket, alpha helix

The user then specifies the name of a new file where results will be printed. 
  Example results:

    Pubmed ID: 56678986
        Keyword: binding affinity
        collection of terms that are believed to be important for the binding affinity, e.g., hydrogen bonds, 
    
        Keyword: bindng pocket 
        Residues in the Ligand-Binding Pocket of the Vitamin D Receptor
    
CONTRIBUTORS: 
Sydney Hutton
Rui Qui
Dr. Pengyu Ren
The University of Texas at Austin

Pubmed Batch Download - Edoardo "Dado" Marcora, Ph.D. This program uses an updated version of the wrapper written by bio-geeks. Updates were made by Bill Greenwald to allow the program to run under Ruby version 2.0.

PDF Miner - Copyright (c) 2004-2014 Yusuke Shinyama

Please direct all questions to shutton1@stanford.edu
