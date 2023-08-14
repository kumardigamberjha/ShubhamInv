gsap.from('#navbar',{duration:2, y:'-100%',ease:'bounce'})

// Testimonials AutoPlay
var swiper2 = new Swiper(".mySwiper2", {
    grabCursor: true,
    effect: "creative",
    autoplay: {
        delay: 3000,
        disableOnInteration: false,
    },
    creativeEffect: {
      prev: {
        shadow: true,
        translate: ["-120%", 0, -500],
      },
      next: {
        shadow: true,
        translate: ["120%", 0, -500],
      },
    },
  });

//   Frequently Asked Questions
const faqQuestions = document.querySelectorAll('.faq-question');

faqQuestions.forEach(question => {
  question.addEventListener('click', () => {
      const answer = question.nextElementSibling;
      answer.style.display = answer.style.display === 'block' ? 'none' : 'block';
  });
});

// Animation
document.addEventListener("DOMContentLoaded", function() {
    const animationSection = document.getElementById("animation-section");
    const animationClass = "animate__fadeInRight";
    
    function isElementInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    function handleScroll() {
        if (isElementInViewport(animationSection)) {
            animationSection.classList.add(animationClass);
        }
    }

    // Initial check on page load
    handleScroll();

    // Attach scroll event listener
    window.addEventListener("scroll", handleScroll);
});
