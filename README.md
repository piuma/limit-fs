# limit-fs
FUSE filesystem that removes the oldest files whenever the free space
reaches the set percentage.

You can use it in a no empty directory, anything you write in will be
written in the underlying filesystem. After unmounting it all files
remain in the unmounted directory.

## How to use
Once limit-fs is installed running it is very simple:

```
limit-fs [FUSE options] [mount options] mountPoint
```
It is _strongly recommended_ to run limit-fs as regular user (not as
root). For this to work the mount point must be owned by the user.

To unmount the filesystem:
```
fusermount -u mountpoint
```

## Screencast
[![limit-fs screencast](https://asciinema.org/a/228205.png)](https://asciinema.org/a/228205)

## File-system specific options

You can specify the options:

| option | default | description |
|:-:|:-:|---|
| --usage-limit=<d>  | *80* | set the usage limit in percentage. |

## Example
```
limit-fs --usage-limit=90 /mnt/
```

## Installation from source

 * Install dependences in fedora >= 27
```
# dnf install m4 automake autoconf gcc fuse3 fuse3-devel
```

 * Install dependences in CentOS/RHEL/Fedora < 27
```
# yum install m4 automake autoconf gcc fuse fuse-devel
```

* Compile and install
```
$ ./setup.sh
$ ./configure
$ make
$ sudo make install
```
