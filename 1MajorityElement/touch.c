#include<stdio.h>
#define NUM 3
//1
void printArray(int *array, int num){
	for(int i = 0; i < num; i++){
		printf("%d ", array[i]);
	}
	printf("\n");
}

void swap(int *array, int i, int j){
	//a = a+b
	//b = a-b = a
	//a = a-b = b
	array[i] += array[j];
	array[j] = array[i] - array[j];
	array[i] -= array[j];
}
void sort(int *array, int num){
	if(num <= 1)
		return ;
	int flag = array[0];
	int i = 0, j = num - 1;
	while(i < j){
		while(j > i && array[j] >= flag)
			j--;
		if(array[j] < flag){
			swap(array, i, j);
		}
		while(i < j && array[i] < flag)
			i++;
		if(array[i] > flag){
			swap(array, i, j);
		}
	}
	sort(array, i);
	sort(array+i+1, num-i-1);
}

int majorityElement1(int* nums, int numsSize) {
		sort(nums, numsSize);
		//printArray(nums, NUM);
		return nums[numsSize/2];
}

//2 Moore voting algorithm
//O(n) time and O(1) space

int majorityElement(int* nums, int numsSize) {
		int judging = nums[0];
		int i = 0, count = 0;
		while(i < numsSize){
			if(count == 0){
				judging = nums[i];
				count = 1;
				i++;
				continue;
			}
			if(judging == nums[i]){
				count++;
			}
			else count--;
			i++;
		}
		return judging;
}


int main(){
	int array[NUM] = {6,5,5} ;	
	printf("%d\n",majorityElement(array, NUM));
	return 0;
}