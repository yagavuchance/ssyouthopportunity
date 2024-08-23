document.addEventListener('DOMContentLoaded', function () {
    const slides = document.querySelectorAll('.slider-slide');
    const sliderWrapper = document.querySelector('.slider-wrapper');
    const prevButton = document.querySelector('.prev-slide');
    const nextButton = document.querySelector('.next-slide');
    const indicators = document.querySelectorAll('.indicator');
    let currentSlide = 0;
    let isTransitioning = false;
    const transitionDuration = 500; // Duration in milliseconds

    function updateSlider(index) {
        isTransitioning = true;
        sliderWrapper.style.transform = `translateX(-${index * 100}%)`;
        indicators.forEach(indicator => indicator.classList.remove('active'));
        indicators[index % slides.length].classList.add('active');

        setTimeout(() => {
            isTransitioning = false;
        }, transitionDuration);
    }

    function nextSlide() {
        if (!isTransitioning) {
            currentSlide++;
            updateSlider(currentSlide);

            // Handle loop to first slide after the last slide
            if (currentSlide === slides.length) {
                setTimeout(() => {
                    sliderWrapper.style.transition = 'none'; // Disable transition
                    currentSlide = 0;
                    updateSlider(currentSlide); // Jump to the first slide
                    setTimeout(() => {
                        sliderWrapper.style.transition = `transform ${transitionDuration}ms ease-out`; // Re-enable transition
                    }, 50);
                }, transitionDuration);
            }
        }
    }

    function prevSlide() {
        if (!isTransitioning) {
            if (currentSlide === 0) {
                sliderWrapper.style.transition = 'none';
                currentSlide = slides.length;
                updateSlider(currentSlide - 1);
                setTimeout(() => {
                    sliderWrapper.style.transition = `transform ${transitionDuration}ms ease-out`;
                    currentSlide--;
                    updateSlider(currentSlide);
                }, 50);
            } else {
                currentSlide--;
                updateSlider(currentSlide);
            }
        }
    }

    nextButton.addEventListener('click', nextSlide);
    prevButton.addEventListener('click', prevSlide);
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            if (!isTransitioning) {
                currentSlide = index;
                updateSlider(index);
            }
        });
    });

    setInterval(nextSlide, 15000); // Auto-slide every 10 seconds
});
