#include <math.h>
#include <stdio.h>

#undef show_primes

int is_prime(int n) {
  /* Implements a primality test on n

  The algorithm used is to simply test primes from 2 to sqrt(n).

  There are better algorithms for this, but this is simple to understand
  and implement.
  */

  for (int test = 2; test < sqrt(n); test++) {
    if (n % test == 0) {
      return 0;
    }
  }

  return 1;
}

int main() {
  int last_was_prime = 0;
  int count = 0;

  for (int i = 3; i < 1000000; i+=2) {
    if (is_prime(i)) {
      if (last_was_prime) {
        count += 1;
        #ifdef show_primes
          printf("%d and %d\n", i-2, i);
        #endif
      }
      last_was_prime = 1;
    } else {
      last_was_prime = 0;
    }
  }

  printf("Found %d twin primes\n", count);

  return 0;
}
