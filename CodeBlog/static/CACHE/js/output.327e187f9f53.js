;if(window.addEventListener&&window.requestAnimationFrame&&document.getElementsByClassName){window.addEventListener('load',function(){'use strict';var pItem=document.getElementsByClassName('progressive replace')
var pCount;var timer;window.addEventListener('scroll',scroller,false);window.addEventListener('resize',scroller,false);if(MutationObserver){var observer=new MutationObserver(function(){if(pItem.length!==pCount)inView();});observer.observe(document.body,{subtree:true,childList:true,attributes:true,characterData:true});}
inView();function scroller(){timer=timer||setTimeout(function(){timer=null;inView();},300);}
function inView(){if(pItem.length)requestAnimationFrame(function(){var wH=window.innerHeight,cRect,cT,cH,p=0;while(p<pItem.length){cRect=pItem[p].getBoundingClientRect();cT=cRect.top;cH=cRect.height;if(0<cT+cH&&wH>cT){loadFullImage(pItem[p]);pItem[p].classList.remove('replace');}
else p++;}
pCount=pItem.length;});}
function loadFullImage(item,retry){var href=item&&(item.getAttribute('data-href')||item.href);if(!href)return;var img=new Image(),ds=item.dataset;if(ds){if(ds.srcset)img.srcset=ds.srcset;if(ds.sizes)img.sizes=ds.sizes;}
img.onload=addImg;retry=1+(retry||0);if(retry<3)img.onerror=function(){setTimeout(function(){loadFullImage(item,retry);},retry*3000);};img.className='reveal';img.src=href;function addImg(){requestAnimationFrame(function(){if(href===item.href){item.style.cursor='default';item.addEventListener('click',function(e){e.preventDefault();},false);}
var pImg=item.querySelector&&item.querySelector('img.preview');item.appendChild(img);img.addEventListener('animationend',function(){if(pImg){if(pImg.alt)img.alt=pImg.alt;pImg.parentNode.removeChild(pImg);}
img.classList.remove('reveal');addPinItBtnToImg(img);});});}}},false);}