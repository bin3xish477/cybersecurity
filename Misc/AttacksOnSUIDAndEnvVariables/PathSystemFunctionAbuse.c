#include <stdlib.h>
// overwriting the PATH variable will allow the attacker to perform 
// search order hijacking attack and replace the "cal" program that
// would normally run
int main() {
  system("cal");
  return 0;
}
