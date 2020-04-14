// Init des animations sur le texte quand on scroll
AOS.init();

// Bouton qui copie le lien de l'iframe
new ClipboardJS('.btn')

// Navbar
$(window).on('scroll', function() {

  
  if ($(window).scrollTop() > 60) {
    $('.navbar').removeClass('nav-expended').addClass('nav-collapsed')
  } else {
    $('.navbar').removeClass('nav-collapsed').addClass('nav-expended')
  }
})

// Bouton pour retourner tout en haut
$(window).on('scroll', function() {
  if ($(window).scrollTop() > 300) {
    $('.btn-top').removeClass('hide').addClass('show')
  } else {
    $('.btn-top').removeClass('show').addClass('hide')
  }
})
$(window).on('scroll', function() {
  if ($(window).scrollTop() > 2000) {
    $('.btn-top').css('bottom', '110px')
  } else {
    $('.btn-top').css('bottom', '30px')
  }
})

// Revenir tout en haut
$('.btn-top').on('click', function() {
  $(window).scrollTop(0)
})



// Ajustement mobiles
function mobileViewUpdate() {
  if ($(window).width() <= 991) {
    $('.container').removeClass('col-8').addClass('col-12')
    $('.div-nav').removeClass('offset-2 col-8').addClass('col-12')

    $(window).on('scroll', function() {
      if ($(window).scrollTop() > 1400) {
        $('.btn-top').css('bottom', '100px')
      } else {
        $('.btn-top').css('bottom', '30px')
      }

    })
  } else {
    $('.container').removeClass('col-12').addClass('col-8')
    $('.div-nav').removeClass('col-12').addClass('offset-2 col-8')
  }
}
$(window).resize(mobileViewUpdate);
