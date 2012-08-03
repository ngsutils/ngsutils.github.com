---
layout: templ
title: tobed
module: gtfutils
---
    
    Convert a GFF/GTF file to BED format
    
    This will convert whole genes, individual exons, or expressed regions.
    Expressed regions are distinct sections of exons that take into account
    alternative splicing, such that each region is assigned to be 'constant' or
    'alternative'.
    
    Usage: gtfutils tobed [-genes|-exons|-regions] filename.gtf{.gz}
    You must select "-exons" or "-genes" or "-regions"
    
    
    Convert a GFF/GTF file to BED format
    
    This will convert whole genes, individual exons, or expressed regions.
    Expressed regions are distinct sections of exons that take into account
    alternative splicing, such that each region is assigned to be 'constant' or
    'alternative'.
    
    Usage: gtfutils tobed [-genes|-exons|-regions] filename.gtf{.gz}
    
