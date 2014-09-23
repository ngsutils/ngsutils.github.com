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
        -unmapped                  Keep only unmapped reads
        -properpair                Keep only properly paired reads (both mapped, 
                                   correct orientation, flag set in BAM)
        -noproperpair              Keep only not-properly paired reads
    
        -mask bitmask              Remove reads that match the mask (base 10/hex)
        -uniq {length}             Remove reads that are have the same sequence
                                   Note: BAM file should be sorted
                                   (up to an optional length)
        -uniq_start                Remove reads that start at the same position
                                   Note: BAM file should be sorted
                                   (Use only for low-coverage samples)
    
        -mismatch num              # mismatches or indels
                                   indel always counts as 1 regardless of length
                                   (requires NM tag in reads)
    
        -mismatch_dbsnp num dbsnp.txt.bgz
                                   # mismatches or indels - not in dbSNP.
                                   Variations are called using the MD tag.
                                   Variations that are found in the dbSNP list are
                                   not counted as mismatches. The dbSNP list is a
                                   Tabix-indexed dump of dbSNP (from UCSC Genome
                                   Browser). Indels in dbSNP are also counted.
                                   Adds a 'ZS:i' tag with the number of found SNPs
                                   in the read.
                                   (requires NM and MD tags)
    
                                   Example command for indexing:
                                   ngsutils tabixindex snp.txt.gz -s 2 -b 3 -e 4 -0
    
        -mismatch_ref num ref.fa   # mismatches or indel - looks up mismatches
                                   directly in a reference FASTA file
                                   (use if NM tag not present)
    
        -mismatch_ref_dbsnp num ref.fa dbsnp.txt.bgz
                                   # mismatches or indels - looks up mismatches
                                   directly from a reference FASTA file. (See
                                   -mismatch_dbsnp for dbSNP matching)
                                   (use if NM or MD tag not present)
    
        -nosecondary               Remove reads that have the 0x100 flag set
        -noqcfail                  Remove reads that have the 0x200 flag set
        -nopcrdup                  Remove reads that have the 0x400 flag set
    
    
        -exclude ref:start-end     Remove reads in this region (1-based start)
        -excludebed file.bed {nostrand}
                                   Remove reads that are in any of the regions
                                   from the given BED file. If 'nostrand' is given,
                                   strand information from the BED file is ignored.
    
        -include ref:start-end     Remove reads NOT in the region (can only be one)
        -includebed file.bed {nostrand}
                                   Remove reads that are NOT any of the regions
                                   from the given BED file. If 'nostrand' is given,
                                   strand information from the BED file is ignored.
    
                                   Note: If this is a large dataset, use
                                   "bamutils extract" instead.
    
        -includeref refname        Exclude reads NOT mapped to a reference
        -excluderef refname        Exclude reads mapped to a particular reference
                                   (e.g. chrM, or _dup chromosomes)
    
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
    
    
