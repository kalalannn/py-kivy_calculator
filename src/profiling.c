#include <stdio.h>
#include <math.h>

int main()
{
	double sum=0.0;
	double sumq=0.0;
	unsigned n=0;
	double tmp;
	while(scanf("%lf ",&tmp)>0)
	{
		sum+=tmp;
		sumq+=tmp*tmp;
		n++;
	}
	double ar=sum/n;
	double res=sqrt(
		(1.0/(n-1.0))*
		(sumq-n*ar*ar)
		);
	printf("%f\n",res);
	return 0;
}