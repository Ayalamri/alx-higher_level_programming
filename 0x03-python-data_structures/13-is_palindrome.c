#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return *head;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev_slow = *head;
    listint_t *second_half, *mid_node = NULL;
    int is_palindrome = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        if (fast != NULL)
        {
            mid_node = slow;
            slow = slow->next;
        }

        second_half = slow;
        prev_slow->next = NULL;
        reverse_list(&second_half);
        is_palindrome = compare_lists(*head, second_half);
        reverse_list(&second_half);

        if (mid_node != NULL)
        {
            prev_slow->next = mid_node;
            mid_node->next = second_half;
        }
        else
            prev_slow->next = second_half;
    }

    return is_palindrome;
}

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the first list
 * @list2: pointer to the second list
 * Return: 1 if lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n == list2->n)
        {
            list1 = list1->next;
            list2 = list2->next;
        }
        else
            return 0;
    }

    if (list1 == NULL && list2 == NULL)
        return 1;
    return 0;
}
