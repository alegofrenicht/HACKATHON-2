$(window).on('load', function() {
  $('.welcome').addClass('fade-in');
});


let selectedMovies = []
document.addEventListener('DOMContentLoaded', function() {
    const clickers = document.querySelectorAll('.clicker')
    clickers.forEach(function(clicker) {
        clicker.addEventListener('click', function(event) {
            event.preventDefault()
            let movie = clicker.dataset.movie
            let toggle = clicker.classList.toggle(movie)
            if (toggle === true) {
                selectedMovies.push(movie)
            }
            else if (toggle === false) {
                const index = selectedMovies.indexOf(movie)
                selectedMovies.splice(index, 1)
            }
    })
    });
});


document.addEventListener('DOMContentLoaded', function() {
  const submitBtn = document.querySelector('.submit-btn');
  submitBtn.addEventListener('click', function(event) {
    event.preventDefault();

    if (selectedMovies.length < 3) {
        Swal.fire('Please select at least 3 movies')
    }
    else {
        fetch(`/home/add_movies`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(selectedMovies)
    })
    .then(response => {
        Swal.fire('Thank you!', 'These movies have been added to your watchlist and will affect your recommendations.')
            .then(() => {
                window.scrollTo({top: 0, behavior: 'smooth'});
                window.location.reload();
            });
        });
    }
  });
});


