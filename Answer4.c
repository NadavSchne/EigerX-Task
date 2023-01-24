#include <stdio.h>

int elementCount(int maxNum, int count);

int main()
{
    elementsCount(0, 0);                                // starting recursive func with no inputs
    return;
}

void elementsCount(int maxNum, int count)
{

    int n;
    scanf("%d", &n);                                    // receiving inputs 1 by 1

    if (n == 0)                                         // reached last element
    {
        printf("(%d; %d)\n", maxNum, count);            // printing as requested
        return;
    }

    if (n > maxNum)                                     // found greater number
    {
        maxNum = n;
        count = 1;                                      // reset count to 1
    }
    else if (n == maxNum)                               // encounter current greatest number again
        count++;

    elementsCount(maxNum, count);
}