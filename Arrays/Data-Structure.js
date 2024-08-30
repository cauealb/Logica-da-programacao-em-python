class UnionFind{
    constructor(size){
        this.parent = new Array(size) .fill(0).map((_, index) => index)
        this.rank = new Array(size).fill(1)
    }

    find(x){
        if(this.parent[x] !== x){
            this.parent[x] = this.find(this.parent[x])
        }

        return this.parent[x]
    }

    union(x, y){
        const raizX = this.find(x)
        const raizY = this.find(y)

        if(raizX !== raizY){
            if(this.rank[raizX] > this.parent[raizY]){
                this.parent[raizY] = raizX
            } else if(this.rank[raizX] < this.parent[raizY]){
                this.parent[raizX] = raizY
            } else{
                this.parent[raizY] = raizX
                this.rank[raizY] += 1
            }
        }
    }

    connected(x, y){
        return this.find(x) === this.find(y)
    }
}

const union = new UnionFind(5)

union.union(1, 2);
union.union(2, 3);

union.connected(1, 3)

