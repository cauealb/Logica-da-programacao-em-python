class UnionFind{
    constructor(size){
        this.parent = new Array(size).fill(0).map((_, index) => index)
        this.rank = new Array(size).fill(1)
    }

    find(x){
        if(this.parent[x] !== x){
            this.parent[x] = this.find(this.parent[x])
        }
        return this.parent[x];
    }

    union(x, y){
        const rootX = this.find(x)
        const rootY = this.find(y)

        if(rootX !== rootY){
            if(this.rank[rootX] > this.rank[rootY]){
                this.parent[rootY] = rootX
            } else if(this.rank[rootX] < this.rank[rootY]){
                this.parent[rootX] = rootY 
            } else{
                this.parent[rootX] = rootY
                this.rank[rootY] += 1
            }
        }
    }

    connected(x, y){
        return this.find[x] === this.find[y]
    }
}

const un = new UnionFind(6)

un.union(1, 5)
un.union(3, 4)
un.union(5, 4)

console.log(un.find(3))