;if(typeof optinJsLoaded==='undefined'){(function(){function removeOptins(){var optins=document.getElementsByName('optin');var optinIndex;for(optinIndex=0;optinIndex<optins.length;optinIndex+=1){var optin=optins[optinIndex];optin.classList.add('fade-out');optin.addEventListener('animationend',function(e){var targ=e.target;targ.parentNode.removeChild(targ);});}}
var optins=document.getElementsByName('optinform');var optinIndex;var counter=0;for(optinIndex=0;optinIndex<optins.length;optinIndex+=1){var optin=optins[optinIndex];counter++;optin.setAttribute('id','optinform'+counter.toString());optin.addEventListener("submit",function(event){event.preventDefault();target=event.target;var xhttp=new XMLHttpRequest();xhttp.addEventListener('load',function(event){var alertcls='alert-success';target.removeAttribute('disabled');document.getElementById('btn-loader').classList.add('d-none');removeOptins();if(event.target.status==201){createNotification(alertcls,'swing-in-top-fwd','swing-out-top-bck','Subscribed!',' Check your email',true);if(settings.debug){Cookies.set('subscribed','true',{expiry:60});}else{var d=new Date();Cookies.set('subscribed','true',{expiry:new Date(d.getFullYear()+1,d.getMonth(),d.getDate())});}}else{createNotification(alertcls,'swing-in-top-fwd','swing-out-top-bck','Subscriber Verified ','',true);if(settings.debug){Cookies.set('subscribed','true',{expiry:60});}else{var d=new Date();Cookies.set('subscribed','true',{expiry:new Date(d.getFullYear()+1,d.getMonth(),d.getDate())});}}});var url=target['apiURL'].value;var formEmail=target['emailoptin'].value;var optinUsed=target['optinName'].value;var csrftoken=Cookies.get('csrftoken');var data={email:String(formEmail),optin_used:String(optinUsed),subscribed:true};try{xhttp.open("POST",url,true);xhttp.setRequestHeader('Content-Type','application/json');xhttp.setRequestHeader('Accepts','application/json');xhttp.setRequestHeader("X-CSRFToken",csrftoken);xhttp.send(JSON.stringify(data));target.setAttribute('disabled','true');document.getElementById('btn-loader').classList.remove('d-none');}catch(e){console.log(e);}});}})();}
optinJsLoaded=true;