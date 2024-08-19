window.addEventListener('load', function() {
    var alertBox = document.querySelector('.alert');
// After 3 seconds, hide the alert box
    setTimeout(function() {
        alertBox.classList.add('fade-out');
        alertBox.addEventListener('animationend', function() {
            alertBox.remove();
        });
        
}, 2000); 
});