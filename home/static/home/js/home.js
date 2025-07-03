document.addEventListener("DOMContentLoaded", () => {
  const section = document.querySelector('.category-section');
  const images = [
    "{{ category.image_url }}",
    "{% static 'images/overlay.png' %}"
  ];
  let idx = 0;

  setInterval(() => {
    // move to the next image
    idx = (idx + 1) % images.length;
    section.style.backgroundImage = `url('${images[idx]}')`;
  }, 7000);
});