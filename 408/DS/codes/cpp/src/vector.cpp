#include "vector.h"

template <typename T> 
void Vector<T>::copyFrom(T const* A, Rank lo, Rank hi) {
    _elem = new T[_capacity = 2 * (hi - lo)];
    _size = 0;
    while(lo < hi) {
        _elem[_size++] = A[lo++];
    }
}