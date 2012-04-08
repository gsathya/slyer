#!/usr/bin/env python
import sys
import getopt
import os 

import util

def usage():
    print "Options"
    print "-i --index    create an index page"
    print "-p --publish  render posts"
    print "-c --clean    clear headers from drafts"
    print "-s --sync     check if files are in sync"
    print "-h --help     print help"
    sys.exit(1)

def indexify():
    import index
    index = index.BlogIndex()

def publish():
    import publish
    listing = os.listdir('drafts')
    for infile in listing:
        entry = publish.BlogEntry(os.path.join('drafts', infile))

def sync():
    if util.issync():
        print "All files in sync"
    else:
        print "Files are not in sync"

def main():
    if len(sys.argv) < 2:
        usage()
    args = sys.argv[1:]
    opts = "ipcsh"
    long_opts = "index publish clean sync help".split()
    try:
        opts, args = getopt.getopt(sys.argv[1:], opts, long_opts)
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-i", "--index"):
            indexify()
        elif o in ("-p", "--publish"):
            publish()
        elif o in ("-c", "--clean"):
            util.clean()
        elif o in ("-s", "--sync"):
            sync()
        else:
            assert False, "unhandled option"

if __name__ == '__main__':
    main()
