# limitfs
FUSE filesystem that removes the oldest file whenever the free space reaches the setted percentage

## Compile with
```
gcc -Wall limitfs.c `pkg-config fuse --cflags --libs` -lulockmgr -o limitfs
```

You must have FUSE (version 2.9) installed to compile rotatefs.

## Usage
```
limitfsfs [FUSE and mount options] mountPoint
```
