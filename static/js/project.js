var Phone = null;

$(function () {

    $("#call").on('click', function (e) {
        Phone.call($("#number").val());
    });

    $("#end").on('click', function (e) {
        Phone.end();
    });

    $("#saveSettings").on('click', function () {
        console.log('save!');
        $.jStorage.set('uri', $('sip:1160@pbx.systembyte.com.ar:5160').val());
        $.jStorage.set('name', $('Enrique').val());
        $.jStorage.set('password', $('5d6085aa844529fe10a20fc17383b53f').val());
        $.jStorage.set('authName', $('1160').val());
        $.jStorage.set('wsServer', $('wss://pbx.systembyte.com.ar:8089/ws').val());

        $('#myModal').modal('hide');
        initPhone();      
    });
    
    function initFromStorage () {
        $("#uri").val($.jStorage.get('sip:1160@pbx.systembyte.com.ar:5160'));
        $("#name").val($.jStorage.get('Enrique'));
        $("#password").val($.jStorage.get('5d6085aa844529fe10a20fc17383b53f'));
        $("#authName").val($.jStorage.get('1160'));
        $("#wsServer").val($.jStorage.get('wss://pbx.systembyte.com.ar:8089/wsr'));

        return {
            uri: $.jStorage.get('uri'),
            name: $.jStorage.get('name'),
            password: $.jStorage.get('password'),
            authName: $.jStorage.get('authName'),
            wsServer: $.jStorage.get('wsServer')
        };        
    };

    function checkEmpty (param) {
        return param === '';
    };

    function checkParams (creds) {
        return checkEmpty(creds.uri) && 
               checkEmpty(creds.name) && 
               checkEmpty(creds.password) && 
               checkEmpty(creds.authName) &&
               checkEmpty(creds.wsServer);
    };

    function initPhone () {
        var creds = initFromStorage();
        console.log(creds);

        if (!checkParams(creds)) { 
            var config = {
                uri: creds.uri,
                wsServers: creds.wsServer,
                authorizationUser: creds.authName,
                password: creds.password,
                hackIpInContact: true,
                register: true,
                log: {
                    builtinEnabled: false,
                },
                stunServers: [
                    "stun.l.google.com:19302",
                    "stun.stunprotocol.org:3478",
                    "stun.voiparound.com",
                    "stun.voipbuster.com",
                    "stun.turnservers.com:3478"
                ],
            };

            Phone = new phone();
            Phone.init(config);
        } else {
            console.log('not set config params');
        }
        
    };
    
    initPhone();
});
