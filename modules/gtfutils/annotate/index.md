---
layout: templ
title: annotate
module: gtfutils
---
    Annotates genomic positions based on a GTF model
    
    For a given input tab-delimited text file with a valid reference and position column,
    this script will add columns for the gene name and intron/exon/utr/intragenic position
    within the gene (if the position maps to a gene).
    
    Column counts start at 1.
    
    Usage: gtfutils annotate {options} filename.gtf{.gz} input.txt
    
    Options:
        -ref num        Column with reference (default: 1)
        -pos num        Column with pos (1-based) (default: 2)
    
        -gene_id        Output gene_id (from GTF file)
        -transcript_id  Output transcript_id (from GTF file)
        -gene_name      Output gene_name (from GTF file)
        -gene_location  Output gene location (exon, inton, etc)
    
        -noheader       The first line is not a header (default: True)
    
    
