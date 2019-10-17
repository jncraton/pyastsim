/* Looks for twin primes between 0 and 1000000 */

#include <math.h>
#include <stdio.h>

#undef verbose

int check_primality(int num) {
  /* Determines if num is prime */

  /* Loop over possible factors */
  for (int test_num = 2; test_num < sqrt(num); test_num++) {
    /* Use trial division to see if we have a match */
    if (num % test_num == 0) {
      return 0;
    }
  }

  /* Return true if we didn't find anything */
  return 1;
}

int main() {
  int previous_is_prime = 0;
  int num_primes = 0;

  /* Search over possible primes */
  for (int x = 3; x < 1000000; x+=2) {
    if (check_primality(x)) {
      if (previous_is_prime) {
        num_primes += 1;
        #ifdef verbose
          printf("%d and %d\n", x-2, x);
        #endif
      }
      previous_is_prime = 1;
    } else {
      previous_is_prime = 0;
    }
  }

  printf("Found %d twin primes\n", num_primes);

  return 0;
}
