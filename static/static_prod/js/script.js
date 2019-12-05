
$(document).ready(function() {
    // <!-- Display the countdown timer in an element -->
    // Set the date we're counting down to
    var n1 = document.getElementById('py-to-js-date').innerHTML;
    var n2 = document.getElementById('polled-id').innerHTML;
    console.log(n2);
    var ulr_to_redirect = '/polled/polled_itog/'+ n2 + '/'
    console.log(ulr_to_redirect);
    var countDownDate = new Date(n1).getTime();
    // console.log(countDownDate);
// py-to-js-date
    // Update the count down every 1 second
    var x = setInterval(function() {

      // Get today's date and time
      var now = new Date().getTime();

      // Find the distance between now and the count down date
      var distance = countDownDate - now;

      // Time calculations for days, hours, minutes and seconds
      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);

      // Display the result in the element with id="demo"
      document.getElementById("time_countdown").innerHTML = hours + "h "
      // document.getElementById("time_countdown").innerHTML = days + "d " + hours + "h "
      + minutes + "m " + seconds + "s ";

      // If the count down is finished, write some text
      if (distance < 0) {
        clearInterval(x);
        document.getElementById("time_countdown").innerHTML = "EXPIRED";
        window.location.replace(ulr_to_redirect);
      }
    }, 1000);
});
