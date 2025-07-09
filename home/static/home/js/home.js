document.addEventListener("DOMContentLoaded", () => {
  const section = document.querySelector('#rotator');

  if(!section) return;

  const images = [
   section.getAttribute('data-img-1'),
   section.getAttribute('data-img-2'),
  ];
  let idx = 0;

  setInterval(() => {
    // move to the next image
    idx = (idx + 1) % images.length;
    section.style.backgroundImage = `url('${images[idx]}')`;
  }, 7000);
});