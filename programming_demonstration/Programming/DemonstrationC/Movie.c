// Micah Joshua Rahardjo 991687206 PROG36859 //
                // workshop 3//
        // rahardjm@sheridan college.ca //

#include <stdio.h>
#include <string.h>
#define _CRT_SECURE_NO_WARNINGS
#include "Movie.h"

struct movie {

    char mName[60];
    int year;
    char rating[3];
    int duration;
    char genre[60];
    char cRating[4];

};

int loadMovie(struct movie* mptr, FILE* fptr){

    if (fscanf(fptr, "%[^\t]\t%4d\t%[^\t]\t%d\t%[^\t]\t%s\n", mptr->mName, &mptr->year, mptr->rating, &mptr->duration, mptr->genre, &mptr->cRating) == 6){
        return 1;
    } 
    else return 0; 
}

void printInWidth(const char str[], int width){
    int  i, len;

    len = strlen(str);

    if (len >= width){
        for (i=0; i<width-1; i++){
            printf("%c", str[i]);
        }
    }
    else{
        printf("%s", str);
        for(i=0; i<width-len-1 ;i++){
            printf(" ");

        }
    }

}

void list(const struct movie* mptr, int row){
    int hour, minute, time;
    time = mptr->duration;
    hour = time/60;
    minute = time%60;
    
    putchar('|');
    printf("%-5d", row);
    putchar('|');
    printInWidth(mptr->mName, 20);
    putchar('|');
    printf( "%-5d", mptr->year);
    putchar('|');
    printInWidth(mptr->rating, 5);
    putchar('|');
    printf( "%d:%-4d", hour, minute);
    putchar('|');
    printInWidth(mptr->genre, 25);
    putchar('|');
    printInWidth(mptr->cRating, 5);
    putchar('|');
    printf("\n");
}

void display(const struct movie* mptr){
    int hour, minute, time;
    time = mptr->duration;
    hour = time/60;
    minute = time%60;

    printf("Title : %s\n", mptr->mName);
    printf("Year : %d\n", mptr->year);
    printf("Rating : %s\n", mptr->rating);
    printf("Duration : %d:%d\n", hour,minute);
    printf("Genre : %s\n", mptr->genre);
    printf("Consumer rating : %s\n", mptr->cRating);

}

const char* getMovieTitle(const struct movie* mptr){
    return &mptr->mName;
}

