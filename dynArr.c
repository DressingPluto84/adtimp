#include <stdio.h>
#include <stdlib.h>

struct dynArr {
    int *arr;
    int arrSize;
    int allocated;
};

void addElem(struct dynArr *d, int k);

int main(int argc, char* argv[]) {
    struct dynArr *darr = malloc(sizeof(struct dynArr));
    darr->arr = malloc(sizeof(int));
    darr->arrSize = 0;
    darr->allocated = 1;
    addElem(darr, 1);
    addElem(darr, 2);
    addElem(darr, 3);
    printf("%d\n", darr->arrSize);
    printf("%d\n", darr->allocated);
}

void addElem(struct dynArr *d, int k) {
    if (d->arrSize == d->allocated) {
	int *newArr = malloc(sizeof(int) * d->arrSize * 2);
	for (int i = 0; i < d->arrSize; i++) {
	    newArr[i] = d->arr[i];
	}
	d->arr = newArr;
	d->allocated = d->allocated * 2;
	
    }
    d->arr[d->arrSize] = k;
    d->arrSize += 1;
}
