<script>
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Show the spinner
    document.getElementById('spinner').style.display = 'block';

    // Simulate a delay for the analysis (3 seconds)
    setTimeout(function() {
        // Hide the spinner
        document.getElementById('spinner').style.display = 'none';

        // Show the popup
        document.getElementById('overlay').style.display = 'block';
        document.getElementById('popup').style.display = 'block';
    }, 3000);
});

document.getElementById('popup-button').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('popup').style.display = 'none';
});
</script>
