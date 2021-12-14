#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

#define N 100

void main()
{
   int n = N, i, me = 0;
   double x[N], norm1, norm2, norminf;

   printf("\n Parallel execution with a maximum of %d threads callable\n\n",omp_get_max_threads());

   for (i=0; i<N; i++)
      x[i] = (double)(i+1);

   #pragma  // TO BE FINISHED
      for (i=0; i<n; i++)
      {
         norm1 = norm1 + abs(x[i]);
         norm2 = norm2 + x[i]*x[i];
         norminf = fmax(norminf, abs(x[i]));
      }

   norm1 =      norm1/(double)N;
   norm2 = sqrt(norm2/(double)N);

   printf("  1-norm = %8.4f\n", norm1  );
   printf("  2-norm = %8.4f\n", norm2  );
   printf("inf-norm = %8.4f\n", norminf);
   printf("\n");

}