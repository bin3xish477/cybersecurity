#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

void main()
{
  int fd;
  char *v[2];
  
  /*
  Assume `/etc/xyz` is an important system file, and it
  is owned by root with permission 0644.
  Before running this program, you should create the file
  `/etc/xyz/` first
  */
  fd = open("/etc/xyz", O_RDWR | O_APPEND);
  if (fd == -1)
  {
    printf("Cannot open /etc/xyz\n");
    exit(0);
  }
  
  printf(fd is %d\n", fd);
  
  // permanently disable the privilege by making the
  // effective uid the same as the real uid
  setuid(getuid());
  
  // execute `/bin/bash`
  v[0] = "/bin/bash"; v[1] = 0;
  execve(v[0], v, 0);
}
