# what flags you want to pass to the C compiler & linker
AM_CFLAGS = --pedantic -Wall -std=c99 -O2 ${FUSE3_CFLAGS} 
AM_LDFLAGS = -lulockmgr ${FUSE3_LIBS}

# this lists the binaries to produce, the (non-PHONY, binary) targets in
# the previous manual Makefile
bin_PROGRAMS = limit-fs
limit_fs_SOURCES = limit-fs.c
