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
    
    Usage: gtfutils tobed [type] filename.gtf{.gz}
    
    Where type is one of:
        -genes    The gene from start to end (including introns)
        -exons    Each annotated exon
        -regions  Export constant / alternative regions (annotated splice regions)
        -tss      Transcription start sites (unique)
        -tlss     Translational start sites (unique start codons)
    
    
    
