---
layout: templ
title: add_isoform
module: gtf
---
    Adds isoform annotations to a GTF file (isoforms)
    
    This adds isoform annotations based upon the KnownGene annotations from the
    UCSC Genome Browser. Isoforms are taken from the knownIsoform table. This
    table must be downloaded from the UCSC Genome Browser.
    
    The isoforms file should be in the following format:
    
    isoform_id {tab} transcript_id
    
    Where all transcripts that are isoforms of the same gene will have the same
    isoform_id value.
    
    This will add the following attributes:
        isoform_id (isoform cluster id)
    
    Usage: gtfutils add_isoform filename.gtf knownIsoform.txt
    
