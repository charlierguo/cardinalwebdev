;(function ($, window, undefined) {

  /* Image Bounce Effect */
  $('.topics img, .photo').click(function() {
    var $img = $(this);
    $img.addClass('bounce');
    window.setTimeout( function() {
      $img.removeClass('bounce');
    }, 1000);
  });

  /* Apply Button Reveal Application */
  $('button.apply, a.apply').click(function(e) {
    e.preventDefault();
    var app = $(this).parent().parent().next();
    if (!app.hasClass('app-wrapper')) {
      app = $(this).parent().parent().parent().next();
    }
    app.slideDown();
    $('html, body').animate({
      scrollTop: app.offset().top + 50
    }, 800);
  });

  /* Submit Application */
  $('.application form').live('submit', function(e) {
    e.preventDefault();
    var offset = $(this).parent().parent().parent().parent().offset().top + 50;
    $.ajax({
      type: 'POST',
      url: '/',
      data: $(this).serialize(),
      success: function(data) {
        if (data['status'] === 'success') {
          $('.application form').html('');
          $('.application h3.msg').fadeIn();
        } else {
          $('.app-wrapper').html(data);
        }
        $('html, body').animate({
          scrollTop: offset
        }, 800);
      }
    });
  });

  /* ZURB Foundation Javascript Initialization */
  var $doc = $(document);
  var Modernizr = window.Modernizr;

  $(document).ready(function() {
    $.fn.foundationAlerts           ? $doc.foundationAlerts() : null;
    $.fn.foundationButtons          ? $doc.foundationButtons() : null;
    $.fn.foundationAccordion        ? $doc.foundationAccordion() : null;
    $.fn.foundationNavigation       ? $doc.foundationNavigation() : null;
    $.fn.foundationTopBar           ? $doc.foundationTopBar() : null;
    $.fn.foundationCustomForms      ? $doc.foundationCustomForms() : null;
    $.fn.foundationMediaQueryViewer ? $doc.foundationMediaQueryViewer() : null;
    $.fn.foundationTabs             ? $doc.foundationTabs({callback : $.foundation.customForms.appendCustomMarkup}) : null;
    $.fn.foundationTooltips         ? $doc.foundationTooltips() : null;
    $.fn.foundationMagellan         ? $doc.foundationMagellan() : null;
    $.fn.foundationClearing         ? $doc.foundationClearing() : null;
    $.fn.placeholder                ? $('input, textarea').placeholder() : null;
  });

  $('#featured').orbit();
  $('input, textarea').placeholder();

  // UNCOMMENT THE LINE YOU WANT BELOW IF YOU WANT IE8 SUPPORT AND ARE USING .block-grids
  // $('.block-grid.two-up>li:nth-child(2n+1)').css({clear: 'both'});
  // $('.block-grid.three-up>li:nth-child(3n+1)').css({clear: 'both'});
  // $('.block-grid.four-up>li:nth-child(4n+1)').css({clear: 'both'});
  // $('.block-grid.five-up>li:nth-child(5n+1)').css({clear: 'both'});

  // Hide address bar on mobile devices (except if #hash present, so we don't mess up deep linking).
  if (Modernizr.touch) {
    $(window).load(function () {
      setTimeout(function () {
        window.scrollTo(0, 1);
      }, 0);
    });
  }

  /* -----------------------------------------
     AUTO-SETS CSRF TOKEN FOR AJAX CALLS
  ----------------------------------------- */

  // Acquiring CSRF token and setting it to X-CSRFToken header for AJAX POST Request
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type)) {
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
      }
    }
  });

})(jQuery, this);