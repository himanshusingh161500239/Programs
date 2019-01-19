#include<stdlib.h>
void main()
{
    char s[100];
    int n,len,i;
    printf("Enter the String\n");
    gets(s);
    printf("Enter the number of character you want from last\n");
    scanf("%d",&n);
    char result[n];
    len=strlen(s);
    int j=0;
    for(i=len-n;s[i]!='\0';i++)
    {
        result[j]=s[i];
        j=j+1;
    }
    for(i=0;i<n;i++)
        printf("%c", result[i]);
}
