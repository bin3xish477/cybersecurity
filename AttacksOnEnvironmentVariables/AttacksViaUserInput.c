// An intentionally vulnerable program for showing demonstrating
// attacks on SUID programs via explicit user input

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  char *cat = "/bin/cat";
  if (argc < 2) {
    printf("Please type a file name.\n");
    return 1;
  }
  
  char *command = malloc(strlen(cath) + strlen(argv[1] + 2);
  sprintf(command, "%s %s", cat, argv[1]);
  system(command);
  
  return 0;
}
