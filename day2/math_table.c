#include<stdio.h>

int main()
{
    int inputNum = 0;
    puts("Enter a number to print Math table: ");
    scanf("%d",&inputNum);
    int i = 0;
    int table = 0;
    for(i = 1; i <= 10;i++)
    {
        
        
       printf("%d * %d = %d \n",inputNum ,i,i*inputNum);

    }

return 0;

} 