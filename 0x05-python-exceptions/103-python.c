#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < PyList_Size(p); ++i) {
        PyObject *element = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(element)) {
            printf("bytes\n");
            print_python_bytes(element);
        } else if (PyFloat_Check(element)) {
            printf("float\n");
            print_python_float(element);
        } else if (PyLong_Check(element)) {
            printf("int\n");
            print_python_int(element);
        } else if (PyList_Check(element)) {
            printf("list\n");
            print_python_list(element);
        } else if (PyTuple_Check(element)) {
            printf("tuple\n");
            print_python_tuple(element);
        } else if (PyUnicode_Check(element)) {
            printf("str\n");
            print_python_str(element);
        } else {
            printf("[.] Unknown type\n");
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; ++i) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", PyFloat_AsDouble(p));
}
