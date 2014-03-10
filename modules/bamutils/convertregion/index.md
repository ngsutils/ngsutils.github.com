---
layout: templ
title: convertregion
module: bamutils
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
    
    
    
    Usage: bamutils convertregion {-overlap} in.bam out.bam [chrom.sizes]
    
    (Note: A samtools faidx file can be used for the chrom.sizes file.)
    
    Options:
      -f             Force overwriting an existing out.bam file
      -unmapped      Keep all unmapped reads in the output file (including invalid junction reads)
    
      -overlap N     Require that all reads must overlap a splice junction
                     by N bases. This also removes unmapped reads. [default 4]
                     Set to zero to allow all reads.
    
      -validateonly  Don't convert the reference and position, just confirm that
                     the reads correctly overlap a junction. Any reads that don't
                     overlap a junction will not be written to the out.bam file.
    
                     If -validateonly is set, then the chrom.sizes file isn't
                     required.
    
    
    
