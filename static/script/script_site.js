// Init des animations sur le texte quand on scroll
AOS.init();

$(window).scroll(function() {
  if ($(window).scrollTop() + $(window).height() > $(document).height() - 80) {
    $('#window').css('bottom', '9%')
    $('.btn-to-chat').css('bottom', '15%')
    $('.btn-top').css('bottom', '9%')
  } else {
    $('#window').css('bottom', '10px')
    $('.btn-to-chat').css('bottom', '10px')
    $('.btn-top').css('bottom', '10px')
  }
})

// Revenir tout en haut
$('.btn-top').on('click', function() {
  $(window).scrollTop(0)
})

// Ajustement mobiles
if ($(window).width() <= 991) {

  $('.btn-top').hide()
  $('.btn-to-chat').show()
  $('#window').hide()

  $('.container').removeClass('col-8').addClass('col-12')
  $('.div-nav').removeClass('offset-2 col-8').addClass('col-12')

  $('[data-aos]').removeAttr('data-aos')

  $('#video').css('width', '98%')

} else {

  $('.btn-top').show()
  $('.btn-to-chat').hide()
  $('#window').show()
  $('.container').removeClass('col-12').addClass('col-8')
  $('.div-nav').removeClass('col-12').addClass('offset-2 col-8')

  // Montrer ou cacher le bouton pour remonter en haut
  $(window).on('scroll', function() {
    if ($(window).scrollTop() > 300) {
      $('.btn-top').css('display', 'block')
    } else {
      $('.btn-top').css('display', 'none')
    }
  })

  // Agrangir ou retrecir la navbar
  $(window).on('scroll', function() {
    if ($(window).scrollTop() > 60) {
      $('.navbar').removeClass('nav-expended').addClass('nav-collapsed')
    } else {
      $('.navbar').removeClass('nav-collapsed').addClass('nav-expended')
    }
  })

  // Minimiser ou maximiser la fenêtre chatbot
  $(document).ready(function() {
    $("#min_max_button").click(function() {
      if ($('#icon-toggle').hasClass('fa-window-minimize')) {
        $('#icon-toggle').toggleClass('fa-window-minimize', false).toggleClass('fa-window-maximize');
      } else {
        $('#icon-toggle').toggleClass('fa-window-maximize', false).toggleClass('fa-window-minimize');
      }
      $('#box').slideToggle();
    });
  });
}
