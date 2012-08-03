---
layout: templ
title: convertregion
module: bam
---
    
    Converts region mapping to genomic mapping
    
    This takes a BAM file that has been mapped to a genomic region and converts
    the mapping to genomic coordinates.  This can be used to convert reads mapped
    against a junction library or targeted resequencing back to genomic
    coordinates.  The names of the reference sequences should be named:
    chrom:start-end (0-based start).  If there are gaps (junctions), they should
    be named: chrom:start-end,start-end,etc...
    
    In this is the case, this script will ensure the proper conversion of
    reference, start position, and CIGAR alignment.
    
    Example 1:
    chr1:1000-2000    20    50M
    
    converted to:
    chr1    1020    50M
    
    Example 2:
    chr1:1000-1050,2000-2050,3000-4000    25    100M
    
    converted to:
    chr1    1025    25M950N50M950M25M
    
    
    
    Usage: bamutils convertregion {-overlap} in.bam out.bam chrom.sizes
    
    Options:
    -overlap    Require that all reads must overlap a splice junction
                by 4 bases. (Also removes unmapped reads)
    
    
