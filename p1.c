// accept the no from the user and check if its even or not
#include<stdio.h>
int main()
{
int inputNum = 0;
puts("Enter a number to check if it is Even ");
scanf("%d",&inputNum);
if (inputNum % 2 == 0)
    printf("%d is even",inputNum);
else
    printf("%d is not even",inputNum);
return 0;
}

