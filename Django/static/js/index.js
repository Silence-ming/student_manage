
// $(function () {
//     //编辑
//     $('table').on('dblclick','td:not(.del)',function(){
//         $(this).attr('contenteditable','true').focus().css('backgroundColor','red');
//         var beforeValue=$(this.val());
//         $(this).blur(function(){
//             if ($(this).val() == beforeValue){
//                  $.ajax({
//                     url:'/edit/',
//                     type:'post',
//                     data:{value:$(this).val()},
//                     success:function(e){
//                          $(this).removeAttr('contenteditable').css('backgroundColor','#D2B48C')
//                     }
//                 })
//             }
//
//
//         })
//     });
//     //删除
//     $('table').on('click','.delete',function(){
//          $(this).parent().parent().remove()
//     });
//     //添加
//     $('#add').click(function(){
//         $.ajax({
//             url:'/add/',
//             type:'post',
//             data:{name:"a",sex:'a',student:'a',classes:'a'},
//             success:function(a){
//                 var content = '<td></td><td></td><td></td><td></td><td><button class="delete">删除</button></td>';
//                 var tr=$('<tr>').html(content);
//                 $('table').append(tr);
//             }
//         })
//     })
// })