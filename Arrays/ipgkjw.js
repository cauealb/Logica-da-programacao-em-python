const isValid = function(s){
    const splitA = s.split('')
    let array = []
    let j 
    for(let i = 0; i < splitA.length; i++){
    
        if(splitA[i] === '(' || splitA[i] === '{' || splitA[i] === '['){
            array.push(splitA[i])
        }
        else{
            if(array.length === 0){
                return true;;
            }
    
            j = array.length - 1
            switch (array[j]){
                case '(':
                    if(splitA[i] === ')'){
                        array.pop()
                    }else{
                        return false;
                    }
                    break;
                case '{':
                    if(splitA[i] === '}'){
                        array.pop()
                    }else{
                        return false;
                    }
                    break;
                case '[':
                    if(splitA[i] === ']'){
                        array.pop()
                    }else{
                        return false;
                    }
                    break;
                default:
                    return false;
            }
        }
    }
    if(j !== 0){
        return false;
    }
    return true;
}

isValid(']')