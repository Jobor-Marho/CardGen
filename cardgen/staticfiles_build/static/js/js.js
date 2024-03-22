//Message



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

var pwdbtn = $('#showPwords')
pwdbtn.on('click', () => {
    oldpwd = document.getElementById('oldpwd')
    pwd1 = document.getElementById('pwordd')
    pwd2 = document.getElementById('pwordd2')
    if(pwd1.type == 'password' && pwd2.type == 'password' && oldpwd.type == 'password'){
        pwd1.type = pwd2.type = oldpwd.type = 'text';
    }
    else{
        pwd1.type = pwd2.type = oldpwd.type = 'password';
    }
})

function showerror(mesg){
    var header = document.getElementById('header')
    var msg = document.createElement('div')
    msg.classList.add('message');msg.classList.add('text-center');msg.classList.add('alert');msg.classList.add('alert-danger');msg.classList.add('alert-dismissible');msg.classList.add('fade');msg.classList.add('show');
    msg.setAttribute('role', 'alert')
    var strong = document.createElement('strong')
    var i = document.createElement('i')
    i.classList.add('bi');i.classList.add('bi-exclamation-triangle-fill');
    strong.appendChild(i)
    strong.appendChild(document.createTextNode(`${mesg}`))
    var button = document.createElement('button');
    button.setAttribute('type', 'button');
    button.setAttribute('data-bs-dismiss', 'alert');
    button.setAttribute('aria-label', 'Close');
    button.classList.add('btn-close');

    msg.appendChild(strong)
    msg.appendChild(button)
    header.appendChild(msg)
    
}



// Login
var login_btn = $('#login-btn')
login_btn.on('click', function(){
    const spinner = $('#spinners')
    spinner.removeClass('visually-hidden')
    $('#btn-text').text('Authenticating')
    login_btn.disabled = true
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
                    login_btn.disabled = false
                    
                }else if(response.status == 'register'){
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Log In')
                    login_btn.disabled = true
                    window.location.href  = '/signup'
                }else{
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Success')
                    login_btn.disabled = true
                    window.location.href  = '/build'
                }
            },
        error: function(error){
            spinner.addClass('visually-hidden')
            $('#btn-text').text('Log In')
            login_btn.disabled = false
        },
    });
})

//Register
var prof_btn = $('#prof-btn')
prof_btn.on('click', function(){
    const spinner = $('#spinners')
    spinner.removeClass('visually-hidden')
    $('#btn-text').text('Saving')
    prof_btn.disabled = true
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
                    prof_btn.disabled = false
                    
                }else if(response.status == 'exist'){
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Save')
                    prof_btn.disabled = true
                    window.location.href  = '/login'
                }else{
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Success')
                    prof_btn.disabled = true
                    window.location.href  = '/auth'
                }
            },
        error: function(error){
            spinner.addClass('visually-hidden')
            $('#btn-text').text('Save')
            prof_btn.disabled = false
        },
    });
})

// Auth Validation

var validate_btn = $('#validate-btn')
validate_btn.on('click', function(){
    const spinner = $('#spinners')
    spinner.removeClass('visually-hidden')
    $('#btn-text').text('Validating')
    validate_btn.disabled = true
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
                    validate_btn.disabled = false
                    
                }else{
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Success')
                    validate_btn.disabled = true
                    window.location.href  = '/build'
                }
            },
        error: function(error){
            spinner.addClass('visually-hidden')
            $('#btn-text').text('Validate')
            validate_btn.disabled = false
        },
    });
})

//Change Password
var change_btn = $('#change-btn')
change_btn.on('click', function(){
    const spinner = $('#spinners')
    spinner.removeClass('visually-hidden')
    $('#btn-text').text('Changing')
    change_btn.disabled = true
    $.ajax({
        type: 'POST',
        url: '/changepassword/',
        data: {
            oldpwd: $('#oldpwd').val(),
            pword: $('#pwordd').val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
        },
        success: function(response){
                if(response.status == 'error'){
                    spinner.addClass('visually-hidden')
                    $('#btn-text').text('Change')
                    showerror(response.msg)
                    change_btn.disabled = false
                    
                }else{
                    spinner.addClass('visually-hidden')
                    change_btn.disabled = true
                    $('#btn-text').text('Success')
                    window.location.href  = '/login'
                    
                }
            },
        error: function(error){
            spinner.addClass('visually-hidden')
            $('#btn-text').text('Change')
            change_btn.disabled = false
        },
    });
})


