#include <stdio.h>
#include <stdlib.h>
#ifdef _OPENMP
#include <omp.h>
#endif

void main()
{
   int tid, max_threads, num_threads;

   #ifdef _OPENMP
      max_threads = omp_get_max_threads();
      printf("\n Parallel execution with a maximum of %d threads callable\n\n",max_threads);
   #else
      printf("\n Sequential execution\n\n");
   #endif

   #pragma omp parallel private(tid) shared(max_threads) num_threads(2)
   {
      #ifdef _OPENMP
         tid         = omp_get_thread_num();
         num_threads = omp_get_num_threads();
         printf("Hello World from thread %2d / %2d / %2d\n", tid, num_threads, max_threads);
      #else
         printf("Hello World\n");
      #endif
   }
}