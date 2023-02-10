from pydantic import BaseSettings
from requests.auth import HTTPBasicAuth


class Settings(BaseSettings):
    debug = True
    allow_origin: str
    # Auth
    auth_client_id: str
    auth_client_secret: str
    auth_jwks_file = "jwks.json"
    auth_hosted_ui: str
    auth_redirect_uri: str
    # S3
    s3_bucket_name: str

    def cognito_auth(self):
        return HTTPBasicAuth(self.auth_client_id, self.auth_client_secret)


settings = Settings()
