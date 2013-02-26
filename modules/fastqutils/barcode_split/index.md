---
layout: templ
title: barcode_split
module: fastqutils
---
    
    Given a FASTA/FASTQ file and a list of barcodes (name and seq),
    the FASTA/FASTQ file is split into N number of new files representing
    the reads for each barcode. The format of the input file is determined
    automatically. The barcode will be removed from read sequence (and quality
    score if FASTQ).
    
    barcode input format:
    tagname	sequence	orientation (5 or 3)
    
    The output files will be named: out_template_tagname.fast[qa]
    
    Reads missing a barcode (or if the tag is too degenerate) will be written to:
    out_template_missing.fast[qa]
    
    Note: This is a slow method using a Smith-Waterman alignment algorithm. It is
          primarily useful with data that is inherently noisy, such as PacBio
          sequencing reads. For less-noisy sequences, a faster, non-alignment
          approach will be better.
    
    Note 2: This isn't appropriate for color-space FASTQ files with a prefix base
            included in the read sequence, since it trims an equal number of bases
            from the sequence and quality FASTQ lines.
    
    
    Usage: barcode_split.py {options} barcodes.txt input.fastx{.gz} output_template
    
    Options:
      -edit num         Number of mismatches/indels to allow in barcode discovery.
                        (default: 0)
    
      -pos num          Allow barcode to be within [num] bases from the start.
                        (or end for 3' barcodes) (default: 0)
    
      -allow-revcomp    Allow barcodes to match the reverse-compliment of a read.
                        (non-strand specific sequencing) The read's orientation
                        will *not* be changed in the output file.
    
      -gz               GZip compress the output files.
    
      -stats            Output stats file (output_template.stats.txt)
    
