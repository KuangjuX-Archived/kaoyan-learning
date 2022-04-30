#include "vector.h"

template <typename T> 
void Vector<T>::copyFrom(T const* A, Rank lo, Rank hi) {
    _elem = new T[_capacity = 2 * (hi - lo)];
    _size = 0;
    while(lo < hi) {
        _elem[_size++] = A[lo++];
    }
}

// 向量不足时扩容
template <typename T> void Vector<T>::expand() {
    if(_size < _capacity)return;
    if(_capacity < DEFAULT_CAPACITY) _capacity = DEFAULT_CAPACITY;
    T* oldElem = _elem;
    // 容量加倍
    _elem = new T[_capacity <<= 1];
    for(int i = 0; i < _size; i++){
        _elem[i] = oldElem[i];
    }
    delete [] oldElem;
}

// 装填因子过小时压缩向量所占空间
template <typename T> void Vector<T>::shrink() {
    // 装填因子过小时压缩向量所占空间
    if(_capacity < DEFAULT_CAPACITY << 1) return;
    if(_size << 2 > _capacity) return; // 以 25% 为界
    T* oldElem = _elem;
    _elem = new T[_capacity >>= 1];
    for(int i = 0; i < _size; i++) _elem[i] = oldElem[i];
    delete [] oldElem;
}

// 直接引用元素
template <typename T> T& Vector<T>::operator[] (Rank r) const {
    return _elem[r];
}

// 置乱算法
template <typename T> void permute(Vector<T>& V) {
    // 随机置乱算法
    for(int i = V.size(); i > 0; i--){
        std::swap(V[i - 1], V[std::rand() % i]);
    }
}

// 区间置乱接口
template <typename T> void Vector<T>::unsort(Rank lo, Rank hi) {
    // 等概率随机置乱区间[lo, hi)
    T* V = _elem + lo;
    for(Rank i = hi - lo; i > 0; i--) {
        std::swap(V[i - 1], V[std::rand() % i]);
    }
}

// 无序向量的顺序查找
template <typename T> 
Rank Vector<T>::find(T const& e, Rank lo, Rank hi) const {
    while((lo < hi--) && (e != _elem[hi]));
    return hi;
}

// 插入算法
template <typename T> 
Rank Vector<T>::insert(Rank r, T const& e) {
    // 若有必要，先扩容
    expand();
    for(int i = _size; i > r; i--) _elem[i] = _elem[i - 1];
    _elem[i] = e;
    _size++;
    return r;
}

// 删除区间元素
template <typename T> int Vector<T>::remove(Rank lo, Rank hi) {
    // 删除区间 [lo, hi)
    if(lo == hi) return 0; // 处于效率考虑，单独处理退化情况
    while(hi < _size) _elem[lo++] = _elem[hi++];
    _size = lo; // 更新规模，直接丢弃尾部内容
    shrink();
    return hi - lo;
}

// 单元素删除
template <typename T> T Vector<T>::remove( Rank r ){
    T e = _elem[r];
    remove(r, r + 1);
    return e;
}

// 不变性: [0, i) 中元素彼此互异
// 删除无序向量中重复元素(高效版)
// 复杂度 O(n^2)
template <typename T> int Vector<T>::deduplicate() {
    int oldSize = _size;
    Rank i = 1;
    // 从前向后遍历，从其前缀中找到若干雷同，若无雷同则向后考察，否则删除雷同者
    while(i < _size) (find(_elem[i], 0, i) < 0)? i++: remove(i);
    return oldSize - _size
}

// 遍历
// 借助函数指针机制
template <typename T> void Vector<T>::traverse(void(*visit)(T&)) {
    for(int i = 0; i < _size; i++) {
        visit(_elem[i]);
    }
}

template <typename T> template <typename VST>
void Vector<T>::traverse(VST& visit) {
    // 借助函数对象机制
    for(int i = 0; i < _size; i++) {
        visit(_elem[i]);
    }
}

// 返回向量中逆序相邻元素对的总数
template <typename T> int Vector<T>::disordered() const {
    int n = 0;
    for(int i = 1; i < _size; i++) {
        if(_elem[i - 1] > _elem[i]) n++;
    }
    return n;
}

// 有序向量重复元素剔除算法(高效版)
// 复杂度可以降到 O(n)
template <typename T> int Vector<T>::uniquify() {
    Rank i = 0, j = 0;
    while(++j < _size) {
        if(_elem[i] != _elem[j]) {
            _elem[++i] = _elem[j];
        }
    }
    _size = ++i;
    shrink(); // 直接截取尾部多余元素
    return j - i; 
}

template <typename T> Rank Vector<T>::search(T const& e, Rank lo, Rank hi) const {
    
}

