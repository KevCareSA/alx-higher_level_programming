#include "lists.h"

 /**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to head 
 * @number: integer to insert
 * Return: listint_t*
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev_node;
	listint_t *new_node;
	listint_t *now_node;
	int n;

	now_node = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (now_node == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}

	while (now_node != NULL)
	{
		n = now_node->n;
		if (n > number)
		{
			break;
		}

		prev_node = now_node;
		now_node = now_node->next;
	}

	new_node->next = now_node;
	if (now_node == *head)
		*head = new_node;
	else
		prev_node->next = new_node;

	return (new_node);
}
