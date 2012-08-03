---
layout: templ
title: add_reflink
module: gtfutils
---
    Adds gene name and isoform annotations to a GTF file (refLink)
    
    This adds isoform and gene name annotations based upon the refLink table from
    the UCSC Genome Browser. This assumes that the GTF transcript_id is the same
    as the mrnaAcc field in the refLink table. Any transcripts with the same
    locuslink/gene id will be treated as isoforms of each other.
    
    This will add the following attributes:
        gene_name
        isoform_id (NCBI LocusLinkID/GeneID)
    
    Usage: gtfutils add_reflink filename.gtf reflink.txt
    
