$(document).ready(function(){
    $('.peer-invi').hide();
  });
function goToCreateNewCampaign() {
    const url = $('#content-top-bar .go-to-create-new-campaign').val();
    window.open(url, name = '_self');
}

function goToCFPublic(url) {
    window.open(url, name = '_self');
}

$('.ms-control-icon').click(function () {
    let scrollId = $(this).attr('data-scroll-id');
    let direction = $(this).attr('data-scroll-direction');
    if (direction === 'right') {
        MagicScroll.forward(scrollId, 1);
    } else {
        MagicScroll.backward(scrollId, 1);
    }
})

function onActiveHomeSubpage($selectedTab, marginPosition){
    $('.crowdfunding-tabss').show();
    let tabLink = $selectedTab.attr('data-tab-link');
    let tagLink = $selectedTab.attr('data-tag-link');
    let doChange = false
    if (tabLink === "crowdfunding"){
        $('.peer-invi').hide();
        if (window.location.pathname !== '/dashboard/home-page'){
            
            $('.home-page .campaigns-view').removeClass('active-tab');
            $('.home-page .'+tabLink).addClass('active-tab');
            if (tagLink) {
                $("html, body").animate({scrollTop: $('#'+tagLink).offset().top - marginPosition}, '100');
            } else {
                $("html, body").animate({scrollTop: 0}, '100');
            }
        }
    }
    else if (tabLink === "peer"){
        $('.peer-invi').show();


    }
    else if (tabLink === "event"){
        // $('.peer-invi').hide();
        // $('.crowdfunding-tabss').hide();

    }
    else {
        $('.home-page .campaigns-view').removeClass('active-tab');
        $('.home-page .'+tabLink).addClass('active-tab');
        if (tagLink) {
            $("html, body").animate({scrollTop: $('#'+tagLink).offset().top - marginPosition}, '100');
        } else {
            $("html, body").animate({scrollTop: 0}, '100');
        }
    }
}

$('#content-top-bar .group-item').click(function (){
    $('.group-item').removeClass('active');
    $(this).addClass('active');
    onActiveHomeSubpage($(this), 100);
})

// on mobile dropdown tab
$("#content-top-bar .drop-down-icon").click(function () {
    $('#content-top-bar .drop-down-icon').toggleClass('d-none');
    let dropDownMenu;
    dropDownMenu = $('#content-top-bar .drop-down');
    dropDownMenu.toggleClass('d-none');
});

$('#content-top-bar .drop-down-item').click(function () {
    const text = $(this).text();
    $('#content-top-bar .selected-item span').text(text);
    $('#content-top-bar .drop-down').toggleClass('d-none');
    $('#content-top-bar .drop-down-icon').toggleClass('d-none');
    $('.tab-item-group .drop-down-item').removeClass('active');
    $(this).addClass('active');
    onActiveHomeSubpage($(this), 150);
})


$("#update").click(function(e) {
    e.preventDefault();
    
  });

  function toGetUrl(element){
    $('#output').hide();
    let url=window.location.origin+''+element.dataset.url
    let name = element.dataset.namee
    $('#current_url').val(url)
    $('#orgnamee').val(name)
  }


  $('#sendbuttoninvvite').on('click', function(e){
    var re = /^\w+([-+.'][^\s]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
    // emailformat = re.test($("#email").val())
    if (re.test($("#email").val())){
    $('#output').hide();
    $('#sendbuttoninvvite').hide();
    $('#loading-image').removeAttr("hidden");
    // $('#exampleModalCenter').modal('show'); 
    // myurl = window.location.origin+'/send-invite/'
    mydata={
        sendemail : $('#email').val(),
        url : $('#current_url').val(),
        name : $('#name').val(),
        orgnamee : $('#orgnamee').val(),
          csrfmiddlewaretoken: '{{ csrf_token }}',
          dataType: "json",
        }
     $.ajax({
            type : "POST", 
            url: window.location.origin+'/send-invite/',
            // url: ,
            data: mydata,
            success : function(json) {
                console.log("heyyyyyyy")
                // $('#exampleModalCenter').modal('show')
              //$('#loading-image').show();
              // remove the value from the input
              $('#output').text('');// remove the value from the input
              $('#output').append(json.message.content);
              $('#output').addClass('alert alert-info');
              $('#loading-image').attr("hidden","true");
              $('#sendbuttoninvvite').show();
              $('#output').show(); 
              $('.sendemailinvite').trigger("reset");
              },
              
  
              // handle a non-successful response
              error : function(xhr,errmsg,err) {
                  $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                      " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                  console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
              },
              complete: function(){
                  // $('#loading-image').hide();
            //  $('#textme').show();
            console.log("success")
  
                }
          
            });  }
        else{
            $('#output').text('');// remove the value from the input
            $('#output').append("Please Provide Valid Email");
            $('#output').addClass('alert alert-info');
            $('#output').show(); 
        }
        });