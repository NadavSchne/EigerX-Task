#include <stdio.h>

int digitsSum(int n);

int main()
{
    int num = 2347623;
    int sum = digitsSum(num);
    printf("The sum of the digits of your number is: %d\n", sum);
    return;
}

int digitsSum(int n)
{
    if (n == 0)                                 // return with 0 once all numbers were processed
        return 0;
    return (n % 10 + digitsSum(n / 10));        // calculate the last digit and call recursivly without last digit
}