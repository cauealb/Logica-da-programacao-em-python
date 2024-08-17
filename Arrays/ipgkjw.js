const minAddToMakeValid = function(s){
    const separa = s.split('')
    let array = new Array()
    let antigo
    let cont = 0

    for(let i of separa){
        if(i === '('){
            array.push(i)

        }else{
            if(antigo === '('){
                array.pop()

            }else{
                array.push(i)

            }
        }
        antigo = array[array.length - 1]
    }

    return array.length

}

minAddToMakeValid('()')