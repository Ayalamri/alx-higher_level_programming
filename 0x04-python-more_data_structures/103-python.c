#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t rrr, k;
    PyObject *element;

    printf("[*] Python list info\n");
    rrr = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", rrr);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (k = 0; k < rrr; ++k) {
        element = PyList_GetItem(p, k);
        printf("Element %ld: %s\n", k, Py_TYPE(element)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t rrr, k;
    unsigned char *string;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    rrr = PyBytes_Size(p);
    string = (unsigned char *)PyBytes_AsString(p);

    printf("  rrr: %ld\n", rrr);
    printf("  trying string: %s\n", (char *)string);

    printf("  first 10 bytes: ");
    for (k = 0; k < rrr && k < 10; ++k) {
        printf("%02x", string[k]);
        if (k + 1 < rrr && k + 1 < 10) {
            printf(" ");
        }
    }
    printf("\n");
}
