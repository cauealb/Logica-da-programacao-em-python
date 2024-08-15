var removeOuterParentheses = function(s) {
    const trus = s.split('')
    let array = []
    let cont = 0

    for(let i of trus){
        if(i === '('){
            if(cont > 0){
                array.push(i)
            }
            cont++
        }else{
            cont--
            if(cont > 0){
                array.push(i)
            }
        }

    }

    let string = array.join('')
    return string
};






removeOuterParentheses('(()())(())(()(()))')