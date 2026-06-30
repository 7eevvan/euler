#include <bits/stdc++.h>
using namespace std;
#define int long long
#define sz(x) ((int)(x).size())


int gcd(int x, int y) {
    if (x == 0) {
        return y;
    }
    return gcd(y % x, x);
}

void solve() {
    int n;
    cin >> n;
    vector<int> lengths(n);
    for (int i = 0; i < n; i++) {
        cin >> lengths[i];
    }
    sort(lengths.begin(), lengths.end());

    int res = 0;
    for (int i = 0; i < n/2; i++) {
        res += (lengths[n-1-i] - lengths[i]);
    }
    cout << res << endl;

}
 
signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();
}