<!-- MenuRecommendation.jsx
import React from 'react';

function MenuRecommendation() {
  const handleSubmit = (event) => {
    event.preventDefault();
    // 폼 제출 로직 추가
  };

  const openZone = () => {
    window.location.href = "https://127.0.0.1:443/zone";
  };

  const service = () => {
    window.location.href = "https://127.0.0.1:443/service";
  };

  const loadImage = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
      document.getElementById('image').src = e.target.result;
    };

    reader.readAsDataURL(file);
  };

  return (
    <div>
      <h1>메뉴 추천하는 사이트</h1>

      <form method="post" action={call_back_url} onSubmit={handleSubmit}>
        <button type="submit">
          <img src="/static/images/kakao_image.png" style={{ padding: "0.05px 0.1px" }} alt="" />
        </button>
      </form>

      <br />

      <form id="zoneForm" action="/zone" method="get">
        <button type="button" onClick={openZone}>
          <img src="/static/images/map.png" style={{ padding: "0.01px 0.01px" }} alt="" />
        </button>
      </form>

      <br />

      <label>위에 버튼 다 누르고 누르셈</label>
     <form id="service" action="/service" method="get">
        <button type="button" onClick={service}>
         <img src="/static/images/send.png" style={{ padding: "0.01px 0.01px" }} alt="" />
        </button>
      </form>

     <input type="file" id="fileInput" onChange={loadImage} />
     <img id="image" src="" alt="" />
   </div>
 );
}

export default MenuRecommendation; -->





--------------
<!-- // MenuRecommendation.jsx
// import React, { useEffect } from 'react';

// function MenuRecommendation() {
//   useEffect(() => {
//     if (navigator.geolocation) {
//       navigator.geolocation.getCurrentPosition(function(position) {
//         var lat = position.coords.latitude;
//         var lon = position.coords.longitude;
//         alert(lat + " " + lon);
//         console.log(lat, lon);

//         var mapContainer = document.getElementById('map');
//         var mapOption = {
//           center: new kakao.maps.LatLng(lat, lon),
//           level: 5
//         };
//         var map = new kakao.maps.Map(mapContainer, mapOption);
//         var locPosition = new kakao.maps.LatLng(lat, lon);
//         displayMarker(map, locPosition);
//       });
//     }
//   }, []);

//   const handleSubmit = (event) => {
//     event.preventDefault();
//     const coordinates = event.target.좌표.value;
//     // 현재 좌표 전달 로직 추가
//   };

//   const openLogin = () => {
//     window.location.href = 'https://127.0.0.1:443/login';
//   };

//   const displayMarker = (map, locPosition) => {
//     var marker = new kakao.maps.Marker({ map: map, position: locPosition });
//     var infowindow = new kakao.maps.InfoWindow({
//       content: '현재 위치',
//       removable: true
//     });
//     infowindow.open(map, marker);
//     map.setCenter(locPosition);
//   };

//   return (
//     <div>
//       <h1>메뉴 추천하는 사이트</h1>
//       <div id="map" style={{ width: '55%', height: '400px' }}></div>

//       <br />

//       <form method="post" action="/map" onSubmit={handleSubmit}>
//         <label htmlFor="좌표">현재좌표:</label>
//         <input type="text" id="좌표" name="좌표" />
//         <input type="submit" value="전달" />
//       </form>

//       <br />

//       <button type="button" onClick={openLogin}>
//         홈페이지로 돌아가기
//       </button>
//     </div>
//   );
// }

// export default MenuRecommendation; -->






----------


<!-- // MenuRecommendationSite.jsx
// import React from 'react';

// function MenuRecommendationSite() {
//   const openLogin = () => {
//     // 메인 페이지로 이동하는 로직
//     window.location.href = '/login';
//   };

//   return (
//     <div>
//       <h1>메뉴 추천하는 사이트</h1>
//       <button type="button" onClick={openLogin}>
//         홈페이지로 들어가기
//       </button>
//     </div>
//   );
// }

// export default MenuRecommendationSite; -->


----------

<!-- // MenuRecommendation.jsx
// import React from 'react';

// function MenuRecommendation() {
//   const handleSubmit = (event) => {
//     event.preventDefault();
//     const location = event.target.위치.value;
//     // 현재 위치를 사용하여 날씨 정보 판단 로직 추가
//     console.log("현재 위치:", location);
//   };

//   const handleOpenMap = () => {
//     window.location.href = 'https://127.0.0.1:443/map';
//   };

//   return (
//     <div>
//       <label>주변 날씨 판단을 위해</label>
//       <form onSubmit={handleSubmit}>
//         <label htmlFor="위치">현재위치:</label>
//         <input type="text" id="위치" name="위치" />
//         <input type="submit" value="전달" />
//       </form>

//       <br />

//       <button type="button" onClick={handleOpenMap}>
//         지도
//       </button>
//     </div>
//   );
// }

// export default MenuRecommendation; -->