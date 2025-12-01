let nums = [2, 7, 11, 15];
let target = 9;
let nj = [];

function twoSums() {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) { 
            if (nums[i] + nums[j] === target) {
                nj.push(i);
                nj.push(j)
            }
        }
    }
}

twoSums();
console.log(nj)


