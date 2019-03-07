# limit-fs
FUSE filesystem that removes the oldest files whenever the used space
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

To unmount the filesystem use `fusermount -u mountpoint`

## Screencast
[![limit-fs screencast](https://asciinema.org/a/228205.png)](https://asciinema.org/a/228205)

## Mounting automatically at boot time

Add the FS to the */etc/fstab* file. For example take the line:
```
limit-fs   /mnt/tmpfs/limitfs	limit-fs	usage-limit=95,id=1000,gid=1000,user	0 0
```
Second part is the mount point which the limit-fs is mounted.

Next use limit-fs in the file system type.

Then comes the options **usage-limit=95,uid=1000,gid=1000,user**

## File-system specific options

You can specify the options:

| long option | short option | default | description |
|:-:|:-:|:-:|---|
| --usage-limit=<d> | -u | *80* | set the usage limit in percentage. |
| --help            | -h |      | print help message |
| --version         | -V |      | print version |

## Example
```
limit-fs --usage-limit=90 /mnt/
```

## Installation from source

 * Install dependences in Fedora >= 27
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
