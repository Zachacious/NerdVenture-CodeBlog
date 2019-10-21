var ticking = false;
var navOnTop = true;
var menu_opened = false;

function searchToggle(){
    var searchForm = document.getElementById('search-form');
    var toggler = document.getElementById('search-toggle');

    if(searchForm.classList.contains('hide-el')){
        searchForm.classList.remove('hide-el');
        toggler.classList.add('hide-el');
        searchForm.classList.add('fade-in');
        toggler.classList.add('fade-out');
    } else {
        searchForm.classList.remove('fade-in');
        searchForm.classList.add('fade-out');
        searchForm.classList.add('hide-el');
        toggler.classList.remove('hide-el');
    }
}

(function(){
    window.addEventListener('scroll', function(e){
        var ypos = window.scrollY;
        
        if(!ticking){
            window.requestAnimationFrame(function(){
                var nav = document.getElementById('navigation');
                if(!nav) {return};

                if(ypos > 20){
                    navOnTop = false;
                    nav.classList.remove('bg-transparent');
                    nav.classList.add('bg-main-blue');
                } else {
                    navOnTop = true;
                    if(!menu_opened){
                        nav.classList.add('bg-transparent');
                        nav.classList.remove('bg-main-blue');
                    }
                }

                ticking = false;
            });

            ticking = true;
        }
    })

    var nav = document.getElementById('navigation');
    var menuBtn = document.getElementById('navbar-toggle-cbox');
    var hamburger = document.getElementById('nav-menu-icon');
    var navMenuClose = document.getElementById('nav-menu-close');

    menuBtn.onclick = function(e){
        if(!this.checked){
            if(navOnTop){
                nav.classList.add('bg-transparent');
                nav.classList.remove('bg-main-blue');
            }
            menu_opened = false;
            hamburger.classList.remove('d-none');
            navMenuClose.classList.add('d-none');
            
        } else {
            menu_opened = true;
            hamburger.classList.add('d-none');
            navMenuClose.classList.remove('d-none');

            nav.classList.remove('bg-transparent');
            nav.classList.add('bg-main-blue');
        }
        
    }

    nav.addEventListener('click', function(e){
        if(!e.target.matches('a,button')) return;
        menuBtn.checked = false;
        menu_opened = false;
        hamburger.classList.remove('d-none');
        navMenuClose.classList.add('d-none');

        if(navOnTop){
            nav.classList.add('bg-transparent');
            nav.classList.remove('bg-main-blue');
        }
    });
})()