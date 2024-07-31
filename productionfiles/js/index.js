// static/js/index.js

function initializeCountdown(deadline, elementId) {
    var deadlineDate = new Date(deadline).getTime();

    var x = setInterval(function() {
        var now = new Date().getTime();
        var distance = deadlineDate - now;

        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById(elementId).innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

        if (distance < 0) {
            clearInterval(x);
            document.getElementById(elementId).innerHTML = "EXPIRED";
        }
    }, 1000);
}

document.addEventListener("DOMContentLoaded", function() {
    var countdownElements = document.querySelectorAll('[data-deadline]');

    countdownElements.forEach(function(element) {
        var deadline = element.getAttribute('data-deadline');
        var elementId = element.getAttribute('id');
        initializeCountdown(deadline, elementId);
    });
});
