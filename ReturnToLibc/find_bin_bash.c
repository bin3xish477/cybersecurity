#include <stdio.h>
#include <stdlib.h>

int main()
{
    // export MYSELL="/bin/bash"
    char *shell = (char *)getenv("MYSHELL");

    if (shell)
    {
        printf("\tValue:\t%s\n", shell);
        printf("\tAddress: %x\n", (unsigned int)shell);
    }

    return 1;
}
