//Message

var msg = $('.message')
msg.fadeOut(5000)

var show = $('#show')
show.on('click', function(){
    pwd1 = document.getElementById('pword')
    pwd2 = document.getElementById('pword2')

    if(pwd1.type && pwd2.type == 'password'){
        pwd1.type = pwd2.type = 'text';
    }else{
        pwd1.type = pwd2.type = 'password';
    }
})

var show_pwd = $('#show_pwd')
show_pwd.on('click', function(){
    pwd = document.getElementById('pword')
    if(pwd.type  == 'password'){
        pwd.type = 'text';
    }else{
        pwd.type = 'password';
    }
})

function showerror(mesg){
    var header = document.getElementById('header')
    var msg = document.createElement('div')
    msg.classList.add('message');msg.classList.add('text-center');msg.classList.add('alert');msg.classList.add('alert-danger');
    var i = document.createElement('i')
    i.innerText = `${mesg}`
    i.classList.add('fst-normal');i.classList.add('bi');i.classList.add('bi-exclamation-triangle-fill');
    msg.appendChild(i)
    header.appendChild(msg)
    var msg = $('.message')
    msg.fadeOut(5000)
}



// Login
var login_btn = $('#login-btn')
login_btn.on('click', function(){
    const spinner = $('#spinners')
    spinner.removeClass('visually-hidden')
    $('#btn-text').text('Authenticating')
    $.ajax({
        type: 'POST',
        url: '/login/',
        data: {
            username: $('#username').val(),
            pword: $('#pword').val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
        },
        success: function(response){
                if(response.status == 'error'){
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Log In')
                    showerror(response.msg)
                    
                }else if(response.status == 'register'){
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Log In')
                    window.location.href  = '/signup'
                }else{
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Success')
                    window.location.href  = '/build'
                }
            },
        error: function(error){
            spinner.addClass('visually-hidden')
            $('#btn-text').text('Log In')
        },
    });
})

//Register
var prof_btn = $('#prof-btn')
prof_btn.on('click', function(){
    const spinner = $('#spinners')
    spinner.removeClass('visually-hidden')
    $('#btn-text').text('Saving')
    $.ajax({
        type: 'POST',
        url: '/signup/',
        data: {
            username: $('#username').val(),
            businessName: $('#businessName').val(),
            pword: $('#pword').val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
        },
        success: function(response){
                if(response.status == 'error'){
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Save')
                    showerror(response.msg)
                    
                }else if(response.status == 'exist'){
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Save')
                    window.location.href  = '/login'
                }else{
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Success')
                    window.location.href  = '/auth'
                }
            },
        error: function(error){
            spinner.addClass('visually-hidden')
            $('#btn-text').text('Save')
        },
    });
})

// Auth Validation

var validate_btn = $('#validate-btn')
validate_btn.on('click', function(){
    const spinner = $('#spinners')
    spinner.removeClass('visually-hidden')
    $('#btn-text').text('Validating')
    $.ajax({
        type: 'POST',
        url: '/auth/',
        data: {
            auth: $('#auth').val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
        },
        success: function(response){
                if(response.status == 'error'){
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Validate')
                    showerror(response.msg)
                    
                }else{
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Success')
                    window.location.href  = '/build'
                }
            },
        error: function(error){
            spinner.addClass('visually-hidden')
            $('#btn-text').text('Validate')
        },
    });
})


