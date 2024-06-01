from google_auth_oauthlib.flow import Flow

def get_refresh_token():
    flow = Flow.from_client_secrets_file(
        'client_secret_888112706325-7onak3s0ckp6652jd248r3hdlddmfmq3.apps.googleusercontent.com.json',
        scopes=['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'],
        redirect_uri='http://localhost:8000/accounts/google/login/callback/'
    )
    auth_url, _ = flow.authorization_url(prompt='consent')

    print('Please go to this URL: {}'.format(auth_url))

    code = input('Enter the authorization code: ')
    flow.fetch_token(code=code)

    creds = flow.credentials
    print('Refresh token:', creds.refresh_token)

# Call the function to get the refresh token
get_refresh_token()