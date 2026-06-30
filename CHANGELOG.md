# Changelog

## 4.1.0 (2026-06-30)

Full Changelog: [v4.0.0...v4.1.0](https://github.com/BrainbaseHQ/brainbase-python-sdk/compare/v4.0.0...v4.1.0)

### Features

* **api:** update via SDK Studio ([#61](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/61)) ([9c0c551](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/9c0c551d114f385be676f42aab844de1309b9406))
* clean up environment call outs ([696f18b](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/696f18b140f81774258c1bf92e36e070fbf65c7e))
* **client:** add custom JSON encoder for extended type support ([87eaded](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/87eaded4b920b9cefa1f24e6b3b07b6d522a957e))
* **client:** add follow_redirects request option ([6eb41c9](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/6eb41c9ae22aeeae7139e4cdc0bb9e0f34bb37ff))
* **client:** add support for aiohttp ([6f6ddd9](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/6f6ddd94c735b6bcf82920259c45f2a112f12507))
* **client:** add support for binary request streaming ([41c399b](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/41c399bd7a4dc55e627fefedd31d79a4f959de72))
* **client:** allow passing `NotGiven` for body ([#67](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/67)) ([3ad7f25](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/3ad7f25e58b4823792d6475c7c14a3700273dd13))
* **client:** send `X-Stainless-Read-Timeout` header ([#63](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/63)) ([a594c75](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/a594c7501a919a038a7b4d08754ee837acd45b89))
* **client:** support file upload requests ([fde965a](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/fde965a36bf905c2e8ee5e29013141fca52d6e92))
* improve future compat with pydantic v3 ([bccbddf](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/bccbddf086f9791bcd117701a886c16306c4c4f4))
* **internal/types:** support eagerly validating pydantic iterators ([8e8ca68](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/8e8ca685a548167c7fe8838e7ed42fa90756fb2d))
* **internal:** implement indices array format for query and form serialization ([c601950](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/c601950f359d8897e52fb3d06679441e0fc3b9a5))
* support setting headers via env ([20336c3](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/20336c3c3cbc11c74dd1055d7e3de066c84434f1))
* **types:** replace List[str] with SequenceNotStr in params ([0578887](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/0578887c11b95955522042771b4680d5a9f4f6b9))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#66](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/66)) ([ca310cd](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/ca310cd8beb201d9ad2c66ab13c1e0ed605e6a91))
* avoid newer type syntax ([db10820](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/db108205529a83cadc51c9506fc2c7a8c372d964))
* **ci:** correct conditional ([66eb0ef](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/66eb0ef07df1d265cbb31619ec71f2e097c42f4f))
* **ci:** ensure pip is always available ([#78](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/78)) ([d3d295a](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/d3d295a6a4007e2504000988e6b997a5a96be28b))
* **ci:** release-doctor — report correct token name ([65cdccf](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/65cdccfa4575fb71d6c4947ba13e210537ec181e))
* **ci:** remove publishing patch ([#79](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/79)) ([493f504](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/493f504df7150a24d8373065b217c8b69320b432))
* **client:** add missing f-string prefix in file type error message ([8026d49](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/8026d493cd102704bb9e19049edc17e0bbdef145))
* **client:** close streams without requiring full consumption ([e783145](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/e783145b013ec8af7142e357f9ec4d9d7ddc99b1))
* **client:** correctly parse binary response | stream ([3924997](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/392499744e9c7f7b6d770f243ae700d772663fad))
* **client:** don't send Content-Type header on GET requests ([6bcbc4e](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/6bcbc4e13f22a42e2a69d7f62c8148430bbd88d9))
* **client:** mark some request bodies as optional ([3ad7f25](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/3ad7f25e58b4823792d6475c7c14a3700273dd13))
* **client:** preserve hardcoded query params when merging with user params ([12d00c8](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/12d00c8a277e96e774333e66a9987e897acec1fc))
* compat with Python 3.14 ([f7d6103](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/f7d6103a91fad3aa7aba7eb7174afe1b2cfea3b9))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([898ca7b](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/898ca7bd4cf577eeeab764fbcdd9a77518b44587))
* **deps:** bump minimum typing-extensions version ([323a703](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/323a703c41d2db1f40ffa1277d170017d17d4bed))
* ensure file data are only sent as 1 parameter ([2a24f49](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/2a24f4984b912fff98af394b1854c91dd2dbbdb4))
* ensure streams are always closed ([f89af68](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/f89af6811daed337f503b3c3ad4cb93ab8b38936))
* **package:** support direct resource imports ([ad2d130](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/ad2d130ead5da49f75340d1c642a00854f9d29b6))
* **parsing:** correctly handle nested discriminated unions ([cd511d2](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/cd511d2d51ded4d55af012cdc475c2aa79be5785))
* **parsing:** ignore empty metadata ([bdd8ead](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/bdd8eadd20c5e4f34b85c3b8e922831f5f1074ab))
* **parsing:** parse extra field types ([470d8a8](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/470d8a8851db80f9c3720320a5f51ef214504c52))
* **perf:** optimize some hot paths ([7cc4937](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/7cc4937c3882b956356579443e99826de72a4025))
* **perf:** skip traversing types for NotGiven values ([38509ba](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/38509baa0c8b7fe6cd68ee34fe769ae1c0d95a5c))
* **pydantic v1:** more robust ModelField.annotation check ([3dc3480](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/3dc3480e627d3199117ef6a2b869d413f6408f7b))
* **pydantic:** do not pass `by_alias` unless set ([887a8ec](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/887a8ec60b2687760b400f368f484494d9ec9724))
* sanitize endpoint path params ([40f9b7b](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/40f9b7bbc848731968ce104787a7094e7f281e52))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([539215f](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/539215ff08dfbe906fad296b7a09fbd3a2bdb5bf))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([84b4806](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/84b4806cef26c829d8f2cea180d7db87be025788))
* **types:** handle more discriminated union shapes ([#77](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/77)) ([8b6dcf0](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/8b6dcf01f11bed61a53a66b45ab3ae255deb82e8))
* use async_to_httpx_files in patch method ([6bfd0c0](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/6bfd0c0e4e37cf063c32a82525914a4e6da16546))
* use correct field name format for multipart file arrays ([0f7a6a4](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/0f7a6a4f695744d429f58e1e06d794a935ead24d))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([639db35](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/639db35075e0feefdde737178ca111f05673c22b))


### Chores

* add Python 3.14 classifier and testing ([c172e9c](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/c172e9c16b4ca6fd3c03631a9f58c85c6132de7d))
* broadly detect json family of content-type headers ([febefbc](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/febefbc87ca1d2bbfadc9932400b5ae42644f49a))
* bump `httpx-aiohttp` version to 0.1.9 ([7aeb4c8](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/7aeb4c87f034ee7f506a64adf52a349efb343cf5))
* **ci:** add timeout thresholds for CI jobs ([d5cbcd0](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/d5cbcd06c3d27b71601e34e9ea8fb2a5461ec37d))
* **ci:** change upload type ([d7e4405](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/d7e4405ad6aa676d5f21fe603b705f2bf7d36496))
* **ci:** enable for pull requests ([1ea6fbc](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/1ea6fbc396ca2c40b1233e7e07ab81b6f1b19620))
* **ci:** fix installation instructions ([6291f4a](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/6291f4ad4b3f4ae3624f3ef3dafc3ef5c9ae4ced))
* **ci:** only run for pushes and fork pull requests ([5d00f3e](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/5d00f3ed62f35deb17229244613a788ad45bbdc7))
* **ci:** only use depot for staging repos ([19ee773](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/19ee77377796949bd043a65b8e6934a60a9aa455))
* **ci:** skip lint on metadata-only changes ([287d210](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/287d210640325b4f7c1d30c6d023d076ee415ca1))
* **ci:** skip uploading artifacts on stainless-internal branches ([d12f89a](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/d12f89a1c25c3d7c7fb8075e339d0b5eb9b08ac4))
* **ci:** upgrade `actions/github-script` ([bdad5ed](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/bdad5edd750b61ec763847dc58d60f4eab166a11))
* **ci:** upload sdks to package manager ([598ec7e](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/598ec7e8bf03284b8db9e94049d5e42a1adef26b))
* **client:** minor internal fixes ([1e29d3b](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/1e29d3b13de115b6047b3a712ceeac69f77ba51f))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([fd940b6](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/fd940b62669bcb40a24c2be17e5ab75d116c4ce2))
* do not install brew dependencies in ./scripts/bootstrap by default ([67c48f0](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/67c48f09376cd85fbb5dca63dc47d83c106e7be6))
* **docs:** grammar improvements ([540e711](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/540e711335d2757eb6c76138bb5cc8fceae04ff3))
* **docs:** remove reference to rye shell ([ec32daa](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/ec32daa0c329830982eabdffde4356b3dafdfb41))
* **docs:** update client docstring ([#71](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/71)) ([b41543a](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/b41543a89e16e504054f95ef8987e12bef2da3a2))
* **docs:** use environment variables for authentication in code snippets ([ff7f0ef](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/ff7f0ef0716e3bbe9973b18a4a69b5608376f701))
* fix typos ([#80](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/80)) ([c1576cc](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/c1576ccb8e5592b395e435cc949ba7c077211b67))
* format all `api.md` files ([034e708](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/034e708be77a8e37c70ab108b24b82f20faac2ad))
* **internal/tests:** avoid race condition with implicit client cleanup ([d3a5435](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/d3a5435f4e7c9609de5141ec44639b109758a49b))
* **internal:** add `--fix` argument to lint script ([0b1e68e](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/0b1e68e074af9dc9a8e60a539c964433c66c3887))
* **internal:** add missing files argument to base client ([5547d1b](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/5547d1ba450d6ccb13963d24699f89f487e7dc78))
* **internal:** add request options to SSE classes ([931a27e](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/931a27e24a149745779ec677619475ae74ad28a5))
* **internal:** add Sequence related utils ([5f815ef](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/5f815ef63af5a60d77c4f792f3aaf42b317be58f))
* **internal:** avoid errors for isinstance checks on proxies ([5dc0949](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/5dc09490c13d71ac41d430d78e9c32f8f59c330e))
* **internal:** base client updates ([0ac179a](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/0ac179a512ed4773d3717a4226c7f041c67eab17))
* **internal:** bump dependencies ([5c298f6](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/5c298f6c0ae0a7dadb475d15fea257bfbbdb3a63))
* **internal:** bump pinned h11 dep ([6cafe07](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/6cafe072603e69522dd754cf2d3f2a59b8f49271))
* **internal:** bump pyright version ([81c2baf](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/81c2bafbaab324b6e4c85c1e193148fbe2c88525))
* **internal:** bump rye to 0.44.0 ([#76](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/76)) ([21a20b3](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/21a20b383e1ce4b072bdbcdefc5774f9e2ba21f4))
* **internal:** change ci workflow machines ([656643d](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/656643d1bd5e3bba6a6997ac3ecbce69d0aaf4cc))
* **internal:** codegen related update ([0b4efb7](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/0b4efb79489847366f43e83b5be51c68eddac2bd))
* **internal:** codegen related update ([2f8fbc4](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/2f8fbc4b1ebdcf56188bb58f763e2fb9fd8c202b))
* **internal:** codegen related update ([d6d5a1d](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/d6d5a1d5cf3fec7ee383f25b8927d773a20230ca))
* **internal:** codegen related update ([a145cee](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/a145cee50fe2c30203c1beea85b9e87e58339103))
* **internal:** codegen related update ([#75](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/75)) ([db19786](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/db197864c745b7235e546f349e0a24a7c8cd9801))
* **internal:** detect missing future annotations with ruff ([23b94ed](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/23b94edc4b2f2e1ab1b8ed02881296a185b3ccac))
* **internal:** expand CI branch coverage ([7fd1145](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/7fd1145852e5f82cd271dcb4432e2474e1cbd9d4))
* **internal:** fix devcontainers setup ([#68](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/68)) ([97b7254](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/97b725436eaca395261fa04119202ccd938e2edd))
* **internal:** fix lint error on Python 3.14 ([1d9c80a](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/1d9c80a25ab60a7c954f5fd4ed7f1b60dc6ba3c4))
* **internal:** fix list file params ([1b5e333](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/1b5e333c271ee804b2fe7738dfb2ee7bd0044c9a))
* **internal:** fix ruff target version ([1437b86](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/1437b86f88760d95f63a3cd9e5e4e3d1b9cc1673))
* **internal:** fix type traversing dictionary params ([#64](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/64)) ([1322c80](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/1322c808afea9e8d17ac958e289850115c8d0fe8))
* **internal:** grammar fix (it's -&gt; its) ([8b1cdb7](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/8b1cdb737ecd09456400b79a03d1aa2d02ab8e2b))
* **internal:** import reformatting ([8a3f6f0](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/8a3f6f0fc98525d48998f38b6bafc6b78bbea73d))
* **internal:** make `test_proxy_environment_variables` more resilient ([f79d30c](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/f79d30c32f9c5943c226a4873b00a7c5eaf18b2d))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([08e33e4](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/08e33e43f929ddfae112287a7ce87a9ab8bab92e))
* **internal:** minor type handling changes ([#65](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/65)) ([7e69125](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/7e691251edd799b8ffd067792c0833f99a6906bb))
* **internal:** more robust bootstrap script ([449a9c3](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/449a9c30d635c6b277eb2c495d564bcf57090349))
* **internal:** move mypy configurations to `pyproject.toml` file ([f87b268](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/f87b2684a44a8c6112fa30fd935e42d9d532fdbf))
* **internal:** properly set __pydantic_private__ ([#69](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/69)) ([bc25b84](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/bc25b84c059996c26d435aa61da24f684b25f2e8))
* **internal:** reduce CI branch coverage ([2492996](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/249299619c40b6abeef1332f3c3e33e436fe5da5))
* **internal:** refactor retries to not use recursion ([055e329](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/055e329cdf3927632ab1e4b128c2ed5ce0333e8f))
* **internal:** reformat pyproject.toml ([5b57987](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/5b57987241093abe10e025109f392fcd99650b2c))
* **internal:** remove extra empty newlines ([#74](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/74)) ([3d90dff](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/3d90dff0832619c6495bbf7f82cc74ac9aac46c9))
* **internal:** remove mock server code ([cb06a16](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/cb06a163037d34e5de3b94a457f4108e4df5f415))
* **internal:** remove trailing character ([#81](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/81)) ([4cfa80b](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/4cfa80bf1f6a9f24ae0a7244b3ae5a248e131edc))
* **internal:** remove unused http client options forwarding ([#72](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/72)) ([69a44e3](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/69a44e38bcfb88f523e036d4f434942a96397061))
* **internal:** slight transform perf improvement ([#82](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/82)) ([5498eaf](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/5498eaf9154b388668be1a516d3597d27b74cc7c))
* **internal:** tweak CI branches ([2372dd8](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/2372dd83cc92834fae8d3a037b952b7263904261))
* **internal:** update `actions/checkout` version ([54d6bd9](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/54d6bd9925eeb5c9effab29b7be1257c60c6679c))
* **internal:** update comment in script ([103820e](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/103820ebecd7a1dd118282d8becf5db502a1ec0d))
* **internal:** update conftest.py ([83531b4](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/83531b46d24f38f1f7c6a3ca13ddbb4e5d16590b))
* **internal:** update gitignore ([15b9637](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/15b9637d6c5030288c36a57b04db9a2371a9b93a))
* **internal:** update models test ([421a2b5](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/421a2b57d0973344ae3d86ec0f989ca655490970))
* **internal:** update pydantic dependency ([5dd09a4](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/5dd09a48ae3a7ef8efe86304ea1d84acd0bf7d39))
* **internal:** update pyright exclude list ([f306088](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/f3060880c80762252f85cb071eae6b7c1263265f))
* **internal:** update pyright settings ([2d267e1](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/2d267e1d9a8fee34b0dde0ca9274afac975a1648))
* **package:** drop Python 3.8 support ([95ca18d](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/95ca18d4426eac5714e12b54f5f0fb181aaa85e6))
* **package:** mark python 3.13 as supported ([06ad64f](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/06ad64facff9ca27b1049dc9bc2a41aa1872b7ee))
* **project:** add settings file for vscode ([6754b39](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/6754b3937cfa144183e8d4633efdd19e2d0e1413))
* **readme:** fix version rendering on pypi ([b1e9e51](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/b1e9e51bb3adf1c0f2387b4aff1804ff6e40e346))
* **readme:** update badges ([f3f214f](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/f3f214f315d721421f383ba4b5e63ddd828c0b59))
* speedup initial import ([3b3f4e6](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/3b3f4e63e4488509e60062a71cf5f3f569b4e529))
* **tests:** add tests for httpx client instantiation & proxies ([5e172cd](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/5e172cd1be541e04ab62ef1c770b5d1e9b7fc44d))
* **tests:** run tests in parallel ([497b381](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/497b3816f4167e344dbbad4a2910236436641777))
* **tests:** simplify `get_platform` test ([ef07d85](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/ef07d85cf3d9001104e57e9e1a266aa65f6852e5))
* **tests:** skip some failing tests on the latest python versions ([39d037c](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/39d037c9713c26103a549a3b0c03003a93ef3fc4))
* **types:** change optional parameter type from NotGiven to Omit ([14cb9a9](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/14cb9a994e36c901e9b73ca1004a40cb30f87786))
* update @stainless-api/prism-cli to v5.15.0 ([d766a01](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/d766a015e4fd9a56336bf37be4cce0eb08361a20))
* update github action ([d0f9d9e](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/d0f9d9e2bd470f7ee9f2c29cf514d9a9da093c0b))
* update lockfile ([77726a0](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/77726a0c2aeb678ef7995da7be5aa667388917ca))
* update mock server docs ([1241c00](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/1241c004a7596c895f10f2e165057bddae9d0f69))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([3341b85](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/3341b85797cfcc35e3e8c1f3a151176c85587ec8))
* update URLs from stainlessapi.com to stainless.com ([#70](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/70)) ([08062c4](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/08062c48906749ce529d5ea1fcdfed3b1b18412c))

## 4.0.0 (2025-02-04)

Full Changelog: [v3.0.0...v4.0.0](https://github.com/BrainbaseHQ/brainbase-python-sdk/compare/v3.0.0...v4.0.0)

### Features

* **api:** update via SDK Studio ([#58](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/58)) ([a36fbfd](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/a36fbfd33d803dcb51826108315826af5dffa6e4))

## 3.0.0 (2025-02-04)

Full Changelog: [v2.2.0...v3.0.0](https://github.com/BrainbaseHQ/brainbase-python-sdk/compare/v2.2.0...v3.0.0)

### Features

* **api:** update via SDK Studio ([#55](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/55)) ([21dbb8d](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/21dbb8db01ce953e1154f77ac1cc795ba727cf4c))

## 2.2.0 (2025-02-04)

Full Changelog: [v2.1.0...v2.2.0](https://github.com/BrainbaseHQ/brainbase-python-sdk/compare/v2.1.0...v2.2.0)

### Features

* **api:** update via SDK Studio ([#50](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/50)) ([a665c00](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/a665c00b172f0c41789098e6e50b959c5bb38c15))
* **api:** update via SDK Studio ([#52](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/52)) ([95bff55](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/95bff55484b4d252fdd34cc1bd14f096059eaf45))
* **api:** update via SDK Studio ([#53](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/53)) ([f84535e](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/f84535eec8e1162afe8f0046d32955cd904d7d78))

## 2.1.0 (2025-02-04)

Full Changelog: [v2.0.0...v2.1.0](https://github.com/BrainbaseHQ/brainbase-python-sdk/compare/v2.0.0...v2.1.0)

### Features

* **api:** update via SDK Studio ([#47](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/47)) ([3ae3d6f](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/3ae3d6f3c42b706ce9e640f399723fe0165cfffd))

## 2.0.0 (2025-02-04)

Full Changelog: [v0.1.0-alpha.1...v2.0.0](https://github.com/BrainbaseHQ/brainbase-python-sdk/compare/v0.1.0-alpha.1...v2.0.0)

### Features

* **api:** update via SDK Studio ([#43](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/43)) ([6a4d364](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/6a4d364cc3740780ade0a8bb2168fe5060125848))
* **api:** update via SDK Studio ([#45](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/45)) ([1011b13](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/1011b13fd27121a9e8ef357811ddac287a28de0b))

## 0.1.0-alpha.1 (2025-02-04)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/BrainbaseHQ/brainbase-python-sdk/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([#10](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/10)) ([4fb75c8](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/4fb75c8c78c172cb0a80be304334803956968247))
* **api:** update via SDK Studio ([#12](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/12)) ([a363549](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/a3635498129383f20cae75014ad9720e18cc7ec6))
* **api:** update via SDK Studio ([#18](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/18)) ([5f5451c](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/5f5451cebcda05a40deef4104207be19e5f8e8ac))
* **api:** update via SDK Studio ([#23](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/23)) ([b2bbdf6](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/b2bbdf640fa7b0b9163f0a7a6b8ab964cb2c1fa5))
* **api:** update via SDK Studio ([#33](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/33)) ([9254242](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/9254242f08a8f3f0da2a3b101fd07776022487d4))
* **api:** update via SDK Studio ([#35](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/35)) ([91c7c39](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/91c7c396731fc46c41a031b2235e0e9562acea8f))
* **api:** update via SDK Studio ([#38](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/38)) ([bc32c04](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/bc32c04421def2b0a84a5def7f5a4bb08546d704))
* **api:** update via SDK Studio ([#40](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/40)) ([801bbaa](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/801bbaaddaddba829cf554d8b0ee0bc4c229ee40))
* **api:** update via SDK Studio ([#41](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/41)) ([fb611f9](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/fb611f97127b4b491884acf8ccd636ebea0e858c))
* **api:** update via SDK Studio ([#8](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/8)) ([312b657](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/312b657cf73569a314b3c64ed83521ca2bb576a5))


### Chores

* go live ([#1](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/1)) ([db8a29c](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/db8a29c23e871872bcfc26b15bc7e4b27b0b08b3))
* remove custom code ([e685c86](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/e685c866f3f2b482e1d899a475a5d140ca134938))
* sync repo ([cce7924](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/cce79248b7058f58c4fe7d98ea36ed534403c7a7))
* update SDK settings ([#3](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/3)) ([c5e3c22](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/c5e3c223ba6a7df56e290877e55c31e81c1d4b52))
* update SDK settings ([#5](https://github.com/BrainbaseHQ/brainbase-python-sdk/issues/5)) ([1e74403](https://github.com/BrainbaseHQ/brainbase-python-sdk/commit/1e744032bc5800bb1b4f97a703cfdd1a7a7dd922))
