# include <bits/stdc++.h>
using namespace std;
int main(){
    int val;
    cin >> val;
    int num[val];
    for(int i = 0 ; i < val ; i++){
        cin >> num[i] ;
    }
    for (int i = 0; i < val - 1; i++) {
    for (int j = 0; j < val - i - 1; j++) {
        if (num[j] > num[j + 1]) {
            int temp = num[j];
            num[j] = num[j + 1];
            num[j + 1] = temp;
            }
        }
    }
    for (int n = 0; n < val; n++) {
        cout << num[n] << "  ";
    }
    return 0;
}
