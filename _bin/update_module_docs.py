#!/usr/bin/env python
'''
This script will automatically update the module documentation for NGSUtils
'''

import sys
import os
import subprocess


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
    modules = "bam bed fastq gtf".split()

    cmds = {}

    for module in modules:
        cmds = {}

        # modhelp = runcmd(os.path.join(srcdir, module))
        # reformat = '\n'.join(['    %s' % line for line in modhelp.split('\n')])

        modindex = os.path.join(os.path.dirname(__file__), '..', 'modules', '%sutils' % module, 'index.md')

        for root, dirs, files in os.walk(os.path.join(srcdir, 'ngsutils', module)):
            if root != os.path.join(srcdir, 'ngsutils', module):
                continue

            for f in files:
                if os.access(os.path.join(srcdir, 'ngsutils', module, f), os.X_OK):
                    cmdname = os.path.basename(f)[:-3]
                    cat, desc, experimental = getinfo(os.path.join(srcdir, 'ngsutils', module, f))

                    print module, cmdname,

                    if not cat or not desc:
                        print '[*]'
                    else:
                        print ''

                    if not cat in cmds:
                        cmds[cat] = []

                    help = runcmd((os.path.join(srcdir, 'bin', '%sutils' % module), cmdname, '-h'))
                    cmds[cat].append((cmdname, desc, experimental))

                    fname = os.path.join(os.path.dirname(__file__), '..', 'modules', '%sutils' % module, cmdname, 'index.md')

                    if not os.path.exists(os.path.dirname(fname)):
                        os.makedirs(os.path.dirname(fname))

                    reformat = '\n'.join(['    %s' % line for line in help.split('\n')])

                    with open(fname, 'w') as f:
                        f.write(modtempl % {'module': '%sutils' % module, 'title': cmdname, 'content': reformat})

        with open(os.path.join(srcdir, 'ngsutils', module, 'README'), 'w') as f:
            max_cmd_len = 0
            for cat in 'DNA-seq RNA-seq General Conversion Misc'.split():
                if cat and cat in cmds:
                    for cmd, desc, experimental in sorted(cmds[cat]):
                        if experimental:
                            continue

                        if len(cmd) > max_cmd_len:
                            max_cmd_len = len(cmd)

            f.write('Commands')
            for cat in 'DNA-seq RNA-seq General Conversion Misc'.split():
                if cat and cat in cmds:
                    f.write('\n  %s\n' % cat)
                    for cmd, desc, experimental in sorted(cmds[cat]):
                        if experimental:
                            continue

                        fmt = '    %%-%ss - %%s\n' % (max_cmd_len)
                        f.write(fmt % (cmd, desc))

        with open(modindex, 'w') as f:
            f.write('''---
layout: templ
title: %sutils
module: %sutils
---
<table cellpadding="4">''' % (module, module))
            for cat in 'DNA-seq RNA-seq General Conversion Misc'.split():
                if cat and cat in cmds:
                    f.write('<tr><td colspan="3"><h3>%s</h3></td></tr>\n' % cat)
                    for cmd, desc, experimental in sorted(cmds[cat]):
                        f.write('<tr><td>&nbsp;</td><td><a href="/modules/%sutils/%s">%s</a></td><td>%s%s</td></tr>\n' % (module, cmd, cmd, desc, ' (experimental)' if experimental else ''))
            f.write('</table>')


def getinfo(fname):
    cat = None
    desc = None
    experimental = False

    with open(fname) as f:
        for line in f:
            if line.startswith('## category '):
                cat = line.strip().split(' ', 2)[2]
            elif line.startswith('## desc '):
                desc = line.strip().split(' ', 2)[2]
            elif line.startswith('## experimental'):
                experimental = True
            elif line[0] != '#':
                break

    return (cat, desc, experimental)


def runcmd(args):
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return stdout


if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
        usage()

    update(sys.argv[1])
