function print(x) {
    document.write(`Hi ${x}`)
}

function calculate(x, y, z) {
    if (y == '+'){
        document.write(x+z)
    }
    else if  (y == '-'){
        document.write(x-z)
    }
    else if  (y == 'x' || y == '*'){
        document.write(x*z)
    }
    else if  (y == '/'){
        document.write(x/z)
    }
}

function multiply(x){
    for (i = 1; i<= 12; i++){
        document.write(`<h4 align="center" class="pixel-8">${x} x ${i} = ${x*i}</h4>`)
    }
}