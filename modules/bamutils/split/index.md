---
layout: templ
title: split
module: bamutils
---
    
    Splits a BAM file into smaller pieces
    
    Given a BAM file, this script will split it into smaller BAM files with a
    limit on the number of reads included.
    
    Or it will also split a BAM file into a separate BAM file for each reference
    that is included.
    
    
    Usage: bamutils split {-n num | -ref} in.bam out_template_name
    
    out_template_name will be the template for the smaller BAM files.  They will
    be named "out_template_name.N.bam" where out_template_name is the given
    argument and N is the file number.
    
    Options:
        -n      The number of reads to include in sub-files
                (default: 1000000)
    
        -ref    Split by references
    
    
