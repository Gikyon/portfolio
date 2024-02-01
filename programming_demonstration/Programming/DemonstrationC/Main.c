// Micah Joshua Rahardjo 991687206 PROG36859 //
                // workshop 3//
        // rahardjm@sheridan college.ca //

#include <stdio.h>
#include <string.h>
#define _CRT_SECURE_NO_WARNINGS
#include "Movie.h"
#include "Movie.c"

int main(){

    struct movie m[100];
    int num = 0;
    char yes;
    FILE* file = fopen("movies.dat", "r");
    while(num < 100 && loadMovie(&m[num], file)) {
       list(&m[num], num+1);
       num++;
    }
    fclose(file);
    do {
      searchMovies(m, num);
      printf("Another Search? (y)es/(n)o: ");
      yes = getchar();
      while(getchar() != '\n');
   } while(yes == 'y' || yes == 'Y');
   return 0;
}

void searchMovies(struct movie* m, int size) {
   char title[51];
   int i;
   int found;
   printf("Searching for a movie based on title...\n");
   printf("Title: ");
   scanf("%[^\n]", title);
   for(found = 0,i = 0; i < size; i++) {
      if(strstr(getMovieTitle(&m[i]), title)) {
         printf("%d ============================\n", ++found);
         display(&m[i]);
      }
   }
   while(getchar() != '\n');
}
