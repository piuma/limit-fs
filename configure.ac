AC_PREREQ([2.69])
AC_INIT(limit-fs, 0.1, danilo@piumalab.org)

AC_CONFIG_SRCDIR([limit-fs.c])

AM_INIT_AUTOMAKE

#AC_CONFIG_HEADERS([config.h])



# Checks for programs.
AC_PROG_CC

# Checks for libraries.

PKG_CHECK_MODULES([FUSE3], [fuse3 >= 3], [have_fuse3=yes], [
  PKG_CHECK_MODULES([FUSE], [fuse < 3], [have_fuse3=no])
])
AM_CONDITIONAL([FUSE3],  [test "$have_fuse3" = "yes"])



# Checks for header files.
#AC_CHECK_HEADERS([fcntl.h stddef.h stdlib.h string.h sys/file.h sys/time.h unistd.h])
AC_CHECK_HEADERS([fuse.h stdio.h stdlib.h string.h unistd.h fcntl.h sys/stat.h dirent.h errno.h sys/time.h sys/file.h stddef.h assert.h ftw.h])

AC_OUTPUT(Makefile)

# Checks for typedefs, structures, and compiler characteristics.
AC_TYPE_UID_T
AC_C_INLINE
AC_TYPE_MODE_T
AC_TYPE_OFF_T
AC_TYPE_SIZE_T
AC_TYPE_SSIZE_T

# Checks for library functions.
AC_FUNC_MALLOC
AC_CHECK_FUNCS([fdatasync ftruncate memset mkfifo realpath strdup strerror strrchr])

AC_OUTPUT
