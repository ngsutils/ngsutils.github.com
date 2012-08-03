---
layout: templ
title: minorallele
module: bamutils
---
    
    Calculates a minor allele frequency in (pooled) genomic sequencing.
    
    Given a BAM file and a genomic reference, for each position covered in the
    BAM file, show the reference base, the potential minor allele, and probable
    background.
    
    This assumes that if a SNP exists, there is likely only one possible variation.
    So, this calculation will fail if more than one minor allele is present.  This
    also ignores indels.
    
    If R is installed and -alleles is given, this will also calculate a 95%
    confidence interval. If rpy2 is installed, that bridge will be used to call R,
    otherwise a process is forked for each allele.
    
    
    Usage: bamutils minorallele {opts} in.bam ref.fa
    
    Arguments:
      in.bam        BAM files to import
      ref.fa        Genomic reference sequence (indexed FASTA)
    
    Options:
      -name    name  Sample name (default to filename)
      -qual    val   Minimum quality level to use in calculations
                     (numeric, Sanger scale) (default 0)
      -count   val   Only report bases with a minimum coverage of {val}
                     (default 0)
      -ci-low  val   Only report bases where the 95% CI low is greater than {val}
                     (default: show all)
      -alleles val   The number of alleles included in this sample
                     If given, a Clopper-Pearson style confidence interval will
                     be calculated. (requires rpy2 or R)
    
    rpy2 not detected! Consider installing rpy2 for faster processing!
    
