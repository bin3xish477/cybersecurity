#include <stdio.h>
// altering the LD_PRELOAD environment variable will
// allow an attacker to change the libraries loaded 
// by a program using external libraries
int main() {
  printf("Hello World!");
  sleep(2);
  return 0;
}
