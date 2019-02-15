# what flags you want to pass to the C compiler & linker

if FUSE3
  AM_CFLAGS = ${FUSE3_CFLAGS}
else
  AM_CFLAGS = ${FUSE_CFLAGS}
endif

AM_CFLAGS += --pedantic -Wall -std=c99 -O2

# this lists the binaries to produce, the (non-PHONY, binary) targets in
# the previous manual Makefile

bin_PROGRAMS = limit-fs
limit_fs_LDADD = -lulockmgr
if FUSE3
  limit_fs_SOURCES = limit-fs.c
  limit_fs_LDADD += ${FUSE3_LIBS}
else
  limit_fs_SOURCES = limit-fs2.c
  limit_fs_LDADD += ${FUSE_LIBS}
endif
