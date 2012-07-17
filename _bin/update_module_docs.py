#!/usr/bin/env python
'''
This script will automatically update the module documentation for NGSUtils
'''

import sys
import os
import subprocess
import fnmatch


modtempl = '''\
---
layout: templ
title: %(title)s
module: %(module)s
---
%(content)s
'''


def usage():
    print "Usage: update_module_docs.py ngsutils_dir"
    sys.exit(1)


def update(srcdir):
    modules = [
    ('bamutils', 'bam_utils'),
    ('bedutils', 'bed_utils'),
    ('fastqutils', 'fastq_utils'),
    ('gtfutils', 'gtf_utils')
    ]

    cmds = {}

    for module, dirname in modules:
        cmds = {}

        modhelp = runcmd(os.path.join(srcdir, module))
        reformat = '\n'.join(['    %s' % line for line in modhelp.split('\n')])

        modindex = os.path.join(os.path.dirname(__file__), '..', 'modules', module, 'index.md')

        prefix = dirname.split('_')[0]
        for root, dirs, files in os.walk(os.path.join(srcdir, dirname)):
            for f in files:
                if fnmatch.fnmatch(f, '%s_*' % prefix):
                    cmdname = f.split('_', 1)[1].split('.')[0]
                    cat, desc = getinfo(os.path.join(srcdir, dirname, f))
                    print module, cmdname,
                    if not cat or not desc:
                        print '[*]'
                    else:
                        print ''

                    if not cat in cmds:
                        cmds[cat] = []
                    help = runcmd((os.path.join(srcdir, module), cmdname, '-h'))
                    cmds[cat].append((cmdname, desc))

                    fname = os.path.join(os.path.dirname(__file__), '..', 'modules', module, cmdname, 'index.md')

                    if not os.path.exists(os.path.dirname(fname)):
                        os.makedirs(os.path.dirname(fname))

                    reformat = '\n'.join(['    %s' % line for line in help.split('\n')])

                    with open(fname, 'w') as f:
                        f.write(modtempl % {'module': module, 'title': cmdname, 'content': reformat})
        with open(modindex, 'w') as f:
            f.write('''---
layout: templ
title: %s
module: %s
---
<table cellpadding="4">''' % (module, module))
            for cat in 'DNA-seq RNA-seq General Conversion Misc'.split():
                if cat and cat in cmds:
                    f.write('<tr><td colspan="3"><h3>%s</h3></td></tr>\n' % cat)
                    for cmd, desc in sorted(cmds[cat]):
                        f.write('<tr><td>&nbsp;</td><td><a href="/modules/%s/%s">%s</a></td><td>%s</td></tr>\n' % (module, cmd, cmd, desc))
            f.write('</table>')


def getinfo(fname):
    cat = None
    desc = None

    with open(fname) as f:
        for line in f:
            if line.startswith('## category '):
                cat = line.strip().split(' ', 2)[2]
            elif line.startswith('## desc '):
                desc = line.strip().split(' ', 2)[2]
            elif line[0] != '#':
                break

    return (cat, desc)


def runcmd(args):
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return stdout


if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
        usage()

    update(sys.argv[1])
