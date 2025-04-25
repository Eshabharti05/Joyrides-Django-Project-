let imgarr=['../static/images/images/main background.jpg','../static/images/images/img2.jpg','../static/images/images/bg2.jpg','../static/images/images/img2.jpg','../static/images/images/img5.jpg'];      
        let i=0;
        screen=document.getElementById('img');
        dot=document.getElementsByClassName('dot');
        let c=0;
        setInterval(counter,2000);
        function slide(sign){
            i+=sign;
            if(i<0)
            {
                i=imgarr.length-1;
            }
            else if(i>imgarr.length-1)
            {
                i=0;
            }
            select(i);
        }
        function select(n){
            console.log(n)
            let dots = document.getElementsByClassName("dot");
            screen.src=imgarr[n];
            for (k = 0; k < dots.length; k++){
                 dots[k].className = dots[k].className.replace(" active", "");
            }
            dots[n].className += " active";  
        }
        function counter(){
            if(c>4){
            c=0;}
            
            let dots = document.getElementsByClassName("dot");
            screen.src=imgarr[c]; 
            select(c)
            c++;
        }