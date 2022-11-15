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
        document.write(`<h1 align="center" class="digital text-danger">${x} x ${i} = ${x*i}</h1>`)
    }
}

$(function() {
    $('#menu-title a').click(function(){
        $('#btn-title').text($(this).text());
    });
});

