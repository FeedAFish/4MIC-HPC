#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

void main()
{

   printf("\n Parallel execution with a maximum of %d threads callable\n\n",omp_get_max_threads());

   #pragma // TO BE FINISHED
   {

      printf ("outer     id = %d, \n", omp_get_thread_num());

      #pragma // TO BE FINISHED
      {
         printf ("section 1 id = %d, \n", omp_get_thread_num());
      }

      #pragma // TO BE FINISHED
      {
         printf ("section 2 id = %d, \n", omp_get_thread_num());
      }

   }

}
