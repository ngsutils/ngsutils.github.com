---
layout: templ
title: extract
module: bamutils
---
    
    Extracts reads based on regions in a BED file
    
    Given a BAM file and a BED file, this script will extract only reads that
    map to the given BED regions.
    
    Specifically, if a read starts or ends within a BED region, it is extracted.
    However, if a read completely spans a region (starting before and ending
    after), it is ignored. If the read "touches" the region at all, it is
    extracted.
    
    This tends to be faster than running 'bamutils filter' because this extracts
    reads from a region, without iterating over all of the reads in the BAM file.
    But, if you are already filtering the BAM file for other criteria, it is
    probably worth it to just to the filtering with your other criteria.
    
    
    Usage: bamutils extract {opts} in.bam out.bam regions.bed
    
    Options:
      -ns    Ignore strandedness of reads and regions
    
    
