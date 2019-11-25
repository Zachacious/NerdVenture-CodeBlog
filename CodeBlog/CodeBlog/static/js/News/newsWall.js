var newsWallPage = 0;
var feedPage;
var feedLoading = false;
var feedSpinner = document.getElementById('feed-spinner');

function isInView(elem){
    var bounding = elem.getBoundingClientRect();
    return (
        bounding.top >= 0 &&
        bounding.left >= 0 &&
        bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

function createItemsFromFeed(page){
    var newsWall = document.getElementById('news-wall');
    var post, idx;

    for(idx in page){
        post = page[idx];
        newsWall.innerHTML = newsWall.innerHTML + createNewsItem(post);
    }
}

function createNewsItem(post){
    return (
        '\n \
        <a href="'+post.link+'" target="_blank"\
            class="news-item p-rel d-grid wh100 bk4 overflow-hidden ease grow-light fade-in-anim">\
            \
            <div class="wh100 news-item-top"\
                style="background: url('+post.image+'), #fff no-repeat;\
                background-size: cover; background-position: center center;" >\
            </div>\
            \
            <div class="zindex1 w100 m0 p1">\
                <h5>'+post.title+'</h5>\
                <div class="m1 overflow-hidden ease news-desc">'+post.desc+'</div>\
                <div class="bk2 color1 m1 p05">'+post.source+'</div>\
            </div>\
            \
        </a>\
        '
    )

}

function getFeedPage(page_num){
    var xhttp = new XMLHttpRequest(); //AJAX
    var url = document.getElementById('newsWall-endpoint').value;
    var data = {
        page_num : String(page_num),
    };
    var csrftoken = Cookies.get('csrftoken');
    // AJAX
    //open async post request at endpoint
    try{
        xhttp.open("POST", url, true);
        xhttp.setRequestHeader('Content-Type', 'application/json');
        xhttp.setRequestHeader('Accepts', 'application/json');
        xhttp.setRequestHeader("X-CSRFToken", csrftoken);
        xhttp.send(JSON.stringify(data));
    }catch(e){
        console.log(e);
    }

    // once the ajax request has finished
    xhttp.addEventListener('load', function(event){
        feedPage = JSON.parse(xhttp.response);
        createItemsFromFeed(feedPage);
        feedLoading = false;
        feedSpinner.classList.add('opacity0');
    });
}

(function(){

    newsWallPage++; 
    feedLoading = true;
    feedSpinner.classList.remove('opacity0');
    getFeedPage(newsWallPage);

    window.addEventListener('scroll', function(){
        if(isInView(document.getElementById('news-wall-trigger'))){
            if(!feedLoading){
                // if we've reached the last page of post - do nothing
                if(feedPage && !feedPage[0].has_next){return;}
                newsWallPage++;
                feedLoading = true;
                feedSpinner.classList.remove('opacity0');
                getFeedPage(newsWallPage);
            }
        }
    });

})();
