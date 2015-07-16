;(function($, google) {
  'use strict';

  var CUSTOM_MAPTYPE_ID = 'custom_map',
      MAP_HUE = '#C0392B',
      mapCanvas = document.getElementById('fwMap'),
      timelines = $('ul.flaTimeline'),
      linkedEvent,
      locations,
      labels,
      customMapType,
      featureOptions,
      map;

  if (timelines.length) {
    if (mapCanvas) {
      timelines.flaTimeline({
        onOpeningComplete: function() {
          google.maps.event.trigger(map, 'resize');
          map.set('center', new google.maps.LatLng(32.70730, -97.32784));
          for (var i = 0; i < labels.length; ++i) {
            labels[i].open(map);
          }
        }
      });
    } else {
      timelines.flaTimeline();
    }

    if (window.location.hash) {
      linkedEvent = $(window.location.hash);
      linkedEvent.find('.text').css('display', 'block');
      linkedEvent.toggleClass('open');
    }
  }

  if (mapCanvas) {
    mapCanvas.addEventListener('click', function(e) {
      e.stopPropagation(); // prevent closing timeline event
    });

    locations = [
      {
        position: new google.maps.LatLng(32.75492, -97.33070),
        content: '<a href="http://www.beerknurd.com/stores/fortworth/" target="_blank">Flying Saucer</a>'
      },
      {
        position: new google.maps.LatLng(32.67513, -97.41086),
        content: '<a href="http://www.rosascafe.com/home" target="_blank">Rosa\'s Cafe</a>'
      },
      {
        position: new google.maps.LatLng(32.60990, -97.39548),
        content: 'My High School'
      },
      {
        position: new google.maps.LatLng(32.751587, -97.082996),
        content: '<a href="http://texas.rangers.mlb.com/tex/ballpark/" target="_blank">Ballpark in Arlington</a>'
      }
    ];

    featureOptions = [
      {
        stylers: [
          { hue: MAP_HUE },
          { visibility: 'simplified' },
          { gamma: 0.5 },
          { weight: 0.5 }
        ]
      },
      {
        elementType: 'labels',
        stylers: [
          { visibility: 'off' }
        ]
      },
      {
        featureType: 'water',
        stylers: [
          { color: MAP_HUE }
        ]
      }
    ];

    map = new google.maps.Map(mapCanvas, {
      zoom: 11,
      panControl: false,
      streetViewControl: false,
      zoomControlOptions: {
        style: google.maps.ZoomControlStyle.SMALL
      },
      mapTypeControlOptions: {
        mapTypeIds: []
      },
      mapTypeId: CUSTOM_MAPTYPE_ID
    });
    customMapType = new google.maps.StyledMapType(featureOptions);
    map.mapTypes.set(CUSTOM_MAPTYPE_ID, customMapType);
    labels = [];
    for (var i = 0, len = locations.length; i < len; ++i) {
      labels.push(new google.maps.InfoWindow({
        content: locations[i].content,
        position: locations[i].position
      }));
    }
  }

})(window.jQuery, window.google);
