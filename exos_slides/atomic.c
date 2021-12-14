#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N1 20
#define N2 10

float work1(int i) {return 1.*i;}
float work2(int i) {return 2.*i;}

void main()
{

   float x[N2], y[N1];
   int i, index[N1];

   printf("\n Parallel execution with a maximum of %d threads callable\n\n",omp_get_max_threads());

   for (i=0; i<N1; i++)
      y[i] = 0.;

   for (i=0; i<N2; i++)
      x[i] = 0.0;

   for (i=0; i<N1; i++)
      index[i] = i%N2;

   #pragma // TO BE FINISHED
      for (i=0; i<N1; i++)
      {
         y[i] += work2(i);
         x[index[i]] += work1(i);
      }

   for (i=0; i <N1; i++)
      printf("y[%2d] = %4.1f, index[%2d] = %2d\n",i,y[i],i,index[i]);

   for (i=0; i <N2; i++)
      printf("x[%2d] = %4.1f\n",i,x[i]);

}