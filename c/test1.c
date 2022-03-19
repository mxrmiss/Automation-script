# include <string.h>
# include <stdio.h>

int main(void)
{
	struct staff
	{
		char name[20];
		char deparment[20];
		int salary;
		int cost;
	}worker[3] = {
					{"Xu_Gou", "part1", 800, 200},
					{"Wu_Xia", "part2", 1000, 300},
					{"Li_Jun", "part3", 1200, 350}	
				};
	int i;
	char xname[20];
	printf("\nInput the worker\'s name:");
	scanf("%s", xname);
	for(i = 0; i < 3; i++)
	{
		if(strcmp(xname, worker[i].name) == 0)
		{
			printf("* * * *%s* * * *", xname);
			printf("\n salary:%6d", worker[i].salary);
			printf("\n cost :%6d", worker[i].cost);
			printf("\n payed:%6d", worker[i].salary - worker[i].cost);
		}
	}
 } 
