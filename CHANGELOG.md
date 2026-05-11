# Changelog

## 0.2.0 (2026-05-11)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/harbinger-labs/clarative-python/compare/v0.1.0...v0.2.0)

### Features

* Add SLA tier details to developer API retrieve endpoint ([3a1e889](https://github.com/harbinger-labs/clarative-python/commit/3a1e8898d0d48f0ca803df8911115b6b13ae7871))
* Add vendor domains to developer API list and retrieve endpoints ([1818aed](https://github.com/harbinger-labs/clarative-python/commit/1818aedeb8171791dc8996de8f23aac2875c5098))
* support setting headers via env ([24370c8](https://github.com/harbinger-labs/clarative-python/commit/24370c8fa536baf6a55669d0c38b7026148e8e8d))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([f943621](https://github.com/harbinger-labs/clarative-python/commit/f943621454f6f0e2bf4cda3a21cb70f1fd609d39))
* ensure file data are only sent as 1 parameter ([0913887](https://github.com/harbinger-labs/clarative-python/commit/09138874e46da0b75b45c89674278dae0df94f9e))
* use correct field name format for multipart file arrays ([4e73598](https://github.com/harbinger-labs/clarative-python/commit/4e73598b1db03e23bc647d158b4dddfb0da0c623))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([fa1daba](https://github.com/harbinger-labs/clarative-python/commit/fa1dabaea11bd8856d8b9466c1f57b434e3e34f2))


### Chores

* **internal:** more robust bootstrap script ([80e4352](https://github.com/harbinger-labs/clarative-python/commit/80e4352a7b76730fbf5c5716a1bd56593fbc46af))
* **internal:** reformat pyproject.toml ([953710b](https://github.com/harbinger-labs/clarative-python/commit/953710b9d6f1c590c6de0bc9f8d8bc49dd799bca))

## 0.1.0 (2026-04-08)

Full Changelog: [v0.0.5...v0.1.0](https://github.com/harbinger-labs/clarative-python/compare/v0.0.5...v0.1.0)

### Features

* **internal:** implement indices array format for query and form serialization ([4899970](https://github.com/harbinger-labs/clarative-python/commit/4899970635a3fd07d21303e85974e31c1c99a6ad))
* Risk event endpoint enhancements ([cbd4b24](https://github.com/harbinger-labs/clarative-python/commit/cbd4b24786fa09086cc45b4263d4ae6d1080d7d8))
* Vendor endpoint enhancements + SLA filter ([7a203f6](https://github.com/harbinger-labs/clarative-python/commit/7a203f61aab380a9a625fcc97cec35bd6a77a710))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([0954fd1](https://github.com/harbinger-labs/clarative-python/commit/0954fd1fa710e44c4b53bb20bac83918fc9fbbbb))
* sanitize endpoint path params ([f66ec69](https://github.com/harbinger-labs/clarative-python/commit/f66ec69d76e2c1b97fe86cd695f992d6307aaecd))


### Chores

* **ci:** skip lint on metadata-only changes ([1ec0ef2](https://github.com/harbinger-labs/clarative-python/commit/1ec0ef25c90d0a919f6714af737e2fb9e3eacd03))
* **internal:** update gitignore ([ab05b15](https://github.com/harbinger-labs/clarative-python/commit/ab05b15363a719f5c008235b35bde1e7dbd5a55f))

## 0.0.5 (2026-03-19)

Full Changelog: [v0.0.4...v0.0.5](https://github.com/harbinger-labs/clarative-python/compare/v0.0.4...v0.0.5)

### Features

* Custom Vendor Metadata Fields ([e71229c](https://github.com/harbinger-labs/clarative-python/commit/e71229c2916bc60ccd449a7199133cb262971ee3))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([500d047](https://github.com/harbinger-labs/clarative-python/commit/500d047841e537eeed8824d63fd4b55dcd1a806d))
* **pydantic:** do not pass `by_alias` unless set ([43a0ed2](https://github.com/harbinger-labs/clarative-python/commit/43a0ed27ea15d3fef65dfa6e590bd6b45c0952ed))


### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([007a809](https://github.com/harbinger-labs/clarative-python/commit/007a8097e4994fddfdb9b9b938f233ea9c6fafdb))
* **internal:** refactor authentication internals ([b8fc90f](https://github.com/harbinger-labs/clarative-python/commit/b8fc90f82ed36661b733a505d4fb8a93490486d8))
* **internal:** tweak CI branches ([25d879c](https://github.com/harbinger-labs/clarative-python/commit/25d879cab9102502d1fe161696943c9c520b8766))

## 0.0.4 (2026-03-02)

Full Changelog: [v0.0.3...v0.0.4](https://github.com/harbinger-labs/clarative-python/compare/v0.0.3...v0.0.4)

### Features

* [Jacob/HARB-4470] Developer API /v1/risk-events routes ([c4025d5](https://github.com/harbinger-labs/clarative-python/commit/c4025d5000ec3c3570af92bc39e890e1e5aa49d6))
* [Jacob/HARB-4471] Developer API: Uptime Metrics Endpoint ([fd8def1](https://github.com/harbinger-labs/clarative-python/commit/fd8def19e894e093f707cd6fa3458d4e96bc2f2f))
* [Jacob/HARB-4537] Developer API: SLA Violations Routes ([84b6fe4](https://github.com/harbinger-labs/clarative-python/commit/84b6fe4ea09d9554840d5d2bb46a444909bebc16))
* HARB-4439: Update stainless docs link ([6f5e340](https://github.com/harbinger-labs/clarative-python/commit/6f5e3401a7f6b2a6e39fc9c2ae474102cc100c93))


### Bug Fixes

* Include None and Unassigned in API risk level ([039975a](https://github.com/harbinger-labs/clarative-python/commit/039975ad9887c19f3488e5ffdafb2630267c7cfd))


### Chores

* **ci:** bump uv version ([24ca64c](https://github.com/harbinger-labs/clarative-python/commit/24ca64c0b9e721010db65e19d151a0571afd1c95))
* configure new SDK language ([af5cb12](https://github.com/harbinger-labs/clarative-python/commit/af5cb12fe4450fe73d955095b918c3f5b6118da7))
* **internal:** add request options to SSE classes ([e07119b](https://github.com/harbinger-labs/clarative-python/commit/e07119bf89bfcf49a1cd272d02f671978a97f262))
* **internal:** make `test_proxy_environment_variables` more resilient ([78f94f3](https://github.com/harbinger-labs/clarative-python/commit/78f94f339b0ea5e7ff2d188bd85cfc465aa8204e))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([dde6ec1](https://github.com/harbinger-labs/clarative-python/commit/dde6ec1e3c5b64c2b10659e4f8f6180768a606af))
* **internal:** remove mock server code ([a8feef8](https://github.com/harbinger-labs/clarative-python/commit/a8feef8d6a84d6e4fee71dd2bd2ed35ec97f31c6))
* update mock server docs ([f48f1b7](https://github.com/harbinger-labs/clarative-python/commit/f48f1b7fe9ba0ebbe440b6fd4850c26aa371224f))

## 0.0.3 (2026-02-19)

Full Changelog: [v0.0.2...v0.0.3](https://github.com/harbinger-labs/clarative-python/compare/v0.0.2...v0.0.3)

### Chores

* update SDK settings ([f01ea7b](https://github.com/harbinger-labs/clarative-python/commit/f01ea7b64c91512a9f4500950535e55174dcef41))

## 0.0.2 (2026-02-19)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/harbinger-labs/clarative-python/compare/v0.0.1...v0.0.2)

### Features

* Initial Environment and Risk Events ([d9424ec](https://github.com/harbinger-labs/clarative-python/commit/d9424ecfca0d7788ed9a18499f12ac4c3ba74ad6))


### Chores

* update SDK settings ([089efc6](https://github.com/harbinger-labs/clarative-python/commit/089efc6eeea5fbf0315c56723460dd3ad8f8e201))
* update SDK settings ([180efa5](https://github.com/harbinger-labs/clarative-python/commit/180efa5d2373ab199bb245679e696e925c7938a4))
* update SDK settings ([5b0e486](https://github.com/harbinger-labs/clarative-python/commit/5b0e486fb444b8bd04d718ae71758156d35432ad))
