---
layout: templ
title: fromgff
module: gtfutils
---
    
    Converts a GFF annotation file to GTF, concentrating on the data elements
    that are important for gene annotations (gene, exons, CDS, etc). It will also
    propertly calculate the transcripts (mRNA) for each gene.
    
    Genes, pseudogenes, mRNA, ncRNA, rRNA, snoRNA, snRNA, and tRNAs are all processed.
    
    The output file by default exports "exon" and "CDS" features. Gene and transcript
    features can be exported with the proper arguments.
    
    The input GFF must contain "ID", "Name", and "Parent" attributes.
    
    If there is DNA sequence appended to the end of the file, it must be indicated
    with a ##FASTA tag or the sequence must be in FASTA format.
    
    
    Usage: gtfutils fromgff {options} filename.gff
    
    Options:
      -rnas            Export RNA features
      -genes           Export gene features
      -err filename    Write lines that couldn't be processed to this file
    
