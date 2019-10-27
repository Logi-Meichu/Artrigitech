#include<windows.h>
#include<ctime>
#include<bits/stdc++.h>
using namespace std;

int main(){
	time_t now, last;
	char last_hit = 0;
	
	while(1){
		for(char c = 10 ; c < 128 ; c++){
			now = time(nullptr);
			if((GetAsyncKeyState(c)&0x8000) && last_hit != c){
				last_hit = c;
				last = time(nullptr);
				cout << "hit: " << c << endl;
			}
		}
		
	}
	
	return 0;
}
