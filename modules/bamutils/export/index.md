---
layout: templ
title: export
module: bamutils
---
    
    Outputs information about reads in a BAM file.
    
    This can be used to optionally extract various fields from a BAM file on a
    read-by-read basis. By default this will export the read-name, the mapped
    reference, the mapped position, and the CIGAR alignment string for a read.
    
    Usage: bamutils export {opts} {fields} bamfile
    
    Options:
      -mapped              Output only mapped reads
      -unmapped            Output only unmapped reads
    
      -whitelist file.txt  Output only reads that are listed in a text file
      -blacklist file.txt  Output only reads that are not listed in a text file
    
    Fields:
      -name          Read name
      -ref           Mapped reference (chrom)
      -pos           Mapped position (1-based)
      -strand        Mapped strand (+/-)
      -cigar         CIGAR alignment string
      -flags         Mapping flags (base 10 number)
      -seq           Sequence
      -qual          Quality sequence
      -mapq          MAPQ score
      -nextref       Next mapped reference (paired-end)
      -nextpos       Next mapped position (paired-end)
      -tlen          Template length (paired-end)
      -tag:tag_name  Any tag
                     For example:
                       -tag:AS -tag:NH
                       Outputs the alignment score and the edit distance
      -tag:*         Outputs all tags in SAM format
    
    
      Default fields: -name -ref -pos -cigar
    
    
