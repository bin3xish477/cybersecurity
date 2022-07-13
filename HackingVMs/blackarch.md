# Blackarch

### Update Blackarch

```console
sudo pacman -Syu --needed --overwrite='*' blackarch
```

### Update specific package

```console
sudo pacman -S <pkg> --noconfirm
```

### Install/Enable VMware tools

1. Fixes VM resolution to match host
2. Allow for copy/paste between guest and host
3. Improves device performances

```console
sudo pacman -S archlinux-keyring open-vm-tools glibc lib32-glibc --noconfirm
sudo systemctl enable vmtoolsd
sudo systemctl start vmtoolsd
```
