    
    var bar = new ProgressBar.Line(container_play, {
      strokeWidth: 2,
      easing: 'easeInOut',
      duration: 1000,
      color: '#00DD00',
      trailColor: '#eee',
      trailWidth: 1,
      svgStyle: {width: '100%', height: '100%'},
      text: {
        style: {
          color: '#FFFFFF',
          position: 'absolute',
          left: '120px',
          bottom: '15px',
          padding: 0,
          margin: 0,
        },
      },
    });


    stime = {{radio_player.server_currentsong('time')}}
    elapsed = {{radio_player.server_status('elapsed')}}
    val = elapsed / stime

    init_msec = Date.now()
    act_ela = elapsed * 1000

    val = act_ela / 1000 / stime

    minutes = Math.floor((act_ela / 1000/ 60));
    seconds = Math.floor(act_ela / 1000 - (minutes * 60));

    if (minutes < 10) {minutes = "0"+minutes;}
    if (seconds < 10) {seconds = "0"+seconds;}

    time_txt = minutes + ':' + seconds

    bar.set(val)
    bar.setText(time_txt);
    
    if ('{{radio_player.state}}' == 'play') {

      setInterval(function() {
        if ( bar.value() > 1 ) {
          location.reload()
        }

        act_msec = Date.now()
        dif_msec = act_msec - init_msec
        act_ela = elapsed * 1000 + dif_msec
        val = act_ela / 1000 / stime

        minutes = Math.floor((act_ela / 1000/ 60));
        seconds = Math.floor(act_ela / 1000 - (minutes * 60));

        if (minutes < 10) {minutes = "0"+minutes;}
        if (seconds < 10) {seconds = "0"+seconds;}

        time_txt = minutes + ':' + seconds

        bar.animate(val);
        bar.setText(time_txt);

      }, 900);
    
    }