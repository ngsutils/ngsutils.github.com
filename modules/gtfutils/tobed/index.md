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
        -introns  Each annotated intron
        -regions  Export constant / alternative regions (annotated spliced regions)
        -tss      Transcription start sites (unique)
        -txs      Transcription stop sites (unique)
        -tlss     Translational start sites (unique start codons)
        -tlxs     Translational stop sites (unique stop codons)
        -junc_5   Splice junction 5' donor
        -junc_3   Splice junction 3' acceptor
    
    
    
    
