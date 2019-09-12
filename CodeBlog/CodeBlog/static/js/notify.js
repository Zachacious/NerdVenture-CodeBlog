if(typeof notifyJSLoaded ==='undefined'){

    // (function (){

    function deleteNotification(uuid, animcls){
        let id = 'notify-' + uuid
        let target = document.getElementById(id);
        if(target){
            if(animcls){
                target.classList.add(animcls);
                function anim_end(){
                    if(target.parentNode){
                        target.parentNode.removeChild(target);
                    }
                }
                target.addEventListener('webkitAnimationEnd', anim_end);
                target.addEventListener('animationend', anim_end);
            } else {
                if(target.parentNode){
                    target.parentNode.removeChild(target);
                }
            }
            
        }
                    
    }

    function createNotification(alertcls, anim_startcls, anim_endcls, header, msg, timed=false){
        let uuid = Date.now() + Math.random();
        let div = document.createElement('div');
        div.className = 'row';
        div.innerHTML =  '\
        <div id="notify-' + uuid + '" class="alert sketch-border ' + 
            alertcls + ' ' + anim_startcls +'" role="alert">\
        <strong>' + header + '</strong>' + msg + '\
        <button type="button" class="close" aria-label="Close">\
            <span aria-hidden="true">&times;</span>\
        </button>\
        </div>\
        ';

        div.onclick = function(e){
            deleteNotification(uuid, anim_endcls);
        }

        var target = document.getElementById('notify-bar');
        if(target){
            target.appendChild(div);
        }
        
        if(timed){
            setTimeout(function(){
                deleteNotification(uuid, anim_endcls);
            }, 2000);
        }
    };

    // })();

}
notifyJSLoaded = true;

