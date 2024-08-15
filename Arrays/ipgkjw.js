var removeOuterParentheses = function(s) {
    const trus = s.split('')
    let array = []
    let antigo

    for(let i = 0; i < trus.length; i++){
        antigo = i - 1
        if(array.length >= 1){
            if(trus[i]!== trus[antigo])
                array.push(trus[i])

        }else if(){

        }
        
        
        else{
            if(trus[i] === trus[antigo]){
                array.push(trus[i])
            }
        }
    }

    let string = array.join('')
    return string
};






removeOuterParentheses('(()(()))')