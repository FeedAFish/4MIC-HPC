#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define CHUNKSIZE 4
#define N 20

void main()
{

   int nthreads, tid, i, chunk, which[N];
   float a[N], b[N], c[N];

   printf("\n Parallel execution with a maximum of %d threads callable\n\n",omp_get_max_threads());

   for (i=0; i < N; i++)
      a[i] = b[i] = i * 1.0;

   chunk = CHUNKSIZE;

   #pragma // TO BE FINISHED
   {

      tid = omp_get_thread_num();

      #pragma // TO BE FINISHED
         for (i=0; i<N; i++)
         {
            c[i] = a[i] + b[i];
            which[i] = tid;
         }

   }

   for (i=0; i < N; i++)
      printf("c[%2d] = %4.1f treated by thread %2d\n",i,c[i],which[i]);

}