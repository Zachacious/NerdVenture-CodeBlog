/*
Contact Form -
-Opens the contact form modal
-sends validates and sends data to backend via ajax
-displays thank you screen

TODO:
The contact form needs to be encapsulated in its own app.
*/

// only execut IIFE if it hasn't already been run
if(typeof contactFormJS == 'undefined'){
 
    (function (){
        // if more than one contact form rename id's
        var cforms = document.getElementsByName('contactform');

        var cformIndex;
        var counter = 0;
        for (cformIndex = 0; cformIndex < cforms.length; cformIndex+=1){
            var cform = cforms[cformIndex];
            counter++;
            // cform.setAttribute('id', 'contactform' + counter);

            var form = cform.querySelector('#contact');
            var xhttp = new XMLHttpRequest(); //AJAX
            var sendBtn = form['sendBtn'];
            var formContent = form.parentNode;
            var modal = form.parentNode.parentNode;

            // get access to bootstrap native modal as modalInst
            // var modalInst = new Modal(modal);

            var formThanks = modal.querySelector('#form-thanks');

            // add event listener to make sure it can open it
            // var btn = document.getElementById('contactBtn');
            // btn.addEventListener('click', function(event){
            //     modalInst.show();
            // });

            var resetForm = function(event){
                form.reset(); // reset form fields
                form.removeAttribute('disabled');
                // remove animations
                formContent.classList.remove('fade-out');
                formThanks.classList.remove('fade-in');

                // show the form 
                formContent.style.opacity = 1;
                // hide the thank you msg
                formThanks.style.opacity = 0;
                formContent.style.zIndex = 100;
                formThanks.style.zIndex = 5;
                formThanks.style.display = 'none';
            };

            var clsbtn = document.getElementById('contact-close-btn');
            var outerModal = document.querySelector('.light-modal');
            var modalContent = document.querySelector('.light-modal-content');

            // stop events from progigating to the modal background 
            // because that will cause it to reset and close
            modalContent.addEventListener('click', function(event){
                event.stopPropagation();
            });

            // when clicking outside the modal
            outerModal.addEventListener('click', function(event){
                event.stopPropagation();
                event.preventDefault();
                resetForm(event);
                // close the modal
                window.location.href='#';
            });

            clsbtn.addEventListener('click', function(event){
                resetForm(event);
                
            });

            // callback for when the submit button is clicked
            cform.addEventListener("submit", function(event){
                event.preventDefault();
                
                // the loading spinner icon for the button
                var loader = sendBtn.querySelector('span[name="btn-loader"]');
              
                //callback for success - data sent successfully 
                xhttp.addEventListener('load', function(event){
                    // hide the loading spinner on the button
                    loader.classList.add('d-none');
                    
                    // hide the form show the thank you
                    formContent.classList.add('fade-out');
                    formThanks.classList.add('fade-in');

                    formContent.style.zIndex = 5;
                    formThanks.style.zIndex = 10;

                    formThanks.style.display = 'block';

                    //reset
                    form.reset();

                });
              
                //get api endpoint from hidden input in the form
                var url = form['apiURL'].value;

                // get form data
                var email = form['emailInput'].value;
                var message = form['message'].value;
                var subscribe_check = form['subcribe-checkbox'].checked;
              
                // must send csrf token to the backend
                var csrftoken = Cookies.get('csrftoken');
              
                // data to send
                var data = {
                    email : String(email),
                    message: String(message),
                    subscribe: subscribe_check
                };
              
                // AJAX
                //open async post request at endpoint
                try{
                    xhttp.open("POST", url, true);
                    xhttp.setRequestHeader('Content-Type', 'application/json');
                    xhttp.setRequestHeader('Accepts', 'application/json');
                    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
                    xhttp.send(JSON.stringify(data));
              
                    loader.classList.remove('d-none');
                    form.setAttribute('disabled', true);
                }catch(e){
                    console.log(e);
                }
            });
        }

    })()
}

var contactFormJS = true;