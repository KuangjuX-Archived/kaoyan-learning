typedef int Rank;

#define DEFAULT_CAPACITY 3

// 向量模板类
template <typename T> class Vector {
protected:
    Rank _size; int _capacity; T* _elem;

    void copyFrom(T const* A, Rank lo, Rank hi); // 复制数组区间 A[lo, hi)
};