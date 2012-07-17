---
layout: templ
title: add_xref
module: gtfutils
---
    Adds gene name annotations to a GTF file (xref)
    
    This adds gene name annotations based upon the KnownGene annotations from the
    UCSC Genome Browser. Gene names will be taken from the kgXref table. This
    table must be downloaded separately from the UCSC Genome Browser.
    
    This assumes that the file will be in tab-delimited format and that there is
    one line for each transcript. You may specify which column represents the gene
    name. In the standard "kgXref.txt" file, this is column #5.
    
    This will add the following attributes:
        gene_name
    
    Usage: gtfutils add_xref {-col num} filename.gtf kgXref.txt
    
    Options:
      -col num    The gene name is stored in column {num} (1-based)
                  (default:5)
    
    
