$(function(){

    $('#addServerForm').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            st: {
                validators: {
                    notEmpty: {
                        message: '请填写业务线名称'
                    }
                }
            },
            assets_no: {
                validators: {
                    notEmpty: {
                        message: '请填写资产好'
                    },
                    stringLength: {
                        min: 6,
                        max: 30,
                        message: '资产号长度大于6小于30'
                    },
                }
            },
            cabinet_pos: {
                validators: {
                    notEmpty: {
                        message: '请输入托盘号'
                    }
                    // stringLength: {
                    //     min: 6,
                    //     max: 30,
                    //     message: 'The username must be more than 6 and less than 30 characters long'
                    // },
                    // regexp: {
                    //     regexp: /^[a-zA-Z0-9_\.]+$/,
                    //     message: 'The username can only consist of alphabetical, number, dot and underscore'
                    // }
                }
            },
            hostname: {
                validators: {
                    notEmpty: {
                        message: '请输入主机名'
                    }
                    // emailAddress: {
                    //     message: 'The input is not a valid email address'
                    // }
                }
            },
            address: {
                validators: {
                    notEmpty: {
                        message: '请输入地址'
                    },
                    // different: {
                    //     field: 'username',
                    //     message: 'The password cannot be the same as username'
                    // }
                }
            },
            mac_address: {
                validators: {
                    notEmpty: {
                        message: '请输入MAC地址'
                    }
                }
            },
            // captcha: {
            //     validators: {
            //         callback: {
            //             message: 'Wrong answer',
            //             callback: function(value, validator, $field) {
            //                 var items = $('#captchaOperation').html().split(' '), sum = parseInt(items[0]) + parseInt(items[2]);
            //                 return value == sum;
            //             }
            //         }
            //     }
            // },
            remote_cardip: {
                validators: {
                    notEmpty: {
                        message: '请输入管理卡IP'
                    }
                }
            }
        }
    }).on('success.form.fv', function(e,data) {
    	console.log(arguments)
            // Prevent form submission
            e.preventDefault();

            // Some instances you can use are
            var $form = $(e.target),        // The form instance
                fv    = $(e.target).data('formValidation'); // FormValidation instance
                console.log('success')
      if (data.fv.getSubmitButton()) {
                data.fv.disableSubmitButtons(false);
            }
            // Do whatever you want here ...
        });
})