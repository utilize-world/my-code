#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *solution(int n,char*OutputString) {
  int value[7] = {1000,500,100,50,10,5,1};
  char symbol[7] = {'M','D','C','L','X','V','I'};
  int numberofSymbols[7];
  int i;//total loopcounts
  int j;//loopcounts for control
  for(i = 0;i < 7;i++)
  {
    numberofSymbols[i] =(int)(n/value[i]);
    n = n - numberofSymbols[i]*value[i];
  }
  for(i = 0;i < 7;i++)
  {
    for(j = numberofSymbols[i];j > 0;j--)
    {
      static int k = 0;
      if(j==4)
      {
        if(numberofSymbols[i-1]==0)
        {
         OutputString[k++] = symbol[i];
         OutputString[k++] = symbol[i-1];
         break;
        }
        if(numberofSymbols[i-1]==1)
        {
         OutputString[k-1] = symbol[i];
         OutputString[k++] = symbol[i-2];
         break;
        }
      }
      
      OutputString[k++]=symbol[i];
    }
  }
  return  OutputString;
}
char *solution(int n,char*OutputString);
int main()
{
   char a[20]={""};
   puts(solution(1990,a));
}