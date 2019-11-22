# xonsh-remoteDirCompleter

This script enables tab completion for remote directories, just like fish and zsh do.

Like this:
```
 $ ~ rsync hp:/ (press tab)
 bin/           etc/           lib/           mnt/           run/           swap8G.img     var/          
 boot/          home/          lib64/         opt/           sbin/          sys/           vmlinuz       
 dev/           initrd.img     lost+found/    proc/          snap/          tmp/           vmlinuz.old   
 docker/        initrd.img.old media/         root/          srv/           usr/                            
```

### Installation
Move the script to an appropriate location, and then add it to your completers by using
```
source /path/to/xonsh-remoteDirCompleter.xsh
completer add RemoteDirCompleter remoteDirCompleter
```
You might want to do this in your .xonshrc to enable this on shell startup.
