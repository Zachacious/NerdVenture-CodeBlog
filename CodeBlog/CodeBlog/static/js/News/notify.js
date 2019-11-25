if(typeof notifyJSLoaded ==='undefined'){

    // (function (){

    function deleteNotification(uuid, animcls){
        var id = 'notify-' + String(uuid)
        var target = document.getElementById(id);
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
        var uuid = Date.now() + Math.random();
        var div = document.createElement('div');
        // div.className = 'row';
        div.innerHTML =  '\
        <div id="notify-' + uuid + '" class="bk3 color1 ease fade-down-anim p1 ' + 
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
            }, 3000);
        }
    };

    // })();

}
notifyJSLoaded = true;

