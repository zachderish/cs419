#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>
#include <dirent.h>
#include <string.h>


// Name: Zachary Derish
// netID: zpd3
// RUID: 201001379
// your code for readdir goes here

typedef struct dirent *(*readdir_t)(DIR*);

// function to check directory against all hidden_files
int strings_comp(char* directory) {
    char* hidden_files = getenv("HIDDEN");
    char* hidden_files_copy = strdup(hidden_files);

    char *file = strtok(hidden_files_copy, ":");
    while (file != NULL) {
        if (strcmp(directory, file) == 0) {
            return 0;
        }
        file = strtok(NULL, ":");
    }
    return 1;

}

struct dirent *readdir(DIR *dirp) {
    readdir_t original_readdir = (readdir_t)dlsym(RTLD_NEXT, "readdir");
    struct dirent *dir;

    while ((dir = original_readdir(dirp)) != NULL) {
        if(strings_comp(dir->d_name) == 0) {
            continue;
        }
        return dir;
    }

    return NULL;

}



