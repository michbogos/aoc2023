//gcc 06-2.c -o program -Ofast
#include<stdio.h>
#include<omp.h>

int main(){

long time = 48938595;
long distance = 296192812361391;

int res = 0;

#pragma omp parallel for num_threads(8)
for(int i = 0; i <= time; i++){
    if(i*(time-i)>distance){
        res++;
    }
}

printf("%d\n", res);
return 0;
}