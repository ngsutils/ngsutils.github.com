---
layout: templ
title: filter
module: bamutils
---
    
    Removes reads from a BAM file based on criteria
    
    Given a BAM file, this script will only allow reads that meet filtering
    criteria to be written to output. The output is another BAM file with the
    reads not matching the criteria removed.
    
    Note: this does not adjust tag values reflecting any filtering. (for example:
          if a read mapped to two locations (IH:i:2), and one was removed by
          filtering, the IH:i tag would still read IH:i:2).
    
    Currently, the available filters are:
        -minlen val                Remove reads that are smaller than {val}
        -maxlen val                Remove reads that are larger than {val}
        -mapped                    Keep only mapped reads
        -mask bitmask              Remove reads that match the mask (base 10/hex)
    
        -mismatch num              # mismatches or indels
                                   indel always counts as 1 regardless of length
                                   (requires NM tag in reads)
        -mismatch_ref num ref.fa   # mismatches or indel - looks up mismatches
                                   directly in a ref FASTA file (if NM not
                                   available)
        -noqcfail                  Remove reads that have the 0x200 flag set
        -nosecondary               Remove reads that have the 0x100 flag set
    
    
        -exclude ref:start-end     Remove reads in this region (1-based start)
        -excludebed file.bed       Remove reads that are in any of the regions
                                   from the given BED file
    
        -include ref:start-end     Remove reads NOT in the region (can only be one)
        -includebed file.bed       Remove reads that are NOT any of the regions
                                   from the given BED file
                                   Note: If this is a large dataset, use
                                   "bamutils extract" instead.
    
        -whitelist fname           Remove reads that aren't on this list (by name)
        -blacklist fname           Remove reads that are on this list (by name)
                                     These lists can be whitespace-delimited with
                                     the read name as the first column.
    
        -eq  tag_name value
        -lt  tag_name value
        -lte tag_name value
        -gt  tag_name value
        -gte tag_name value
    
        As a special case, "MAPQ" can be used as the tag_name and the SAM MAPQ
        value will be used.
    
    Common tags to filter by:
        AS      Alignment score
        IH      Number of alignments
        NM      Edit distance (each indel counts as many as its length)
    
        MAPQ    Mapping quality (defined as part of SAM spec)
    
        The tag type (:i, :f, :Z) is optional.
    
    
    
    Usage: bamutils filter in.bam out.bam {-failed out.txt} criteria...
    
    Options:
      -failed fname    A text file containing the read names of all reads
                       that were removed with filtering
    
    Example:
    bamutils filter filename.bam output.bam -mapped -gte AS:i 1000
    
    This will remove all unmapped reads, as well as any reads that have an AS:i
    value less than 1000.
    
    
