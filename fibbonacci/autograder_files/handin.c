#include <stdio.h>
int main() {
	int n, next = 0, cur = 0, prev = 1, T;
	scanf("%d", &T);
	while(T--) {
		scanf("%d", &n);
		while(n--) {
			next = cur + prev;
			prev = cur;
			cur = next;
		}		
		printf("%d\n", cur);
	}
	return 0;
}
