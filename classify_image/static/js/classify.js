$(document).ready(function() { 
    var isLoading=false;
      $(function() {
    
        $("#clear").click(function() {
              $('#predic').hide();
              $('.editable').hide();
              $("#NameDog").text('')
              $("#social-media").hide();
              $(".rating-card").hide();
              $("#clear").hide();
              $('head').append('<style>.modal{height:' + 450+';}</style>')
              $('#profile').removeClass('dragging hasImage');
              $('#profile').css('background-image', '');
              document.getElementById('mydog').value = ''
    
        });
    
    
    
        
        $("#predic").click(function() {
          var str = $("#mydog").val();
          if(str){
            document.getElementById("numloc").innerHTML="";
            isLoading=true;
                  // disable button
              $(this).prop("disabled", true);
              $(this).html(
                '<i class="fa fa-circle-o-notch fa-spin"></i> loading...'
                );
              $.ajax({
                  type: "POST",
                  url: '/classify_image/classify/api/',
                  data: {
                    'image64': $('#img-dog-src').attr('src')
                  },
                  dataType: 'text',
                  success: function(data) {
                    var data = JSON.parse(data);
                    $(".rating-card").show()
                    $("#social-media").show();
                    $("#clear").show();
                    if (data["success"] == true) {
                          x=[];
                          y=[];
                          for (category in data['confidence']) {
                              var percent = data["confidence"][category]
                              x.push(category);
                              y.push(percent);
                          }
                          $('#predic').hide();
                          if(y[0] <= 90){
                            var markup = `<div ><h1>Mixed Breed </h1></div>   `;
                              $(".rating-process").append(markup);
                             var counter=0;
                            $('head').append('<style>.modal{height:' + 660+';}</style>')
                            for (category in data['confidence']) {
                              var percent = data["confidence"][category]
                              if(percent!=0){
                                counter++
                                var markup = `
                                
                                <div class="rating-right-part">
                                <p >`+ category + "  " + percent + " % "+ `</p>
                                <br/>
                                <div class="progress-`+counter+`"></div>
                              </div>
                               `;
                              $(".rating-process").append(markup);
                              }
    
    
                            }
    
                            if(counter < 3)
                              $('head').append('<style>.modal{height:' + 500+';}</style>')
                          else
                               $('head').append('<style>.modal{height:' + 660+';}</style>')
    
                          $('#prop').show();
                          $('head').append('<style>.progress-1:after{width: ' + y[0] + "%"+ ';}</style>');
                          $('head').append('<style>.progress-2:after{width: ' + y[1] + "%"+ ';}</style>');
                          $('head').append('<style>.progress-3:after{width: ' + y[2] + "%"+ ';}</style>');
                          $('head').append('<style>.progress-4:after{width: ' + y[3] + "%"+ ';}</style>');
                          $('head').append('<style>.progress-5:after{width: ' + y[4] + "%"+ ';}</style>');
                          }
                          else{
                            $('head').append('<style>.modal{height:' + 485+';}</style>');
                            var markup = `
                                <div><h1>Pure Breed </h1></div>
                                <div class="rating-right-part">
                                <h3 >`+ x[0] + "  " + y[0] + " % "+`</h3>
                                <br/>
                                <div class="progress-1" style="height: 30px;margin-left:40px"></div>
                              </div>
                          `;
                          $(".rating-process").append(markup);
                          $('#prop').show();
                          $('head').append('<style>.progress-1:after{width: ' + y[0] + "%"+ ';}</style>');
                          }
    
                          isLoading=false;
                    }
                    else
                    {
                      $("#social-media").hide();
                        $('#predic').hide();
                          var markup = `
                                <div style="margin-top:80px;"><h2 style="color:red;text-align: center;"> `+data["message"]+` </h2></div>
                                `;
                          $(".rating-process").append(markup);
                          isLoading=false;
                    }
                  }
                }).always(function() {
                //  modal.modal('close');
              });
          }
          else
          {
              document.getElementById("numloc").innerHTML="Please enter dog's name";
          }
    
    
         
        });
        
    
        $('#prop').hide();
    
        $('#profile').addClass('dragging').removeClass('dragging');
        });
    
        $('#profile').on('dragover', function() {
          if(!isLoading)
              $('#profile').addClass('dragging')
        }).on('dragleave', function() {
          if(!isLoading)
            $('#profile').removeClass('dragging')
        }).on('drop', function(e) {
          if(!isLoading){
         
            $('#profile').removeClass('dragging hasImage');
            if (e.originalEvent) {
                  var file = e.originalEvent.dataTransfer.files[0];
                  console.log(file);
    
                  var reader = new FileReader();
    
                  //attach event handlers here...
    
                  reader.readAsDataURL(file);
                  reader.onload = function(e) {
                    $('#img-dog-src').attr('src', event.target.result);
                    $('.rating-process').html('');
                    $('#predic').show();
                    $("#predic").prop("disabled", false);
                    // add spinner to button
                    $("#predic").html("<h2>Predict Breed of Dog</h2>");
                    $('#predic').show();
                    $('.editable').show();
                    $("#NameDog").text('my dog')
                    $("#social-media").hide();
                    document.getElementById('mydog').value = ''
                  $('#profile').css('background-image', 'url(' + reader.result + ')').addClass('hasImage');
    
            }
          }
        }
        })
        $('#profile').on('click', function(e) {
          if(isLoading==false)
            $('#mediaFile').click();
    
        });
        window.addEventListener("dragover", function(e) {
        e = e || event;
        e.preventDefault();
        }, false);
        window.addEventListener("drop", function(e) {
        e = e || event;
        e.preventDefault();
        }, false);
        $('#mediaFile').change(function(e) {
        var input = e.target;
        if (input.files && input.files[0]) {
          var file = input.files[0];
          var reader = new FileReader();
          reader.readAsDataURL(file);
          reader.onload = function(e) {
              $('#img-dog-src').attr('src', event.target.result);
              $('.rating-process').html('');
              $('#predic').show();
              $("#predic").prop("disabled", false);
              // add spinner to button
              $("#predic").html("<h2>Predict Breed of Dog</h2>");
              $('#predic').show();
              $('.editable').show();
              $("#NameDog").text('my dog')
              $("#social-media").hide();
              document.getElementById('mydog').value = ''
          $('#profile').css('background-image', 'url(' + reader.result + ')').addClass('hasImage');
          }
        }
        })

    })
    
document.addEventListener("DOMContentLoaded", function(event) { 
    // Uses sharer.js 
    //  https://ellisonleao.github.io/sharer.js/#twitter    
       var url = window.location.href;
       var title = document.title;
       var subject = "Read this good article";
       var via = "yourTwitterUsername";
    //facebook
    $('#share-fb').attr('data-url', url).attr('data-sharer', 'facebook');
    //twitter
    $('#share-tw').attr('data-url', url).attr('data-title', title).attr('data-via', via).attr('data-sharer', 'twitter');
    //linkedin
    $('#share-li').attr('data-url', url).attr('data-sharer', 'linkedin');
   
    //Prevent basic click behavior
    $( ".sharer button" ).click(function() {
      event.preventDefault();
    });
      
    });