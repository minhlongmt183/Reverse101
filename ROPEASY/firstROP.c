#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void not_called()
{
    printf("Enjoy Your Shell\n");
    system("/bin/sh");
    exit(0);
}

void vulnerable_func(char *string)
{
    char buffer[96];
    memcpy(buffer, string, 96+8+8);
    memset(buffer+107, 0, 5);
}

int main(int argc, char** argv){
    vulnerable_func(argv[1]);
    return 0;
}
