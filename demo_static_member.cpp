#include <iostream>
using namespace std;

class node{ //���ϥ�static member
	public:
		static int count; 
		node(){		//�غc��
			count++;
		}
			
};
int node::count = 0; //static member initialize


class Node{ //�S���ϥ�static member
	public:
		int count; 	
		Node():count(0){ //�غc��
			count++;
		}
};


int main(){
	//���ϥ�static member
	node a;
	node b;
	cout << a.count << "\n";
	a.count = 1;
	b.count = 0;
	cout << a.count << "\n";
	//�j�a��count�O�P�@��
	
	//�S���ϥ�static member
	Node A;
	Node B;
	cout << A.count << "\n";
	A.count = 1;
	B.count = 0;
	cout << A.count << "\n";
	//�j�a��count�O���P��
} 
