const swiper = new Swiper('.swiper', {
	slidesPerView: 1,
	slidesPerGroup: 1,
	spaceBetween: 30,
  loop: true,
  navigation: {
    nextEl: '.button-next',
    prevEl: '.button-prev',
  },
	pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
		clickable: true
  }
});