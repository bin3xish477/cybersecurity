#include <stdlib.h>
// providing the absolute path to `system` function can still
// be abused by altering both the PATH and IFS environment
// variables
int main() {
  system("/usr/bin/cal");
  return 0;
}
