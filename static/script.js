$(document).ready(function() {
    $('#calorieForm').submit(function(e) {
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/generate_calories',
            data: $(this).serialize(),
            success: function(response) {
                $('#result').text(response.generated_info);
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    });
});
