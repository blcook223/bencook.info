;(function($, google) {
  'use strict';

  var CUSTOM_MAPTYPE_ID = 'custom_map',
      MAP_HUE = '#C0392B',
      mapCanvas = document.getElementById('fwMap'),
      timelines = $('ul.flaTimeline').not('.minimal'),
      minimalTimelines = $('ul.flaTimeline').filter('.minimal'),
      linkedEvent,
      locations,
      labels,
      customMapType,
      featureOptions,
      map;

  if (minimalTimelines.length) {
    minimalTimelines.flaTimeline({
      toggle: false
    });
  }

  if (timelines.length) {
    timelines.flaTimeline({
      onComplete: function() {
        $(this).parent('.content').toggleClass('opened');
      },
      onOpeningComplete: function() {
        google.maps.event.trigger(map, 'resize');
        map.set('center', new google.maps.LatLng(32.70730, -97.32784));
        for (var i = 0; i < labels.length; ++i) {
          labels[i].open(map);
        }
      }
    });

    if (window.location.hash) {
      linkedEvent = $(window.location.hash);
      linkedEvent.find('.text').css('display', 'block');
      linkedEvent.find('.content').toggleClass('content-open');
    }
  }

  if (mapCanvas) {
    mapCanvas.addEventListener('click', function(e) {
      e.stopPropagation(); // prevent closing timeline event
    });

    locations = [
      {
        position: new google.maps.LatLng(32.75492, -97.33070),
        content: '<a href="">Flying Saucer</a>'
      },
      {
        position: new google.maps.LatLng(32.67513, -97.41086),
        content: '<a href="">Rosa\'s Cafe</a>'
      },
      {
        position: new google.maps.LatLng(32.60990, -97.39548),
        content: 'My High School'
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
      mapTypeControlOptions: {
        mapTypeIds: []
      },
      mapTypeId: CUSTOM_MAPTYPE_ID
    });
    customMapType = new google.maps.StyledMapType(featureOptions);
    map.mapTypes.set(CUSTOM_MAPTYPE_ID, customMapType);
    labels = [];
    for (var i = 0; i < locations.length; ++i) {
      labels.push(new google.maps.InfoWindow({
        content: locations[i].content,
        position: locations[i].position
      }));
    }
  }

})(window.jQuery, window.google);
