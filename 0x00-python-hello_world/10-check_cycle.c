#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *timon, *pumba;

	if (list == NULL || list->next == NULL)
		return (0);

	timon = list->next;
	pumba = list->next->next;

	while (timon && pumba && pumba->next)
	{
		if (timon == pumba)
			return (1);

		timon = timon->next;
		pumba = pumba->next->next;
	}

	return (0);
}
