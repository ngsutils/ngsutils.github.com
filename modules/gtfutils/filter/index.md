---
layout: templ
title: filter
module: gtfutils
---
    
    Filter annotations from a GTF file.
    
    Usage: gtfutils filter {filters} filename.gtf
    
    Possible filters:
        -chr str    Remove annotations from chromosomes with 'str' in the name
        
        -to-ucsc    Rename Ensembl-style chromosome names (1, 2, etc) to 
                    UCSC/NCBI-style names (chr1, chr2, etc.) 
                    
                    (This will keep only chromosomes 1-22, X, Y, and MT for Human)
    
    
    
