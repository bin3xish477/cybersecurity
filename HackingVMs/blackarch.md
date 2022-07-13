# Blackarch

### Update Blackarch

```console
sudo pacman -Syu --needed --overwrite='*' blackarch
```

### Update specific package

```console
sudo pacman -S <pkg> --confirm
```

### Install/Enable VMware tools

1. Should maximize screen
2. Allow for copy/paste between guest and host
3. Improves device performances
4. etc

```console
sudo pacman -S --confirm open-vm-tools
sudo systemctl enable vmtoolsd
sudo systemctl start vmtoolsd
```
