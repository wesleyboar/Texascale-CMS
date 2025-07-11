#!/usr/bin/env node

const buildStylesheets = require('@tacc/core-styles').buildStylesheets;

const ROOT = __dirname + '/..';
const BUILD_ID = process.env.BUILD_ID || process.env.npm_package_version;
const PROJECT_PATH = 'src/taccsite_custom/texascale_cms/static/texascale_cms/css';

const options = {
  verbose: true,
  buildId: BUILD_ID,
  // If custom configuration is desired, then create and pass this file
  // customConfigs: [`${ROOT}/.postcssrc.extra.yml`],
};

// TODO: Only build individual files as needed
// SEE: https://github.com/TACC/Core-CMS-Custom/blob/5c04616/frontera_assets/bin/build-css.js#L16-L23
buildStylesheets(
  `${ROOT}/${PROJECT_PATH}/src/**/*.css`,
  `${ROOT}/${PROJECT_PATH}/build`,
  options
);
