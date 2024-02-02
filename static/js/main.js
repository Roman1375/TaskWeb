const addingOptions = $(".adding-options");

$(document).ready(function() {
    addingOptions.addClass("adding-options-active");
    addingOptions.each(function() {
        $(this).css("bottom", -$(this).height()-20);
    });
    addingOptions.removeClass("adding-options-active");

    $('.adding-options > a').each(function () {
        if ($(this).hasClass('active')) {
            $(this).closest('.header__menu-item').addClass('active');
        }
    });
});

const headerMenuItem = $(".header__menu-item");

headerMenuItem.mouseover(function() {
    const addingOptions =  $(this).find(".adding-options");
    if(addingOptions.length === 0) return;
    addingOptions.addClass("adding-options-active");

    setTimeout(function() {
        addingOptions.css({"opacity": "1", "transform": "translateY(0)"});
    },0);
});
headerMenuItem.mouseleave(function() {
    const addingOptions =  $(this).find(".adding-options");
    if(addingOptions.length === 0) return;
    addingOptions.css({"opacity": "0", "transform": "translateY(-20px)"});
    setTimeout(function() {
        addingOptions.removeClass("adding-options-active");
    },200);
});

$('#language-select').change(function () {
    this.form.submit();
});