# limit-fs
FUSE filesystem that removes the oldest files whenever the free space
reaches the set percentage.

You can use it in a no empty directory, anything you write in will be
written in the FS below. After unmounting it all files remain in the
unmounted directory.

## How to use
Once limit-fs is installed running it is very simple:

```
limit-fs [FUSE and mount options] mountPoint
```
It is recommended to run limit-fs as regular user (not as root). For
this to work the mount point must be owned by the user.

To unmount the filesystem:
```
fusermount -u mountpoint
```

On BSD and macOS, to unmount the filesystem:
```
umount mountpoint
```

### File-system specific options

You can specify the option "--usage-limit=<d>" to set the usage limit
in percentage. If the option is omitted, limit-fs use the value
**80%** as usage limit.


## Compile with
```
gcc -Wall limit-fs.c `pkg-config fuse3 --cflags --libs` -lulockmgr -o limit-fs
```
