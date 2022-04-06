function headers(options) {
    options = options || {}
    options.headers = options.headers || {}
    options.headers['X-Requested-With'] = 'XMLHttpRequest'
    return options
}

function refreshCaptcha(){
    let captcha = document.getElementsByClassName("captcha")
    if (captcha){
        captcha[0].addEventListener("click", function(){
            // console.log('yes');
            fetch("/captcha/refresh/", headers())
                .then(response => response.json())
                .then(function(jsonData){
                    // console.log(jsonData);
                    document.getElementsByClassName("captcha")[0].setAttribute('src', jsonData['image_url']);
                    document.getElementById("id_captcha_0").value = jsonData['key'];
                })
                .catch(error => console.log(error))
        });
    }
}
refreshCaptcha()
// $('.captcha').click(function () {
//     $.getJSON("/captcha/refresh/", function (result) {
//         $('.captcha').attr('src', result['image_url']);
//         $('#id_captcha_0').val(result['key'])
//     });
// });