#include <bits/stdc++.h>

using namespace std;


#define LEFT(v) (2*(v))
#define RIGHT(v) (2*(v) + 1)

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}


struct query_res {
	int gcd;
	int min;
	int minCnt;

	query_res(int g, int m, int mC) : gcd(g), min(m), minCnt(mC) {};
};


struct msort_tree
{
	msort_tree(const vector<int>& arr) : n((int)arr.size()),
										 tmerge(4 * n),
										 gcds(4 * n),
										 minimums(4 * n)
	{
		build(arr, 0, n - 1, 1);
	}
	
	void build(const vector<int>& arr, int ln, int rn, int v)
	{
		if(ln == rn) 
		{
			tmerge[v] = {arr[ln]};
			gcds[v] = arr[ln];
			minimums[v] = arr[ln];
		}
		else
		{
			int mid = (ln + rn) / 2;
			build(arr, ln, mid, LEFT(v));
			build(arr, mid + 1, rn, RIGHT(v));
			combine(v);
		}
	}

	int query(int lq, int rq) {
		query_res res = querynr(lq, rq, 0, n - 1, 1);
		int ants = rq - lq + 1;
		if(res.gcd == res.min)
			return ants - res.minCnt;
		return ants;
	}
	
	query_res querynr(int lq, int rq, int ln, int rn, int v)
	{
		if(lq > rq)
			return query_res(-1, 0, 0);
		if(lq == ln && rq == rn) {
			int minCnt = upper_bound(tmerge[v].begin(), tmerge[v].end(), minimums[v]) - lower_bound(tmerge[v].begin(), tmerge[v].end(), minimums[v]);
			return query_res(gcds[v], minimums[v], minCnt);
		}
		int mid = (ln + rn) / 2;

		query_res res1 = querynr(lq, std::min(rq, mid), ln, mid, LEFT(v));
		query_res res2 = querynr(max(lq, mid + 1), rq, mid + 1, rn, RIGHT(v));

		if (res2.gcd == -1) return res1;
		else if (res1.gcd == -1) return res2;

		int newGcd = gcd(res1.gcd, res2.gcd);
		int newMin = min(res1.min, res2.min);
		int newMinCnt;
		if (res1.min == res2.min)
			newMinCnt = res1.minCnt + res2.minCnt;
		else if (res1.min < res2.min)
			newMinCnt = res1.minCnt;
		else
			newMinCnt = res2.minCnt;

		return query_res(newGcd, newMin, newMinCnt);
	}
	
	void combine(int v)
	{
		merge(tmerge[LEFT(v)].begin(), tmerge[LEFT(v)].end(), tmerge[RIGHT(v)].begin(), tmerge[RIGHT(v)].end(),
			  back_inserter(tmerge[v]));
		minimums[v] = min(minimums[LEFT(v)], minimums[RIGHT(v)]);
		gcds[v] = gcd(gcds[LEFT(v)], gcds[RIGHT(v)]);
	}
	
	int n;
	vector<vector<int>> tmerge;
	vector<int> 		gcds;
	vector<int>			minimums;
};


int main() {
    size_t n;
    std::cin >> n;
    std::vector<int> a;
    int aa;
    for(size_t i = 0; i < n; ++i) {
        std::cin >> aa;
        a.push_back(aa);
    }
    msort_tree st(a);

    size_t m;
    std::cin >> m;
    int l, r;
    for(size_t q = 0; q < m; ++q) {
        std::cin >> l >> r;
        int res = st.query(l - 1, r - 1);
		std::cout << res << std::endl;
    }

    return 0;
}