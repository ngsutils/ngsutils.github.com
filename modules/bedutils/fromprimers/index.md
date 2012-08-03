---
layout: templ
title: fromprimers
module: bed
---
    
    Converts a list of PCR primer pairs to BED regions
    
    Given a genomic FASTA file and a list of primers,  this will generate a new
    FASTA file for the targeted region.  This targeted FASTA file can then be
    used for targeted resequencing.
    
    PCR input is expected to be paired FASTA entries with names like:
    >primername/1
    atatcgtgctacgatc
    >primername/2
    ttgatcggcatataaa
    
    Tab-delimited input should be:
    fwd-primer {tab} rev-primer
    
    Uses http://genome.ucsc.edu/cgi-bin/hgPcr to perform ePCR.
    
    Note: This operates by screen scraping,  so it may break unexpectedly in the
    future.
    
    Usage: bedutils fromprimers {opts} -fasta file.fa
           bedutils fromprimers {opts} -tab file.txt
           bedutils fromprimers {opts} fwd_primer rev_primer
    
    Options:
    -db         name    DB to use
    -perfect    bases   Minimum perfect bases (default: 15)
    -good       bases   Minimum good bases (default: 15)
    -size       bases   Max product size (default: 4000)
    -flip               Flip the reverse primer (default: False)
    
    
    
