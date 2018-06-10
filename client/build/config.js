const key = process.env.DEPLOY_ENV
const REACT_APP_USERS_SERVICE_URL = process.env.REACT_APP_USERS_SERVICE_URL

const environment = key
const VERSION = '0.1.0'

module.exports = {
  DEPLOYKEY: key,
  ENVIRONMENT: environment,
  VERSION: VERSION,
  REACT_APP_USERS_SERVICE_URL: REACT_APP_USERS_SERVICE_URL,
}
