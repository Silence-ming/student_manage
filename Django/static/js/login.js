window.onload=function(){
    //验证码
    canvas=document.getElementById('canvas');
    obj=canvas.getContext('2d');
    obj.beginPath();
    arr=['red','blue','green','violet','green'];
    arr1=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    key='';
    for (var i=0;i<6;i++){
        key+=arr1[Math.floor(Math.random()*62)]
    }
    obj.font='bold 18px 楷体';
    obj.fillText(key,20,25,);
    for(var i= 0;i<15;i++){
        obj.strokeStyle=arr[Math.floor(Math.random()*4)];
        obj.moveTo(parseInt(Math.random()*80),parseInt(Math.random()*80));
        obj.lineTo(parseInt(Math.random()*80),parseInt(Math.random()*80));
        obj.stroke()
    }
     $('button').click(function(e){
        if ($('#word').val() != key){
             e.preventDefault()
             $('.message').html('验证码不正确！')
        }
        else{
            $('.message').html('')
        }
    });
    $('#word').focus(function(){
         $('.message').html('')
    })
    //验证
     $('form').validate({
        rules:{
            user:{
                required:true,
                minlength:3
            },
            pass:{
                required:true,
                minlength:6,
            },
        },
        messages:{
            user:{
                required:'请输入用户名',
                minlength:'至少三位',
            },
            pass:{
                required:'请输入密码',
                minlength:'至少六位',
            },
        }
    });

};