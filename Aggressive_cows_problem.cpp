#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool ispossible(vector<int>&arr,int n,int c,int mat){
    int cows=1,laststalpos=arr[0];
    for(int i=1;i<n;i++){
        if(arr[i]-laststalpos>=mat){
            cows++;
            laststalpos=arr[i];

        }
        if(cows==c){
            return true;
        }
    }
    return false;
}

int getdistance(vector<int>&arr,int n,int c){
    sort(arr.begin(),arr.end());
    int st=0,end=arr[n-1]-arr[0];
    int ans=-1;
    while(st<=end){
        int mid=st+(end-st)/2;
        if(ispossible(arr,n,c,mid)){//right
            ans=mid;
            st=mid+1;
        }
        else{//left
            end=mid-1;
        }
    }
    return ans;
}

int main(){
    int n=5,c=2;
    vector<int>arr={1,2,8,4,9};
    cout<<getdistance(arr,n,c)<<endl;
    return 0;
}