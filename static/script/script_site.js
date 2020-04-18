// Init des animations sur le texte quand on scroll
AOS.init();

// Agrangir ou retrecir la navbar
$(window).on('scroll', function() {
  if ($(window).scrollTop() > 60) {
    $('.navbar').removeClass('nav-expended').addClass('nav-collapsed')
  } else {
    $('.navbar').removeClass('nav-collapsed').addClass('nav-expended')
  }
})

// Montrer ou acher le bouton pour remonter en haut
$(window).on('scroll', function() {
  if ($(window).scrollTop() > 300) {
    $('.btn-top').removeClass('hide').addClass('show')
  } else {
    $('.btn-top').removeClass('show').addClass('hide')
  }
})

$(window).scroll(function() {
  if ($(window).scrollTop() + $(window).height() > $(document).height() - 80) {
    $('#window').css('bottom', '90px')
    $('.btn-top').css('bottom', '90px')
  } else {
    $('#window').css('bottom', '10px')
    $('.btn-top').css('bottom', '10px')
  }
})

// Revenir tout en haut
$('.btn-top').on('click', function() {
  $(window).scrollTop(0)
})

// Ajustement mobiles
function mobileViewUpdate() {
  if ($(window).width() <= 991) {
    $('.btn-top').hide()
    $('.container').removeClass('col-8').addClass('col-12')
    $('.div-nav').removeClass('offset-2 col-8').addClass('col-12')
    $('#window').width('100%').css('right', '0px')
    $('#window').css('bottom', '0px')

    $(window).scroll(function() {
      if ($(window).scrollTop() + $(window).height() > $(document).height() - 80) {
        $('#window').css('bottom', '100px')
      } else {
        $('#window').css('bottom', '0px')
      }
    })
  } else {
    $('.btn-top').show()
    $('.container').removeClass('col-12').addClass('col-8')
    $('.div-nav').removeClass('col-12').addClass('offset-2 col-8')
    $('#window').width('350px').css('right', '10px')
    $('#window').css('bottom', '10px')

    $(window).scroll(function() {
      if ($(window).scrollTop() + $(window).height() > $(document).height() - 80) {
        $('#window').css('bottom', '90px')
        $('.btn-top').css('bottom', '90px')
      } else {
        $('#window').css('bottom', '10px')
        $('.btn-top').css('bottom', '10px')
      }
    })
  }
}
$(window).resize(mobileViewUpdate);

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
