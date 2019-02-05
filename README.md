# limitfs
FUSE filesystem that removes the oldest file whenever the free space reaches the setted percentage

## How to use
Once limitfs is installed running it is very simple:

```
limitfs [FUSE and mount options] mountPoint
```
It is recommended to run limitfs as regular user (not as root). For
this to work the mountpoint must be owned by the user.

You can specify the option "--usage-limit=<d>" to set the usage limit
in percentage. If the option is omitted, limitfs use the value 80% as
usage limit.


To unmount the filesystem:
```
fusermount -u mountpoint
```

On BSD and macOS, to unmount the filesystem:
```
umount mountpoint
```


## Compile with
```
gcc -Wall limitfs.c `pkg-config fuse --cflags --libs` -lulockmgr -o limitfs
```

On Linux and BSD, you will also need to install libfuse 3.1.0 or
newer. On macOS, you need OSXFUSE instead.

