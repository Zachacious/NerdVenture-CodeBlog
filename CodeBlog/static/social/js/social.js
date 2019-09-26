function addPinItBtnToImg(img){

    if(!img) {return};

    var parent = img.parentNode;
    var wrapper = document.createElement('div');
    parent.replaceChild(wrapper, img);
    wrapper.appendChild(img);
    //wrapper.style.overflow = 'hidden'; 
    wrapper.style.position = 'relative';

    // create pintrest 
    var pinBtn = document.createElement('a');
    pinBtn.href = 'https://pinterest.com/pin/create/button/?url='+ img.src;
    pinBtn.target = '_blank';
    pinBtn.innerHTML = '<svg class="icon icon-pinterest trans-ease grow" style="color: #c8232c"><use xlink:href="#icon-pinterest"></use></svg><span class="pin-text">Pin It!</span>';
    pinBtn.classList.add('pin-btn-overlay');
    pinBtn.classList.add('bg-light');
    pinBtn.classList.add('sketch-border');
    pinBtn.classList.add('p-1');
    pinBtn.classList.add('m-1');
    //pintBtn.style.fontSize = '1.5em';

    // insert pin button into wrapper 
    wrapper.appendChild(pinBtn);
}

(function(){

    var addPinItBtnToArticleImgs = function(){
        var article = document.getElementById('article-contents');
        if(!article) return;
        var images = Array.from(article.querySelectorAll('img'));

        var imgIndex = 0;
        for(imgIndex = 0; imgIndex < images.length; imgIndex++){

            var img = images[imgIndex];
            addPinItBtnToImg(img);
        }
    };

    var socialAnim = function() {
        var socialbar = document.getElementById('social-share-vert-bar');
        if(socialbar){
            var anim_len = 0.8 * 1000; //seconds * 1000ms
            var anim_interval = 25 * 1000;

            // start the animation every (anim_interval) seconds
            window.setInterval(function(){
                socialbar.classList.add('shake-bl');
            }, anim_interval);

            // remove after done
            window.setInterval(function(){
                socialbar.classList.remove('shake-bl');
            }, anim_interval + anim_len);
        }
    };

    // wait until doc ready
    if (document.readyState!='loading') {
        socialAnim();
        addPinItBtnToArticleImgs();
    }
    else if (document.addEventListener) document.addEventListener('DOMContentLoaded', function(){
        socialAnim();
        addPinItBtnToArticleImgs();
    });
    else document.attachEvent('onreadystatechange', function(){
        if (document.readyState=='complete') {
            socialAnim();
            addPinItBtnToArticleImgs();
        }
    })


    
    // wrap the image in a div
    // var parent = img.parentNode;
    // var wrapper = document.createElement('div');
    // parent.replaceChild(wrapper, img);
    // wrapper.appendChild(img);
    // //wrapper.style.overflow = 'hidden'; 
    // wrapper.style.position = 'relative';

    // // create pintrest 
    // var pinBtn = document.createElement('a');
    // pinBtn.href = 'https://pinterest.com/pin/create/button/?url='+ img.src;
    // pinBtn.target = '_blank';
    // pinBtn.innerHTML = '<svg class="icon icon-pinterest trans-ease grow" style="color: #c8232c"><use xlink:href="#icon-pinterest"></use></svg><span class="pin-text">Pin It!</span>';
    // pinBtn.classList.add('pin-btn-overlay');
    // pinBtn.classList.add('bg-light');
    // pinBtn.classList.add('sketch-border');
    // pinBtn.classList.add('p-1');
    // pinBtn.classList.add('m-1');
    // //pintBtn.style.fontSize = '1.5em';

    // // insert pin button into wrapper 
    // wrapper.appendChild(pinBtn);
// }

})();