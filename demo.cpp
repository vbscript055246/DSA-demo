#include <iostream>
using namespace std;

class node{
	public:
		static int count;
		node(){		//�غc�禡 
			count++;
		}
			
};
int node::count = 0; //static member initialize


class Node{
	public:
		int count; 	//�غc�禡 
		Node():count(0){
			count++;
		}
};


int main(){
	
	node a;
	node b;
	cout << a.count << "\n";
	a.count = 1;
	b.count = 0;
	cout << a.count << "\n";
	
	
	Node A;
	Node B;
	cout << A.count << "\n";
	A.count = 1;
	B.count = 0;
	cout << A.count << "\n";
} 
