/*
 * QuickCopy — Service Worker
 * 전략: 앱 셸 프리캐시 + Cache-First
 *
 * CACHE_NAME 은 앱 버전과 묶여 있다. 파일을 수정하면 09_ChangeVersionName.py 로
 * 버전을 올려야 기존 사용자의 캐시가 폐기되고 새 파일을 내려받는다.
 * (버전만 올리고 캐시명을 그대로 두면 갱신되지 않는다)
 */
'use strict';

var CACHE_NAME = 'quickcopy-v1.0.1';

/* 앱 셸 — 외부 리소스는 하나도 없다 (오프라인 100% 동작) */
var SHELL = [
  './',
  './index.html',
  './manifest.webmanifest',
  './favicon.svg',
  './icon-192.png',
  './icon-512.png',
  './icon-maskable-512.png',
  './apple-touch-icon.png'
];

self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      // 개별 실패가 전체 설치를 막지 않도록 하나씩 담는다
      return Promise.all(SHELL.map(function (url) {
        return cache.add(new Request(url, { cache: 'reload' })).catch(function () { /* 무시 */ });
      }));
    }).then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (k) {
        return k === CACHE_NAME ? null : caches.delete(k);   // 이전 버전 캐시 삭제
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (event) {
  var req = event.request;

  if (req.method !== 'GET') return;                     // GET 만 처리

  var url;
  try { url = new URL(req.url); } catch (e) { return; }
  if (url.origin !== self.location.origin) return;       // 외부 도메인은 그대로 통과
  if (!/^https?:$/.test(url.protocol)) return;

  event.respondWith(
    caches.match(req, { ignoreSearch: true }).then(function (hit) {
      if (hit) return hit;                               // 캐시 우선
      return fetch(req).then(function (res) {
        if (res && res.ok && (res.type === 'basic' || res.type === 'default')) {
          var copy = res.clone();
          caches.open(CACHE_NAME).then(function (cache) {
            cache.put(req, copy).catch(function () { /* 무시 */ });
          });
        }
        return res;
      }).catch(function () {
        // 네트워크 실패 + 내비게이션 요청이면 앱 셸을 돌려준다
        if (req.mode === 'navigate') {
          return caches.match('./index.html').then(function (page) {
            return page || Response.error();
          });
        }
        return Response.error();
      });
    })
  );
});
