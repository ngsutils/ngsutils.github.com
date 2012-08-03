---
layout: templ
title: merge
module: bam
---
    
    Combine multiple BAM files together (taking best-matches)
    
    Given a number of BAM files, this script will merge them together, taking
    only the best matches.  There can be any number of files, but the BAM header
    will be taken from the first one.  The input files should be sorted by read
    name, or at least have reads in the same order.
    
    The first input file should have a record for every read in the other files.
    However, the secondary files *may* have missing lines, so long as they are in
    the same order as the first file.
    
    The value of the attribute/tag given will be used to determine which reads
    should be kept and which should be discarded. The tag should be a numberic
    (int/float) type. This defaults to 'AS'.
    
    Additionally, each file can have more than one record for each read, but they
    should all have the same value for the tag used in determining which reads to
    keep. For example, if the AS tag is used (default), then each read in a file
    should have the same AS value. Reads in different files will have different
    values.
    
    
    
    Usage: bamutils merge {opts} out.bam in1.bam in2.bam ...
    
    Options
      -tag VAL    Tag to use to determine from which file reads will be taken
                  (must be type :i or :f) [default: AS]
      -discard    Discard reads that aren't mapped in any file.
    
    
