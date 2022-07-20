(function () {
  'use strict'

  // Get the DOM where we want to apply Bootstrap validation
  var forms = document.querySelectorAll('.needs-validation')

  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }else {
            alert('Message sent!')
        }
        form.classList.add('was-validated')
      }, false)
    })
})()
