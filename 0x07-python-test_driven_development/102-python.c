#include <stdio.h>
#include "Python.h"

/**
 * print_python_string - Prints what the python string is all about.
 * @p: A PyObject string object.
 *
 * Return: Nothing
 */
void print_python_string(PyObject *p)
{
	long int size_len;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	size_len = ((PyASCIIObject *)(p))->size_len;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	
	printf("  length: %ld\n", size_len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &size_len));
}
