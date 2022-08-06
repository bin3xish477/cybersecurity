# Docker Security Cheat Sheet

### Keep Underlying Host and Docker Up to Date

### Do Not Expose Docker Daemon Socket

### Create and Use Unprivileged User

### Limit Cabilities

> drop all default capabilities and only add the ones you need

```console
docker run --cap-drop all --cap-add CHOWN --cap-add SYS_TIME alpine
```

### Set the `--no-new-privileges` Flag

### Disable inter-container Communication

```console
dockerd --icc=false ...
```

### Use Linux Security Modules

### Limit Container Resources

### Set Filesystem and Volumes to Read-Only

### Use Static Analysis Tools

### Use Minimum Logging Level of INFO

### Lint the Dockerfile at Build Time
