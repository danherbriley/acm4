#include <bits/stdc++.h>
#include <cmath>


using namespace std;


#define LEFT(v) (2*(v))
#define RIGHT(v) (2*(v) + 1)

enum Op { _or , _xor };

struct seg_tree
{
	seg_tree(const vector<int>& arr) : n((int)arr.size()),
									   t(4 * n),
                                       rootOp((int(log2((int)arr.size())) % 2 == 0) ? _xor : _or)
	{
		build(arr, 0, n - 1, 1, rootOp);
	}
	int query(int l, int r)
	{
		return query(l, r, 0, n - 1, 1, rootOp);
	}
	int get(int i)
	{
		return query(i, i);
	}
	void set(int i, int val)
	{
		set(i, val, 0, n - 1, 1, rootOp);
	}
 private:
	void build(const vector<int>& arr, int ln, int rn, int v, Op op)
	{
		if(ln == rn)
			t[v] = arr[ln];
		else
		{
			int mid = (ln + rn) / 2;
            Op op2 = (op == _or) ? _xor : _or;
			build(arr, ln, mid, LEFT(v), op2);
			build(arr, mid + 1, rn, RIGHT(v), op2);
            switch(op) {
                case _or : t[v] = t[LEFT(v)] | t[RIGHT(v)]; break;
                case _xor : t[v] = t[LEFT(v)] ^ t[RIGHT(v)]; break;
            }
		}
	}
	void set(int i, int val, int ln, int rn, int v, Op op)
	{
		if(ln == rn)
			t[v] = val;
		else
		{
			int mid = (ln + rn) / 2;
            Op op2 = (op == _or) ? _xor : _or;
			if(i <= mid)
				set(i, val, ln, mid, LEFT(v), op2);
			else
				set(i, val, mid + 1, rn, RIGHT(v), op2);

            switch(op) {
                case _or : t[v] = t[LEFT(v)] | t[RIGHT(v)]; break;
                case _xor : t[v] = t[LEFT(v)] ^ t[RIGHT(v)]; break;
            }
		}
	}
	int query(int lq, int rq, int ln, int rn, int v, Op op)
	{
		if(lq > rq)
			return 0;
		if(lq == ln && rq == rn)
			return t[v];
		int mid = (ln + rn) / 2;

        switch (op) {
            case _or : return query(lq, min(rq, mid), ln, mid, LEFT(v), _xor)
                        |
			            query(max(lq, mid + 1), rq, mid + 1, rn, RIGHT(v), _xor); break;
            case _xor : return query(lq, min(rq, mid), ln, mid, LEFT(v), _or)
                        ^
			            query(max(lq, mid + 1), rq, mid + 1, rn, RIGHT(v), _or); break;
            default : std::cout << "Chyba" << std::endl; return 0; break;
        }

	}
	int n;
	vector<int> t;
    Op rootOp;
};


int main() {
    size_t n, m;
    std::cin >> n >> m;
    size_t l = pow(2, n);
    std::vector<int> a;
    int aa;
    for(size_t i = 0; i < l; ++i) {
        std::cin >> aa;
        a.push_back(aa);
    }
    seg_tree st(a);

    int p, b, v;
    for(size_t q = 0; q < m; ++q) {
        std::cin >> p >> b;
        st.set(p - 1, b);
        v = st.query(0, l - 1);
        std::cout << v << std::endl;
    }

    return 0;
}