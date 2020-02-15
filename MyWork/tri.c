#include <stdlib.h>
#include <stdio.h>
long long *tribonacci(const long long signature[3], size_t n) {
  if(n == 0)
  return NULL;
  long long *sequence = malloc(sizeof(long long)*n + 1);
  long f = sequence[0] = signature[0] , s = sequence[1] = signature[1] , t = sequence[2] = signature[2];
  for(int i = 3;i < n;i++)
  {
    sequence[i] = f + s + t;
    f = s;//第二个的值给为下次循环的第一个，第三个的值为下次循环的第二个，和的值为下次循环的第三个
    s = t;
    t = sequence[i];/*或者携程sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i-3];*/
  }
  return sequence;
}
int main()
{
    long long a[3] = {1,1,1};
    long long *output = malloc(sizeof(tribonacci(a,7))+1);
    output = tribonacci(a,7);
    for(int i = 0;i<7;i++)
    {
        printf("%3d",output[i]);
    }
    return 0;
}