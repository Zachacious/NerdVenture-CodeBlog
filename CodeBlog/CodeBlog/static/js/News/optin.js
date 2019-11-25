if(typeof optinJsLoaded === 'undefined'){
    

    (function (){

        var subscribeEvent = new Event('subscribed');
        var verifiedEvent = new Event('verified');
        var subscribedOrVerifiedEvent = new Event('subcribedOrVerified');

        function removeOptins(){
            var optins = document.getElementsByName('optinform');
            var optinIndex;
            for (optinIndex = 0; optinIndex < optins.length; optinIndex+=1){
                var optin = optins[optinIndex];

                optin.classList.add('fade-out');
                
                optin.addEventListener('animationend', function(e){
                    var targ = e.target;
                    targ.parentNode.removeChild(targ);
                });
                
            }
        }

        
        var optins = document.getElementsByName('optinform');
        var optinIndex;
        var counter = 0;
        for (optinIndex = 0; optinIndex < optins.length; optinIndex+=1){
            var optin = optins[optinIndex];
            
            // give unique ids
            counter++;
            optin.setAttribute('id', 'optinform' + counter.toString());

            // var submitBtn = optin.querySelector('button[value="Subscribe"]');
            var actionDl = document.getElementById('optin-action-download');
            var actionPl = document.getElementById('optin-action-pageload');
    
            optin.addEventListener("submit", function(event){
                event.preventDefault();
                target = event.target;
                // send ajax post to create subscriber
                var xhttp = new XMLHttpRequest();
        
                //success
                xhttp.addEventListener('load', function(event){
                    
                    var alertcls = 'alert-success';
                    target.removeAttribute('disabled');
                    document.getElementById('btn-loader').classList.add('d-none');
                    removeOptins();

                    if(event.target.status == 201){ //good
                        createNotification(alertcls, 'fade-down-anim', 
                        'fall-out-anim', 'Subscribed!', ' Check your email', true);
                        if(settings.debug){
                            // expires in 60 seconds
                            Cookies.set('NV-Subscribed', 'true', {expiry : 60, path: '/'});
                        } else {
                            var d = new Date();
                            Cookies.set('NV-Subscribed', 'true', 
                            {expiry : new Date(d.getFullYear() + 1, d.getMonth(), d.getDate()), path: '/'});
                        }
                        window.dispatchEvent(subscribeEvent);
                        window.dispatchEvent(subscribedOrVerifiedEvent);
                    } else {
                        // Usually means email already exist as subscriber
                        createNotification(alertcls, 'fade-down-anim', 
                        'fall-out-anim', 'Subscriber Verified ', '', true);
                        if(settings.debug){
                            // expires in 60 seconds
                            Cookies.set('NV-Subscribed', 'true', {expiry : 60, path: '/'});
                        } else {
                            var d = new Date();
                            Cookies.set('NV-Subscribed', 'true', 
                                {expiry : new Date(d.getFullYear() + 1, d.getMonth(), d.getDate()), path: '/'});
                        }
                        window.dispatchEvent(verifiedEvent);
                        window.dispatchEvent(subscribedOrVerifiedEvent);
                    }
                     
                    if(actionDl){ // download
                        window.open(actionDl.value);
                    } 

                    if(actionPl){ // load page
                        window.location = actionPl.value
                    }
                    // console.log(event);
                });
        
                //endpoint 
                var url = target['apiURL'].value;
                

                var formEmail = target['emailoptin'].value;
                var optinUsed = target['optinName'].value;
                
                // var csrftoken = getCookie('csrftoken');
                var csrftoken = Cookies.get('csrftoken');
        
                // data to send
                var data = {
                    email : String(formEmail),
                    optin_used : String(optinUsed),
                    subscribed: true
                };
        
        
                //open async post request at endpoint
                try{
                    xhttp.open("POST", url, true);
                    xhttp.setRequestHeader('Content-Type', 'application/json');
                    xhttp.setRequestHeader('Accepts', 'application/json');
                    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
                    xhttp.send(JSON.stringify(data));

                    target.setAttribute('disabled', 'true');
                    document.getElementById('btn-loader').classList.remove('d-none');
                }catch(e){
                    console.log(e);
                }
                
            });
        }
        })();
}

optinJsLoaded = true;

