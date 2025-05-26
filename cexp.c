#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#define SESSION_DURATION 1500 

struct data{
    char *ch;
    char *ch1;
    char *ch2;
    char *ch3;  
};

void display() {
    char command[100];
    sprintf(command, "py pyt3.py"); // Replace with your path
    system(command);
}

void start_timer() {
    printf("Welcome to the Focus Timer!\n");
    printf("Please enter your name: ");
    char name[50];
    scanf("%s",name);
    FILE *p=fopen("session.csv","r");
    char *rc;
    char r[100];
    int rpg= 1;

    while(fgets(r,100,p)){
        rc=strtok(r,",");
        if (strcmp(rc,name)==0){
            printf("Welcome back %s.\n",name);
            rpg=0;
            break;
        }
    }
    fclose(p);
    if (rpg){
        FILE *fp=fopen("session.csv","a+");
        fprintf(fp,"%s,0,0,0\n",name);
        fclose(fp);
        printf("Welcome %s! This is your first session.\n",name);
    }
    printf("Enter the duration for your focus session in minutes (default is 25): ");
    int duration;
    if (scanf("%d", &duration) != 1 || duration <= 0) {
        printf("Invalid input. Using default duration of 25 minutes.\n");
        duration = SESSION_DURATION;
    } else {
        duration =duration * 60;
    }

    printf("Focus session started! Stay focused for %d minutes...\n",duration / 60);
    //sleep(duration);
    
    printf("Session complete! Well done!\n");
    FILE *fp=fopen("session.csv","r");
     struct data d;
     char chr[100];
    FILE *temp_file = fopen("temp.csv", "w");
     printf("Updating session data...\n");
     while(fgets(chr,100,fp)){
       d.ch=strtok(chr,",");
       d.ch1=strtok(NULL,",");
       d.ch2=strtok(NULL,",");
       d.ch3=strtok(NULL,",");
        char updated_line[1024];
       if (strcmp(d.ch,name)==0){
          if (duration/60<40){
               int value=atoi(d.ch1)+1;
               sprintf(updated_line, "%s,%d,%s,%s",d.ch, value,d.ch2,d.ch3);
          }
          else if (duration/60<60){
               int value=atoi(d.ch2)+1;
               sprintf(updated_line, "%s,%s,%d,%s",d.ch, d.ch1,value,d.ch3);
          }
          else if (duration/60>60){
               int value=atoi(d.ch3)+1;
               sprintf(updated_line, "%s,%s,%s,%d\n",d.ch, d.ch1,d.ch2,value);
          }
          fputs(updated_line,temp_file);

       }
       else{
        sprintf(updated_line, "%s,%s,%s,%s",d.ch, d.ch1,d.ch2,d.ch3);
        fputs(updated_line,temp_file);
       }
    }

    fclose(fp);
    fclose(temp_file);
    remove("session.csv");
    rename("temp.csv", "session.csv");
    printf("Value incremented successfully.\n");
    
}

int main() {
    start_timer();
    char choice;
    printf("Do u want to See ur progress press y/n.\n");
    fflush(stdin);
    scanf("%c",&choice);
    if (choice == 'y' || choice == 'Y') {
        display();
    }
    printf("Thank you");
    return 0;
    
}