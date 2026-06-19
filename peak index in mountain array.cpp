#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int p_I_I_M_I_A(vector<int>& A) {
        int st=1,end=A.size()-2;

        while (st<=end)
        {
            int mid=st+(end-st)/2;
            if (A[mid-1]<A[mid] && A[mid]>A[mid+1]){
                return mid;

            }else if (A[mid-1]<A[mid]){//Right
                st=mid+1;
            }else{                     //Left
                end=mid-1;
            } 
        }
        return -1;
    }
};


int main(){
    vector<int>nums={0,1,0};
    Solution obj;
    cout<<obj.p_I_I_M_I_A(nums);

}